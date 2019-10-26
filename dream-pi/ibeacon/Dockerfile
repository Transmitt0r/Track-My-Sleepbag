FROM balenalib/raspberrypi3-python:3-stretch-run

# RUN install_packages libbluetooth-dev python-dev gcc pkg-config build-essential
# RUN install_packages  libglib2.0-dev libboost-python1.62-dev libboost-thread-dev 

# Set our working directory
#WORKDIR /usr/src/app

# Copy requirements.txt first for better cache on later pushes
#COPY requirements.txt requirements.txt

# pip install python deps from requirements.txt on the resin.io build server
#RUN pip install -r requirements.txt

# This will copy all files in our root to the working  directory in the container
#COPY . ./

# Enable udevd so that plugged dynamic hardware devices show up in our container.
#ENV UDEV=1

# main.py will run when container starts up on the device
#CMD ["python","-u","src/main.py"]