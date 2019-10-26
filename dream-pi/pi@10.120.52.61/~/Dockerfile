FROM balenalib/raspberrypi3-node:12-stretch-run

COPY apt.list ./
# Install requirements
RUN apt-get update -y && apt-get dist-upgrade -y && apt-get upgrade -y && \
    apt-get install -y $(cat apt.list | tr '\n' ' ') && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Defines our working directory in container
WORKDIR /usr/src/app

# Copies the package.json first for better cache on later pushes
COPY package.json package.json

# This install npm dependencies on the balena build server,
# making sure to clean up the artifacts it creates in order to reduce the image size.
RUN JOBS=MAX npm install --production --unsafe-perm && npm cache verify && rm -rf /tmp/*

# This will copy all files in our root to the working  directory in the container
COPY . ./

# Enable udevd so that plugged dynamic hardware devices show up in our container.
ENV UDEV=1

# main.py will run when container starts up on the device
CMD ["npm", "start"]
#CMD ["./ibeacon.sh"]
#RUN ["chmod", "+x", "ibeacon.sh"]
#RUN ./ibeacon.sh