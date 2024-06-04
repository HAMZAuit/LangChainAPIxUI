# Langchain-UI
# app.py
Langchain-UI is a FastAPI application that uses the OpenAI API to generate presentation content. It also uses the Wikipedia API for research purposes.

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install the required packages using pip:

```sh
pip install -r requirements.txt
```
## Usage
# Run the application using uvicorn:
```sh
uvicorn app:app --host 0.0.0.0 --port 8000
```
# The application provides several endpoints:

/generate-menu: Generates a menu for a presentation

/generate-title: Generates a title for a presentation

/generate-script: Generates a script for a presentation

/wikipedia-research: Conducts Wikipedia research based on a given prompt

/generate-presentation-content: Generates a complete presentation


# appUI.py
appUI is a FastAPI application that uses the OpenAI API to generate presentation content. It also uses the Wikipedia API for research purposes.

# Dependencies
* Python 3.6+
* FastAPI
* OpenAI
* Wikipedia API
# Setup
* Clone the repository.
* Navigate to the project directory.
* Install the dependencies using pip:
```sh
pip install -r requirements.txt
```
# Usage
Run the application using uvicorn:
```sh
uvicorn app:app --reload
```
* pen the app in your web browser.
* Enter a topic in the text input field.
* The app will generate a presentation title and content based on your topic.
# How it Works
The app uses the OpenAI API to generate the presentation title and content. It first generates a title based on the user's topic. It then fetches relevant Wikipedia data based on the topic and generates the presentation content based on the title and the Wikipedia data.

The app displays the generated title and content, as well as the history of the title and content generation and the fetched Wikipedia data.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.