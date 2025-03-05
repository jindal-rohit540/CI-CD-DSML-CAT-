# Use an official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /flask-docker

# Upgrade pip
RUN python3 -m pip install --upgrade pip


# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Copy all files into the container
COPY . .

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run Flask when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

