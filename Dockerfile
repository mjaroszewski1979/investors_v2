# Use the official Python 3 image from the Docker Hub
FROM python:3

# Set the environment variable to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from the host to the container's working directory
COPY requirements.txt ./

# Upgrade pip to the latest version
RUN pip3 install --upgrade pip

# Install the Python dependencies listed in requirements.txt
RUN pip3 install -r requirements.txt

# Copy all files from the host to the container's working directory
COPY . .

# Set the entrypoint to run the entrypoint.sh script using the sh shell
ENTRYPOINT ["sh", "entrypoint.sh"]


