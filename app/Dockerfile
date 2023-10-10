# Use the official Python image as the base image
FROM python:3.10-slim

WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Install the required dependencies
RUN pip install -r /app/requirements.txt

# Copy the content of the local app directory into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Run the command to start the app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-t", "0", "-w", "1", "run:app"]