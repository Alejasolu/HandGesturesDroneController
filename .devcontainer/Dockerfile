# Use an official Python runtime as a parent image
#FROM python:2.7 this version is already obsolet so we changed to 3.9

FROM python:3.9

LABEL maintainer="Soubhi Hadri <soubhi.hadri@gmail.com>"



# Set the working directory to /DHC app
WORKDIR /workspace

# Copy requirements.txt in the current directory to the container
COPY requirements.txt .
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y\
#new
        ffmpeg \
        libsm6 \
        libxext6 \
        python3-tk \
        && rm -rf /var/lib/apt/lists/*
        #----

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=World

# Run hand_gestures_detector.py when the container launches
CMD ["bash"]