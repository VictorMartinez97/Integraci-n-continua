FROM python:3.9-slim

RUN pip install requests

COPY script.py /app/script.py

WORKDIR /app

CMD ["python", "script.py"]
