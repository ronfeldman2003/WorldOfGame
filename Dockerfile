FROM python:3.12-slim

WORKDIR /app
COPY MainScores.py Utils.py /app/
RUN pip install flask
EXPOSE 3000
USER 1000
VOLUME /app/tmp


CMD ["python","MainScores.py"]