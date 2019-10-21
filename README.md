# pepper-scripts

A repository for the pepper robot scripts.

---

**Installation procedure**
 0) Instal [ROS Kinetic](http://wiki.ros.org/kinetic/Installation), if you are using Ubuntu 16.04.  
1) Follow intruction to install in [this](http://wiki.ros.org/pepper/Tutorial_kinetic) link to install Pepper ros packages.  
2) You need to bring up the robot with all sensor and actuators by typing 
```
roscore # in a terminal, the open a new terminal

$ roslaunch pepper_bringup pepper_full_py.launch nao_ip:=192.168.26.135 roscore_ip:=192.168.26.157

```
3) Alternatively you can add the following line to your .bashrc
```
alias bringp="roslaunch pepper_bringup pepper_full_py.launch nao_ip:=192.168.26.135 roscore_ip:=192.168.26.157"

# then source your bashrc
$ source ~/.bashrc
```