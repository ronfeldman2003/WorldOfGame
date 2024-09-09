FROM python:3.12-slim

WORKDIR /app
COPY MainScores.py Utils.py /app/
RUN pip install flask
RUN apt-get update && apt-get install -y curl

EXPOSE 3000
EXPOSE 8777


CMD ["python","MainScores.py"]
