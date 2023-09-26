# Use an official Python image that supports Python 3.8 or higher
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the required Python packages
RUN pip install -r requirements.txt

# Define the command to run your application
CMD ["python", "app.py"]
