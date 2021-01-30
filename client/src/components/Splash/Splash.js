import React, { useEffect, useState } from "react";

import LoginForm from "../_forms/LoginForm";
import SignupForm from "../_forms/SignupForm";

const Splash = ({ loginToggle }) => {
  const [toggleUI, setToggleUI] = useState(false);
  const [toggleBtn, setToggleBtn] = useState("Log In");

  useEffect(() => {
    toggleUI ? setToggleBtn("Sign Up") : setToggleBtn("Log In");
  }, [toggleUI]);

  return (
    <div className="splash-container">
      <nav>
        <button className="nav_button" onClick={() => setToggleUI(!toggleUI)}>
          {toggleBtn}
        </button>
      </nav>
      <div className="splash_img">
        <img
          alt="Splash Image"
          src="https://goboatnbucky.s3.us-east-2.amazonaws.com/josh-wedgwood-river-etive-unsplash.jpg"
        />
      </div>
      <div className="splash_panel">
        {toggleUI ? (
          <LoginForm loginToggle={loginToggle} />
        ) : (
          <SignupForm loginToggle={loginToggle} />
        )}
      </div>
      <footer></footer>
    </div>
  );
};

export default Splash;