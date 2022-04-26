# Launch File Explanations

## multi_range.launch 

This launch file will set up a boolean-value object detection in 4 ranges within a 90 degree cone in front of the RPLIDAR. You can set the r_value (in meters) to determine how far away you want the robot to stay away from an obstacle (default .5 m).

## test.launch

This is the launch file which will lead to one method of autonomy, will write more later.
<img src="https://lh3.googleusercontent.com/a39E6MGDDaimv_Fx4XfZ_qbYNEcGiLca6w7pcx3Dr-USbVf5Vh3hL951iIkta5L3O5kAdDmFdpzH_cfpJoV2ES0bYfcm6BWSdSNhpCR2JGMEVU13XFk4tpN74zg2FL-gBaRrsY6BswrFVudVg2dYngaGcbSK0Hebh1QcXC6USpEhr_AnYjXNueuIREnEntXnKgTtLeYM0la_6lB6cmfoCgK8vOAGgy0e3pCxbXAN0Fnn8n_0xH2SBCvXY2RB5H6L_IkU4tjDRYoAHgWKm6-JcECat1kIHltguyBSlKYncEMX63hEjb6yiF4y1bOTiQ1z937LtCbob18L-Koq8bPjeKsUjcarjbGXyLFso_Si7ppOZaBLJc-Ui9AUrfLL-ZyaZ_D91Wl8mX1cEKyu-PCtwow-T3QTVqXkoCbULhodtKh-8Pd3Z8lRat7z4BDSGaxH06tI_z0HP2iMjFGUbjJpNqUdwTx9M2KvHAfTk6fPWEFreJ_v9-rR-KQf_xJhWLr_rEEUN_hmAKolDoTySuq8ONyZrIiyMEHzpG0UiyDKL55w1GWUWd8GmxXlfl4H90cNjOYuus_k16vLI85kVwkvo6DuP3tHoAAnYBPSW71RiLxdNmIYBSgAyn90n-kFeT9vZD75KfJYC6N_ipg9DyGFIn_5mCzPrgvJdKgIgzTp_efp4BqGsSAkfHU870YbvjdNat2A5y01o2ZMZ1hsnC99Zhi4-g=w818-h786-no?authuser=0" width=410, height=394/>
<img src="https://lh3.googleusercontent.com/AD9j4HJrWLqfbWlCdmkDjDGa8BY6ZEVVDf_K3KVz7J4j7-NONBi87nR54AGy8Oq29UAVlQuyBFnFmDxH5701AGYQ9aDY3iNtDNUO9Ys6L3JeW6X4WGGr4YIrsGsfkzmdNNfg7OcJJ5xOy2YPNLCqkfVy-aiIAxfds9OphfF0m2X-uA3kc3Ac8WNl7w3hq76MJMNK8Pm1Bi60N3W8cZpdlCGdqIHBaVrIMCwvGbswKS21YI8LzyuXUgQXHt37p3LGnQOXRVLdu225kOUts7GzDFxLUq4Q_kUwnSEOcWIsUWaCvZ9s1bWWq6eHrEvwgvfG8GcG2glzGoA8xvPIJ-3I64x8frfE7dZVcYk2brA1wq4ZOuXPYAi6rhY0lRfHnIu9L5fLPRthkvnHLKx_2R5dXW609kJv_aMV6mkIKNJZuB_rL-w0nLsuwsrbEAAce6jdYNDgQXtNVtDqOtZZL2AbP_f-Lv2bgCTmSPQl2Ydne9E_XD3qX0fbkiM9GM3AOw_QtPUtj0YwHOBVntBsNG9bbxORr65nIyRJxnkplHuK3FDaN3b9BmHpvxKeuGGm1uEgb27f0LyWiC4gk9o1-MXxA-ghXfAfjkNV7cLd3iKmlUef0xj2qHmACIopD39CuaAKqJY9PsCc9R61D0GpMJJNR4t5mj8Aq7ZLAFXGS4LIkJqApQofBImZKo_q_JgP8hn2mELPimXePbkk_8uf4BgESVvQjg=w916-h585-no?authuser=0" width=500, height=300/>

# Setup and Launch
```
# Make sure the RPLIDAR is connected
ls -l /dev | grep ttyUSB0

# Set permissions for the RPLIDAR
sudo chmod 666 /dev/ttyUSB0

# catkin_make and launch
cd catkin_ws
catkin_make
roslaunch rplidar_ros rplidar.launch
roslaunch check_obstacle {multi_range/detector}.launch
```

# Installation
## With prior install of rplidar_ros
```
cd catkin_ws/src
sudo git clone https://github.com/oliverburrus/obstacle_detector.git
```
## Without prior install of rplidar_ros
```
# Install dependencies.
sudo apt-get update
sudo apt-get install cmake python-catkin-pkg python-empy python-nose python-setuptools libgtest-dev python-rosinstall python-rosinstall-generator python-wstool build-essential git

cd ~/catkin_ws/

gedit ~/.bashrc
#Add the following at the END of the .bashrc file

source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash

# Save and close

source ~/catkin_ws/devel/setup.bash
cd src
sudo git clone https://github.com/Slamtec/rplidar_ros.git
sudo git clone https://github.com/oliverburrus/obstacle_detector.git
```

