FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies and code
RUN pip install --upgrade pip
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
