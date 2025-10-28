# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files ke container
COPY . .

# Expose port untuk Railway
EXPOSE 8000

# Run Flask
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
