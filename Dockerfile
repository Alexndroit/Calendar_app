# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the PYTHONPATH to ensure proper module resolution
ENV PYTHONPATH=/app

# Expose the port that the FastAPI app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "calendar_crud_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

RUN pip install email-validator
