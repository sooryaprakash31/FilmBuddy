# Use the official Python image as the base image
FROM python:3.8-slim

WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Install the required dependencies
RUN pip install -r /app/requirements.txt

# Copy the content of the local app directory into the container
COPY . /app

# Set environment variables
ENV FLASK_APP app/init.py
ENV FLASK_RUN_HOST 0.0.0.0

# Expose the port the app runs on
EXPOSE 5000

# Run the command to start the app
CMD ["flask", "run"]
