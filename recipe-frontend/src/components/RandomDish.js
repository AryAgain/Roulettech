import React, { useState } from 'react';
import axios from 'axios';
import './RandomDish.css';

const RandomDish = ({ setDish }) => {
    const fetchDish = () => {
        axios.get('http://localhost:8000/api/random-dish/')
            .then(response => {
                setDish(response.data.dish);  // Pass dish name to parent component
            })
            .catch(error => {
                console.error("There was an error fetching the dish!", error);
            });
    };

    return (
        <div>
            <button onClick={fetchDish}>What to cook today?</button>
        </div>
    );
};

export default RandomDish;
