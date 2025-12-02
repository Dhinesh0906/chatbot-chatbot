FROM ollama/ollama:latest


RUN apt update && apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    pkg-config

WORKDIR /app

COPY requirements.txt .
COPY app.py .


RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ollama serve & \
    sleep 8 && \
    ollama pull phi && \
    python3 app.py
