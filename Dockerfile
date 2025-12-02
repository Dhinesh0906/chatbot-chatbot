FROM ollama/ollama:latest

RUN ollama pull phi

EXPOSE 5000

COPY app.py /app/app.py
WORKDIR /app

RUN apt update && apt install -y python3 python3-pip
RUN pip3 install flask requests

CMD ["python3", "app.py"]
