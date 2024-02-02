# Use a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirement.txt .

# Install the dependencies
RUN pip install -r requirement.txt

# Copy the main.py file into the container
COPY main.py .

# Set the command to run when the container starts
CMD ["python", "main.py"]
