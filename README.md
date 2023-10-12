# Tab Researcher
An AI assistant to help you research the market for a Tablet Phone, to help you make a decision according to your needs.

## Dependencies
1. Python v3.11
2. [Poetry](https://python-poetry.org/)
3. An OpenAI API key
4. [SerpApi API key](https://serpapi.com) - Used to provide Google search capabilities

## Setup
1. Once you have all the dependencies setup, create a `.env` file, the keys to which is provided in `.env.sample` file, and fill in the appropriate values.
2. Use `poetry env use python3.11` to make Python v3.11 is used for the virtual environment.
3. Use `poetry init` to install the dependencies.
4. Use `poetry run python -m tab_researcher.main` to run the assistant.