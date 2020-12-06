from qibullet import SimulationManager as sim

def main():
    # SimulationManager is a class for managing events/parameters of the simulation
    # it hosts methods names as lunch|reset|stop simulation
    # it can also spawn and remove the robot in the simulation
    # https://softbankrobotics-research.github.io/qibullet/api/
    sim_mngr = sim() # create an instance of SimulationManager
    
    # Call launchSimulation() to generate simulation/physics instance
    # For the time being, we will call it with default parameters
    qibullet_client = sim_mngr.launchSimulation(gui=True) # try with gui=False


    # The X, Y, Z coordinates where the Pepper spawns
    pepper_coords = [0.0, -1.0, 0.0]

    # Spawn the Pepper robot in the simulation with given coordinates
    pepper = sim_mngr.spawnPepper(qibullet_client, translation=pepper_coords, spawn_ground_plane=True)
    
    # Spawn NAO robot in the default coordinates, [0.0, 0.0, 0.0]
    nao = sim_mngr.spawnNao(qibullet_client, spawn_ground_plane=True)

    input("Press a key then Enter to exit: ")

    
# Why is the function of if __main__
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()
