# Use an official Python base image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y msodbcsql17 unixodbc-dev curl gnupg

# Set the working directory in the container
WORKDIR /src

# Copy your code and requirements file into the container
COPY . /src

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
