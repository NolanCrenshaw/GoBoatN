import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { BASE_URL } from "../../config";

const content = {
  inputs: [
    {
      label: "Email",
      name: "email",
      type: "email",
    },
    {
      label: "Password",
      name: "password",
      type: "password",
    },
  ],
};

const schema = yup.object().shape({
  email: yup.string().required().email(),
  password: yup.string().required().min(6),
});

const LoginForm = ({ loginToggle }) => {
  const [submittedData, setSubmittedData] = useState({});

  // React Hook Form Ctrl w/ Yup Validation
  const { register, handleSubmit, errors } = useForm({
    resolver: yupResolver(schema),
  });

  const onSubmit = (data, e) => {
    e.preventDefault();
    setSubmittedData(data);
    // e.target.reset();
  };

  useEffect(() => {
    if (submittedData.password !== undefined) {
      const loginCall = async () => {
        const res = await fetch(`${BASE_URL}/api/auth/login`, {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(submittedData),
        });
        if (!res.ok) {
          // -- TODO -- ERROR HANDLING
          console.log("loginCall res Failure");
        } else {
          const json = await res.json();
          if (json.auth_token === undefined) {
            // -- TODO -- Handling
            console.log("auth_token === undefined");
          } else {
            window.localStorage.setItem("auth_token", json.auth_token);
            loginToggle();
          }
        }
      };
      loginCall();
    }
  }, [submittedData]);

  return (
    <div className="loginform-container form">
      <h2>Login</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        {content.inputs.map((input, key) => {
          return (
            <div className="form_element" key={key}>
              <div>
                <label>{input.label}</label>
                <p>{errors[input.name]?.message}</p>
              </div>
              <input name={input.name} type={input.type} ref={register} />
            </div>
          );
        })}
        <button className="form_button" type="submit">
          Submit
        </button>
      </form>
    </div>
  );
};

export default LoginForm;