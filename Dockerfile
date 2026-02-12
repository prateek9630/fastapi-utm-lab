FROM python:3.11-slim

WORKDIR /app

# Make sure Python can find your modules inside /app
ENV PYTHONPATH=/app

# Copy requirements first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire app folder (this is the important fix)
COPY app/ app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
