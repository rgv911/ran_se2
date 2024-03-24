FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install gunicorn

EXPOSE 5002
CMD ["gunicorn", "-b", "0.0.0.0:5002", "app:app"]
