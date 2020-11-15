# Sensor readings and visualization
In this tutorial, we will first introduce the Pepper robot sensors. Then, we will describe how to read and visualize the sensory readings. To get familiar with the Pepper robot's hardware, we suggest to read the [1] and check the Figure 3 to see the location of each sensor on the robot body. 
Note that the simulated robot model in qiBullet and the actual robot have distinctions. For instance, the sonar sensors in qiBullet were not simulated, and you can not obtain images from multiple cameras at the same time. Nevertheless, designing a simulated experiment will give an idea of how the robot will behave in a real-world scenario.

The Pepper robot sensors: 
* **Cameras:**  located at the forehead and mouth of the robot to extract color images.  
* **Depth sensor:** located behind one of the robot's eyes. It provides distance information in the millimeter format.
* **Microphones:** located inside the head of the robot. They are used to localize the sound in the environment and one-to-one interaction.
* **Tactile sensors:** located the head and outer part of both hands. The tactile sensor can only provide touch or no touch information rather than haptic details (e.g., temperature, friction, mechanical property) regarding the contacted object. 
* **Bumpers:** cover the wheels of the robot, and they enable the robot to stop when it hits an obstacle.
* **Range sensors:** located at various parts of the lower body. The robot has two infrared sensors, one laser scanner, and two sonar sensors. 


## 1- Processing camera images
This tutorial shows how to access one of the robot cameras, manipulate the images and visualize the laser reading.

 - Download **urdf** file for the objects in the simulation. You can download models from either  
 [bullet3 data](https://github.com/bulletphysics/bullet3/tree/master/data) or [Gazebo models]([https://bitbucket.org/osrf/gazebo_models/src/default/](https://bitbucket.org/osrf/gazebo_models/src/default/)).

* Activate the virtual environment
```shell
$ workon qiBulletDemos
```
* Open a file named **qibullet_pepper_cameras.py** by using your favorite text editor. 
* Copy/paste the following lines into the**qibullet_pepper_cameras.py**


```python
import cv2
import pybullet as pyb 
from qibullet import SimulationManager as sim
from qibullet import PepperVirtual as pv

def main():
    # Create an instance of SimulationManager
    # Crate a physics client for the simulation
    sim_mngr = sim()  
    qi_client = sim_mngr.launchSimulation()

    # Spawn the Pepper in default position
    pepper = sim_mngr.spawnPepper(qi_client, spawn_ground_plane=True)

    # Load an object in the simulation. You can download various object from
    pyb.loadURDF("data/table/table.urdf", basePosition=[1.5, 0.0, 0.0])
    pyb.loadURDF("data/racecar/racecar.urdf", basePosition=[1.5, 0.0, 5.0])
    
    # We need to subscribe a sensor to read data. The papper robot has three cameras
    # with the id of ID_CAMERA_DEPTH, ID_CAMERA_TOP, and ID_CAMERA_BOTTOM
    # Since qiBullet allows you only subscribe to **only one** camera, we can display
    # each camera reading by subscribing and unsubcribing them
    while True:
        # Read and colorize depth data
        dcamera = pepper.subscribeCamera(pv.ID_CAMERA_DEPTH)
        img = pepper.getCameraFrame(dcamera)
        print("Depth data type: {}".format(type(img)))
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(img, alpha=0.03), cv2.COLORMAP_JET)
        cv2.imshow("Depth camera", depth_colormap)
        cv2.waitKey(1)  
        pepper.unsubscribeCamera(dcamera)

        # Read data from top camera
        tcamera = pepper.subscribeCamera(pv.ID_CAMERA_TOP)
        img = pepper.getCameraFrame(tcamera)
        print("tcamera data type: {}".format(type(img)))
        cv2.imshow("Top camera", img)
        cv2.waitKey(1)  
        pepper.unsubscribeCamera(tcamera)

        # Read data from boto camera
        bcamera= pepper.subscribeCamera(pv.ID_CAMERA_BOTTOM)
        img = pepper.getCameraFrame(bcamera)
        cv2.imshow("Bottom camera", img)
        cv2.waitKey(1)  
        pepper.unsubscribeCamera(bcamera)

if __name__ == '__main__':
    main()

```
* After executing the python code, you should see the snapshot below. 
```shell
$ python qibullet_pepper_cameras.py
```
![](https://raw.githubusercontent.com/muratkrty/pepper-robot-tutorials/master/assets/pepperCameras.png)

## References
[1] Pandey, A. K., & Gelin, R. (2018). A mass-produced sociable humanoid robot: pepper: the first machine of its kind. IEEE Robotics & Automation Magazine, 25(3), 40-48.
