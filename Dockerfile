FROM python:3.11-slim

# Set the working directory inside the Docker container
WORKDIR /app

# Update package list and install necessary packages
RUN apt-get update && \
    apt-get install -y \
    gcc \
    libcairo2-dev \
    libglib2.0-dev \
    libpixman-1-dev \
    libuuid1 \
    libfreetype6-dev \
    libpng-dev \
    gettext \
    libsystemd-dev \
    libcups2-dev \
    libffi-dev \
    gobject-introspection \
    libgirepository1.0-dev \
    pkg-config \
    librsync-dev \
    lsb-release \
    software-properties-common \
    && apt-get clean

# Add PPA for duplicity dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    librsync-dev \
    python3-dev \
    libssl-dev \
    && apt-get clean

# Copy only the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the app runs (default for Django)
EXPOSE 8000

# Command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
