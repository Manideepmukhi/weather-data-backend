
FROM python:3.10-slim


WORKDIR /app


COPY . .


RUN pip install --no-cache-dir -r requirements.txt


ENV PYTHONUNBUFFERED=1


EXPOSE 5000


CMD ["python", "main.py"]
