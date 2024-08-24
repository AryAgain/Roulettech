import React, { useState } from 'react';
import RandomDish from './components/RandomDish';
import CookingTimer from './components/CookingTimer';
import './App.css'; 

function App() {
    const [dish, setDish] = useState('');

    return (
        <div className="App">
            <h1>Recipe Suggestion</h1>
            <RandomDish setDish={setDish} />
            <h3>Dish: {dish}</h3>
            <CookingTimer dish={dish} />
        </div>
    );
}

export default App;
