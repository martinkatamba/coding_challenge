
FROM python:3.12.3 as builder

# Declare environment variables to be used in the image
ARG MYSQL_DB_HOST
ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD

ENV MYSQL_DB_HOST=${MYSQL_DB_HOST} \
    MYSQL_DATABASE=${MYSQL_DATABASE} \
    MYSQL_USER=${MYSQL_USER} \
    MYSQL_PASSWORD=${MYSQL_PASSWORD}

# Set the working directory
WORKDIR /app

# Install dependencies and tools in one layer, and clean up to save space
RUN apt-get update && apt-get install -y \
    git-all \
    python3-dev \
    cmake \
    build-essential \
    libssl-dev \
  && python3 -m pip install --upgrade pip setuptools wheel \
  && apt-get purge -y --auto-remove \
  && rm -rf /var/lib/apt/lists/*

# Copy the application code to the image
COPY . .

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Expose the port the application will run on
EXPOSE 8000

# Set the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
