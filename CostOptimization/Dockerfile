
# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire CostOptimization directory into the container
COPY . .

# Expose the port that the API will listen on
EXPOSE 8000

# Set the command to run the API using FastAPI
CMD ["uvicorn", "fast_api:app", "--host", "0.0.0.0", "--port", "8000"]
