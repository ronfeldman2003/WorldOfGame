FROM python:3.12-slim

WORKDIR /app
COPY MainScores.py Utils.py /app/
RUN pip install flask
EXPOSE 3000
RUN mkdir -p /app/tmp && chmod 777 /app/tmp


CMD ["python","MainScores.py"]