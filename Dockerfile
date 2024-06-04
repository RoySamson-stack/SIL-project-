FROM python:3.11-slim

# Update package list and install necessary packages
RUN apt-get update && \
    apt-get install -y \
    libcairo2-dev \
    libglib2.0-dev \
    libpixman-1-dev \
    libuuid1 \
    libfreetype6-dev \
    libpng-dev \
    gettext && \
    apt-get clean

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Add any additional commands you need here
