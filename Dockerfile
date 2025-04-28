# Use the langchain/langchain image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only requirements file first for better caching
COPY requirements.txt .

# Install build dependencies (compilers, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    make \
    libffi-dev \
    python3-dev \
    libatlas-base-dev \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Update pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the default command to run your application
CMD ["python", "main.py"]