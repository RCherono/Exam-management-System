# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in container
WORKDIR /app

# Copy the current directory contents into the container at /app/
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
