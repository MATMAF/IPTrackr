FROM python:3.10

EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "-m", "gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "wsgi:app"]
