#docker image build -t docker-flask-test .
#docker image ls
#docker run [-it --rm] -p 5000:5000 -d docker-flask-test

# docker container ls
# docker rm -f <container-name>

# init a base image (Alpine is small Linux distro)
# FROM python:3.7-alpine
# Use an official Python runtime as an image
FROM python:3.6

# The EXPOSE instruction indicates the ports on which a container
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist
WORKDIR /app

#COPY requirements.txt /app
COPY . /app

#apt update is needed if apt is going to be used here

# update pip to minimize dependency errors 
RUN python -m pip install --upgrade pip

#install python dependencies using pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

#COPY app.py /app
#COPY templates/ /app

# Run app.py when the container launches
# define the command to start the container with a list of executable and parameters
CMD python app.py

