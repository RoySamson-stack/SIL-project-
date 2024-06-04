# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y libcairo2-dev libglib2.0-dev libpixman-1-dev libuuid1 libfreetype6-dev libpng-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
