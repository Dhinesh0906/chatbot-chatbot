FROM ollama/ollama:latest


RUN ollama pull phi

EXPOSE 11434

CMD ["ollama", "serve"]
