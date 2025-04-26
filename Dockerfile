# Use an official Python runtime as a parent image
#FROM python:2.7 this version is already obsolet so we changed to 3.9

FROM python:3.9

LABEL maintainer="Soubhi Hadri <soubhi.hadri@gmail.com>"

# Install OS-level dependencies including libGL
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set the working directory to /DHC app
WORKDIR /DHC_app

# Copy the current directory contents into the container at /app
ADD . /DHC_app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=World

# Run hand_gestures_detector.py when the container launches
CMD ["python", "hand_gestures_detector.py"]