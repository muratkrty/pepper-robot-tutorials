# Pepper robot joints
This tutorial shows how to control robot joints with qiBullet. The first part of the tutorial presents the Peppers's joint information. The second part introduces how to control the Pepper robot joints.



## Robot joint information
 1. As always, you should activate the virtual environment. 
```shell
$ workon qiBulletDemos
```
 2. Create a python file as **qibullet_joint_info.py**
 3. Copy/paste below script into **qibullet_joint_info.py**
 ```python
from qibullet import SimulationManager as sim
from qibullet import PepperVirtual as pv

def print_joint_info(agent_joint_list):
    """ Display the agent's joint info:
        Joint class provides getter/setter methods
        for joint angles, velocity, and limit parameters.
    """
    for name, joint in agent_joint_list:
        low_lim, up_lim = joint.getLowerLimit(), joint.getUpperLimit() # in radian
        max_vel, max_effort = joint.getMaxVelocity(), joint.getMaxEffort() # in rad/s, in Nm
        print(name, low_lim, up_lim, max_vel, max_effort )

def main():
    sim_mngr = sim()
    # Disable the gui
    qi_client = sim_mngr.launchSimulation(gui=False) 

    pepper = sim_mngr.spawnPepper(qi_client, spawn_ground_plane=True)

    print_joint_info(pepper.joint_dict.items())

if __name__ == '__main__':
    main()
 ```

 4. If you run the script you will get output similar to the below lines.
```
pybullet build time: Mar 17 2020 17:43:49
('LWristYaw', -1.82387, 1.82387, 17.3835, 0.2014)
('HipRoll', -0.514872, 0.514872, 2.27032, 10.1884)
('RWristYaw', -1.82387, 1.82387, 17.3835, 0.2014)
('HeadYaw', -2.08567, 2.08567, 7.33998, 5.428)
......
```
## Robot joint control
This demo shows how set the robot head and left arm's joint to randomly generated configuration. Note that the robot head has no roll axis. The list of joint and their range can be found in [Softbank documentation](http://doc.aldebaran.com/2-5/family/pepper_technical/joints_pep.html).


 1. As always, you should activate the virtual environment. 
```shell
$ workon qiBulletDemos
```
 2. Create a python file as **peper_joint_control.py**
 3. Copy/paste below script into **peper_joint_control.py**
``` python
import numpy as np
from qibullet import SimulationManager as sim
from qibullet import PepperVirtual as pv
import decimal
import random
import time

def main():
    sim_mngr = sim()  
    qi_client = sim_mngr.launchSimulation()

    nof_iters = 100  # number random joint configuration
    # Spawn the Pepper in default position
    pepper = sim_mngr.spawnPepper(qi_client, spawn_ground_plane=True)

    # joint limits in degress
    hyaw_min, hyaw_max = -119.0, 119.0
    hpitch_min, hpitch_max = -40.0, 36.0
    lelbow_yaw_min, lelbow_yaw_max = -119.0, 119.0
    lelbow_roll_min, lelbow_roll_max =-89.0, -0.5
    lshoulder_pitch_min, lshoulder_pitch_max = -119.0, 119.0
    lshoulder_roll_min, lshoulder_roll_max = 0.5, 89.5
    lwrist_yaw_min, lwrist_yaw_max = -104.0, 104.0

    for _ in range(nof_iters):
        # generate random angles for each joint
        hyaw_rand = np.radians(float(decimal.Decimal(random.randrange(hyaw_min*100, hyaw_max*100))/100))
        hpitch_rand = np.radians(float(decimal.Decimal(random.randrange(hpitch_min, hpitch_max*100))/100))

        lshoulder_roll_rand = np.radians(float(decimal.Decimal(random.randrange(lshoulder_roll_min*100, lshoulder_roll_max*100))/100))
        lshoulder_pitch_rand = np.radians(float(decimal.Decimal(random.randrange(lshoulder_pitch_min*100, lshoulder_pitch_max*100))/100))

        lelbow_yaw_rand = np.radians(float(decimal.Decimal(random.randrange(lelbow_yaw_min*100, lelbow_yaw_max*100))/100))
        lelbow_roll_rand =  np.radians(float(decimal.Decimal(random.randrange(lelbow_roll_min*100, lelbow_roll_max*100))/100))
        lwrist_yaw_rand =  np.radians(float(decimal.Decimal(random.randrange(lwrist_yaw_min*100, lwrist_yaw_max*100))/100))

        # the last parameter list is percentage_speed
        pepper.setAngles(["HeadYaw", "HeadPitch"], [hyaw_rand, hpitch_rand], [0.1, 0.1])
        pepper.setAngles(["LShoulderRoll", "LShoulderPitch"], [lshoulder_roll_rand, lshoulder_pitch_rand], [0.1, 0.1])
        pepper.setAngles(["LElbowYaw", "LElbowRoll"], [lelbow_yaw_rand, lelbow_roll_rand], [0.1, 0.1])
        pepper.setAngles(["LWristYaw"], [lwrist_yaw_rand], [0.1])
        #pepper.setAngles("LWristYaw", lwrist_yaw_rand, 0.1) # yields error. open an issue in qiBullet github account 

if __name__ == '__main__':
    main()
```
4. After executing the python code, you should see the video in this [link]([https://github.com/muratkrty/pepper-robot-tutorials/blob/master/assets/head_larm.ogv](https://github.com/muratkrty/pepper-robot-tutorials/blob/master/assets/head_larm.ogv))
```shell
$ python peper_joint_control.py
```


