# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    libcairo2-dev \
    libxcb1-dev \
    libxcb-render0-dev \
    libxcb-shm0-dev \
    gcc \
    g++

# Set environment variables for compilation
ENV CFLAGS="-fPIC"
ENV LDFLAGS="-fPIC"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
