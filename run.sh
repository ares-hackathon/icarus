#!/bin/bash

export MODEL_NAME=ollama/qwen3:0.6b

# Start Ollama in the background.
ollama serve &

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve defualt model..."
# ollama pull mistral-nemo:latest
ollama pull $(echo ${MODEL_NAME} | cut -f2 -d/)
echo "🟢 Done!"

python -m streamlit run main.py
