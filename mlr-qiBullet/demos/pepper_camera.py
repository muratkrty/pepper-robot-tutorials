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
    # URDF- Unified Robot Description Format: http://wiki.ros.org/urdf/Tutorials
    pyb.loadURDF("data/table/table.urdf", basePosition=[1.5, 0.0, 0.0])
    pyb.loadURDF("data/racecar/racecar.urdf", basePosition=[1.5, 0.0, 5.0])
    
    # We need to subscribe a sensor to read data. The papper robot has three cameras
    # with the id of ID_CAMERA_DEPTH, ID_CAMERA_TOP, and ID_CAMERA_BOTTOM
    # Since qiBullet allows you only subscribe to **only one** camera, we can display
    # each camera reading by subscribing and unsubcribing them. Check the github repo
    # they might fixed with the new relase
    while True:
        # Read and colorize depth data
        dcamera = pepper.subscribeCamera(pv.ID_CAMERA_DEPTH)
        img = pepper.getCameraFrame(dcamera)
        print("Depth data type: {}".format(type(img))) # numpy.ndarray
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(img, alpha=0.03), cv2.COLORMAP_JET)
        cv2.imshow("Depth camera", depth_colormap)
        cv2.waitKey(1)  
        pepper.unsubscribeCamera(dcamera)

        # Read data from top camera
        tcamera = pepper.subscribeCamera(pv.ID_CAMERA_TOP)
        img = pepper.getCameraFrame(tcamera)
        print("tcamera data type: {}".format(type(img))) # numpy.ndarray
        cv2.imshow("Top camera", img)
        cv2.waitKey(1)  
        pepper.unsubscribeCamera(tcamera)

        # Read data from bottom camera
        bcamera= pepper.subscribeCamera(pv.ID_CAMERA_BOTTOM) # numpy.ndarray
        img = pepper.getCameraFrame(bcamera)
        cv2.imshow("Bottom camera", img)
        cv2.waitKey(1)  
        pepper.unsubscribeCamera(bcamera)

if __name__ == '__main__':
    main()
