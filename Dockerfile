FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt MainScores.py Utils.py /app/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y curl

EXPOSE 3000
EXPOSE 8777


CMD ["python","MainScores.py"]
