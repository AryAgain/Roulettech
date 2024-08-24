# Recipe Suggestion App

A simple and elegant web application that suggests random recipes and provides a cooking timer for each dish. The frontend is built using React.js, and the backend is powered by Django with Django REST Framework.

## Features

- **Random Recipe Suggestion**: Click a button to get a randomly selected dish from a variety of cuisines.
- **Cooking Timer**: Start a cooking timer based on the selected dish's cooking time.
- **Responsive Design**: The application is styled with a modern, minimalist design, ensuring it looks good on all devices.

## Technologies Used

- **Frontend**: React.js
- **Backend**: Django, Django REST Framework
- **Styling**: Custom CSS

## Installation

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- Node.js (with npm)
- Git

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/recipe-suggestion-app.git
   cd recipe-suggestion-app

2. Navigate to the backend directory:
    
    ```bash
    cd recipe_backend

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate


4. Install the Python dependencies:

    ```bash
    pip install -r requirements.txt


5. Run the Django development server:

    ```bash
    python manage.py migrate
    python manage.py runserver


The backend should now be running at http://localhost:8000.


## Frontend Setup

1. Navigate to the frontend directory:

    ```bash
    cd ../recipe-frontend

2. Install the JavaScript dependencies:

    ```bash
    npm install


3. Start the React development server:

    ```bash
    npm start


The frontend should now be running at http://localhost:3000.


## API Endpoints
1. Random Dish Endpoint
URL: /api/random-dish/
Method: GET
Description: Returns a randomly selected dish name from a predefined list of dishes.

2. Cooking Timer Endpoint
URL: /api/start-timer/
Method: POST
Description: Starts a cooking timer based on the dish name provided in the request. The response includes the cooking time in seconds.

## Usage
- Open your browser and navigate to http://localhost:3000.
- Click the "What to cook today?" button to get a random dish suggestion.
- Once a dish is selected, click "Start Cooking" to begin the timer.