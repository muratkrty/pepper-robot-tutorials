import numpy as np
from qibullet import SimulationManager as sim
from qibullet import PepperVirtual as pv
import decimal
import random
import time
import cv2

def main():
    sim_mngr = sim()  
    qi_client = sim_mngr.launchSimulation()

    nof_iters = 1000  # number random joint configuration

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

    for i in range(nof_iters):
        # generate random angles for each joint
        hyaw_rand = np.radians(float(decimal.Decimal(random.randrange(hyaw_min*100, hyaw_max*100))/100))
        hpitch_rand = np.radians(float(decimal.Decimal(random.randrange(hpitch_min, hpitch_max*100))/100))

        lshoulder_roll_rand = np.radians(float(decimal.Decimal(random.randrange(lshoulder_roll_min*100, lshoulder_roll_max*100))/100))
        lshoulder_pitch_rand = np.radians(float(decimal.Decimal(random.randrange(lshoulder_pitch_min*100, lshoulder_pitch_max*100))/100))

        lelbow_yaw_rand = np.radians(float(decimal.Decimal(random.randrange(lelbow_yaw_min*100, lelbow_yaw_max*100))/100))
        lelbow_roll_rand = np.radians(float(decimal.Decimal(random.randrange(lelbow_roll_min*100, lelbow_roll_max*100))/100))
        lwrist_yaw_rand = np.radians(float(decimal.Decimal(random.randrange(lwrist_yaw_min*100, lwrist_yaw_max*100))/100))

        # the last parameter list is percentage_speed
        pepper.setAngles(["HeadYaw", "HeadPitch"], [hyaw_rand, hpitch_rand], [0.1, 0.1])
        pepper.setAngles(["LShoulderRoll", "LShoulderPitch"], [lshoulder_roll_rand, lshoulder_pitch_rand], [0.1, 0.1])
        pepper.setAngles(["LElbowYaw", "LElbowRoll"], [lelbow_yaw_rand, lelbow_roll_rand], [0.1, 0.1])
        pepper.setAngles(["LWristYaw"], [lwrist_yaw_rand], [0.1])

        # store camera images
        tcamera = pepper.subscribeCamera(pv.ID_CAMERA_TOP)
        img = pepper.getCameraFrame(tcamera)
        print("tcamera data type: {}".format(type(img))) # numpy.ndarray
        cv2.imshow("Top camera", img)
        #cv2.imwrite("img_data/img"+str(i)+".png", img)
        cv2.waitKey(1)  
        pepper.unsubscribeCamera(tcamera)


        print("Iteration: ", i)
        
if __name__ == '__main__':
    main()
