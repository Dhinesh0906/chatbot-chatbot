FROM ollama/ollama:latest


RUN apt update && apt install -y python3 python3-pip

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 5000


CMD ollama serve & \
    sleep 5 && \
    ollama pull phi && \
    python3 app.py
