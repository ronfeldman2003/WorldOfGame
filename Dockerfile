FROM python:3.12-slim

WORKDIR /app
COPY MainScores.py Utils.py /app
COPY Scores.txt /app/Scores.txt
RUN pip install flask
EXPOSE 3000

CMD ["python","MainScores.py"]