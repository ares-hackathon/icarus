#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve defualt model..."
# ollama pull mistral-nemo:latest
ollama pull $(echo ${MODEL_NAME} | cut -f2 -d/)
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid
