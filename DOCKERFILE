# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Run Gunicorn as the default command
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
