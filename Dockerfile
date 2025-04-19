# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first and install dependencies
COPY requirements.txt .
# Before installing requirements
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY ./app /app

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
