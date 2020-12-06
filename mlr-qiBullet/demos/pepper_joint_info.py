from qibullet import SimulationManager as sim
from qibullet import PepperVirtual as pv

def print_joint_info(agent_joint_list):
   """ Display the agent's joint info:
       Joint class provides getter/setter methods
       for joint angles, velocity, and limit parameters.
       Check API documentation: https://softbankrobotics-research.github.io/qibullet/api/
       
   """
   for name, joint in agent_joint_list:
       low_lim, up_lim = joint.getLowerLimit(), joint.getUpperLimit() # in radian
       max_vel, max_effort = joint.getMaxVelocity(), joint.getMaxEffort() # in rad/s, in Nm
       print(name, low_lim, up_lim, max_vel, max_effort )

def main():
   sim_mngr = sim()
   qi_client = sim_mngr.launchSimulation(gui=True) 

   pepper = sim_mngr.spawnPepper(qi_client, spawn_ground_plane=True)

   print_joint_info(pepper.joint_dict.items())

   input("Press a key then Enter to exit: ") # otherwise simulation window fades away

if __name__ == '__main__':
   main()
