# Use the official Python 3.10 Alpine image as the base image
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY /src/app.py /app/app.py

# Install any dependencies if required (uncomment and modify if needed)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python application
CMD ["python", "app.py"]