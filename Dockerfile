FROM python:3.12-slim

WORKDIR /app
COPY MainScores.py /app
COPY Utils.py /app
RUN pip install flask
EXPOSE 5000

CMD ["python","MainScores.py"]