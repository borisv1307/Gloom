# Gloom
Gloom is a UI tracker for playing Gloomhaven. 
- The backend is built with Flask and Python3 and generates all the game entities (tiles, rooms, dungeons, monsters, characters)
- The frontend is built with React that renders constructed rooms based on JSON data fetched from the Flask server.

## Backend
### Build and Run
- Navigate to `backend/src/main` and install the requirements: 
```pip install -r requirements.txt```

- To start the flask server locally, navigate to the project root and type the following command:

`PYTHONPATH=. python backend/src/main/flask/app.py`

Your terminal should output the following:
```
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 283-466-228
```
**The backend is now serving a JSON payload detailing what the random map should look like to React** 

## Frontend
### Build and Run
- Pre-requisites: [Install npm](https://www.npmjs.com/get-npm)
- To install the dependencies for Gloom, navigate to `web/app/` and type:

``npm install``

- After the dependencies have successfully been installed, and the Flask server is running in the background, to start the react app type:

`` npm start``
