FROM python:3.12.4-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "wsgi:app"]
