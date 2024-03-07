# Base image
FROM python:3.7-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Make run.sh executable
RUN chmod +x run.sh

# Command to run the application
CMD ["./run.sh"]
