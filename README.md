# ICARUS: Intentionally Compromisable Agent for Red-teaming and Usage Simulation


## Introduction
Welcome to *ICARUS: Intentionally Compromisable Agent for Red-teaming and Usage Simulation*!
This project is a sample chatbot powered by a Large Language Model (LLM) ReAct agent, implemented with Langchain, heavily "inspired" by [Damn Vulnerable LLM Agent](https://github.com/ReversecLabs/damn-vulnerable-llm-agent).
It's designed to be an educational tool for security researchers, developers, and enthusiasts to understand and experiment with prompt injection attacks in ReAct agents. 



## Features
- Simulates a vulnerable chatbot environment.
- Allows for prompt injection experimentation.
- Provides a ground for learning prompt injection vectors.

## Installation

### Pipenv Installation

To get started, you need to set up your Python environment by following these steps:

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Running the Application

Before running the application, you need to setup a .env file based on the provided env templates.

### To run using ollama locally
- Create a .env by copying .env.ollama.template.
- Change the default model to any ollama model you want to use by editing `llm-config.yaml`
- Install [Ollama](https://github.com/ollama/ollama)
- ollama pull mistral-nemo

Note: Please note that small LLMs do not perform very well as ReACT agents. In our testing `mistral-nemo` appeared to be sufficiently reliable. It is possible that you may not see reasonable results with most small models.

### To run the application:

```sh
python -m streamlit run main.py
```

### Docker Image

To build and run the Docker image:

```sh
docker build -t icarus .

# Populate the env.list with necessary environment variables (just the OpenAI API key), then run:
docker run --env-file env.list -p 8501:8501 dvla
```

### Docker Compose 

To run directly with docker compose:

```sh
docker compose up
```

The system will be spinned up including Ollama, and will be available on `http://localhost:8501`

## Usage

To interact with the vulnerable chatbot and test prompt injection, start the server and begin by issuing commands and observing responses.

## License

This project is released open-source under the Apache 2.0 license. By contributing to the Damn Vulnerable LLM Agent, you agree to abide by its terms.

## Contact

For any additional questions or feedback, please [open an issue](https://github.com/ares-hackathon/icarus/issues) on the repository.
