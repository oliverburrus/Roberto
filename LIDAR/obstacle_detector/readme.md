SETUP:
```
# Make sure the RPLIDAR is connected
ls -l /dev | grep ttyUSB0

# Set permissions for the RPLIDAR
sudo chmod 666 /dev/ttyUSB0
```

INSTALLATION (only needed once):
```
# Install dependcies.
sudo apt-get update
sudo apt-get install cmake python-catkin-pkg python-empy python-nose python-setuptools libgtest-dev python-rosinstall python-rosinstall-generator python-wstool build-essential git

cd ~/catkin_ws/

gedit ~/.bashrc
#Add the following at the END of the .bashrc file

source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash

#Save and close

source ~/catkin_ws/devel/setup.bash
cd src
sudo git clone https://github.com/Slamtec/rplidar_ros.git
```
