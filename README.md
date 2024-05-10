# How to setup guide for Bota Systems- Force-Torque Rokubi serial using ROS

[Link](https://www.botasys.com/force-torque-sensors/rokubi) to official datasheet

## Requirements
1. ROS-Noetic or ROS2-Foxy
2. BotaSys FT sensor 

## Hardware description

- **Product**: Bota systems-BFT-ROKS-SER-M8
- **Range(Fxy, Fz, Mxy, Mz)**: (500N, 1200N, 15Nm, 12Nm)
- **Weight**: ~113g
- **Comunication**: Serial RS422/USB
- **Size(DxL)**: 42 x 32 mm 
- **Accuracy**: <2.0%
- **Sampling rate(Max)**: 800 Hz


## Setup 

### Wiring connections

Add a picture of required components of FT sensor

### Install dependencies

#### Step 1
Setup catkin_ws


#### Step 2
Install bota_driver package



#### Step 3
create new package inside catkin_ws/src

Download the ft_sensor repo for calibrated_wrench

#### Step 4
Follow the instructions provided in "Demo" section to verify the installation

### Demo
- Check `rospack list` for installed rokubimini_serial packages
- Run the following node to access the sensor data via topics
```bash
roslaunch rokubimini_ethercat rokubimini_ethercat.launch
```
- Run the custom node to calibrate the sensor 
```bash
rosrun ft_sensor ft_sensor_wrench.py
```


### Verify 
Run (for ROS-noetic)
`rostopic list` and echo the topic of interest `rostopic echo <your topic name>`
```bash
/bus0/ft_sensor0/ft_sensor_readings/reading
/bus0/ft_sensor0/ft_sensor_readings/temperature
/bus0/ft_sensor0/ft_sensor_readings/wrench
/calibrated_wrench
/diagnostics
/rosout
/rosout_agg
/statistics

```
