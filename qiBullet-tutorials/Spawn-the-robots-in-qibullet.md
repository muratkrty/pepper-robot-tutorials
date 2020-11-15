# Spawn the robots in qiBullet
This tutorial will describe how to spawn the Pepper and Nao robot in the same simulation. To run the demo, you should install qiBullet by following the installation guide in this [link](https://scm.cms.hu-berlin.de/adapt/robot-programming-intro/-/wikis/qiBullet-installation). 

* Activate the virtual environment
```shell
$ workon qiBulletDemos
```
* Open a file named **qibullet_robot_spawn.py** by using your favorite text editor. 
* Copy/paste the following lines into the**qibullet_robot_spawn.py**

```python
from qibullet import SimulationManager as sim

def main():
    # SimulationManager is a class for managing events/parameters of the simulation
    # it hosts methods names as lunch|reset|stop simulation
    # it can also spawn and remove the robot in the simulation
    sim_mngr = sim() # create an instance of SimulationManager
    
    # Call launchSimulation() to generate simulation/physics instance
    # For the time being, we will call it with default parameters
    qibullet_client = sim_mngr.launchSimulation()
    
    # The X, Y, Z coordinates where the Pepper spawns
    pepper_coords = [0.0, -1.0, 0.0]

    # Spawn the Pepper robot in the simulation with given coordinates
    pepper = sim_mngr.spawnPepper(qibullet_client, translation= pepper_coords ,spawn_ground_plane=True)
    
    # Spawn NAo robot in the default coordinates, [0.0, 0.0, 0.0]
    nao = sim_mngr.spawnNao(qibullet_client, spawn_ground_plane=True)


    input("Press a key then Enter to exit: ")
    
if __name__ == '__main__':
    main()

```

* After executing the python code, you should see the snapshot below. 
```shell
$ python qibullet_robot_spawn.py
```

![](https://raw.githubusercontent.com/muratkrty/pepper-robot-tutorials/master/assets/spawnRobots.png) 


