import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './CookingTimer.css';

const CookingTimer = ({ dish }) => {
    const [timeLeft, setTimeLeft] = useState(0);

    const startTimer = () => {
        axios.post('http://localhost:8000/api/start-timer/', { dish })  // Send the dish name in the request body
            .then(response => {
                setTimeLeft(response.data.cooking_time);
            })
            .catch(error => {
                console.error("There was an error starting the timer!", error);
            });
    };

    useEffect(() => {
        if (timeLeft > 0) {
            const timerId = setInterval(() => {
                setTimeLeft(prevTime => prevTime - 1);
            }, 1000);

            return () => clearInterval(timerId);
        }
    }, [timeLeft]);

    return (
        <div>
            <button onClick={startTimer} disabled={!dish}>Start Cooking</button>
            {timeLeft > 0 && <h3>Time Left: {Math.floor(timeLeft / 60)}:{timeLeft % 60}</h3>}
        </div>
    );
};

export default CookingTimer;
