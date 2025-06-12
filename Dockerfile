FROM python:3.12-slim

WORKDIR /app

# Install dependencies for wait-for-it.sh
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Copy app files and requirements
COPY app /app/app
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create app user and permissions
RUN useradd -m appuser
RUN mkdir -p /app/app/logs && chown -R appuser /app/app/logs

# Add wait script and set executable permission
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Use non-root user
USER appuser

# Run with wait-for-it
CMD ["./wait-for-it.sh", "db", "5432", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
