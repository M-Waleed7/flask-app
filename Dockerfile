FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create directory for SQLite database
RUN mkdir -p /app/data

EXPOSE 9090

CMD ["python", "app.py"]
