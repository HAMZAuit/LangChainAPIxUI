# Langchain-UI

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



# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

