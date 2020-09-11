import React from 'react';
import { API_URL } from '../config';
import '../styles/landing.css';
import canoeBackgroundSlice from '../images/canoe-background-slice';

// React Component
const Landing = props => {

    // State

    // Listen

    // Functions


// ---- Component Render ---- //

    // Render
    return (
        <div className="landing-root--container">
            <div className="landing">
                <div className="landing__picture-box">
                    <span>
                        Photo by <a href="https://unsplash.com/@antipodos?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Michael Niessl</a> on <a href="https://unsplash.com/s/photos/river?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a>
                    </span>
                </div>
                <div className="landing__notifications-c">
                    <div className="landing__notifications--invites"></div>
                    <div className="landing__notifications--weather"></div>
                </div>
            </div>
        </div>
    )
}
export default Landing;