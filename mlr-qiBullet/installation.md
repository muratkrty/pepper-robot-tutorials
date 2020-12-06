# install-qibullet
To follow the tutorials for the seminar lecture you may need
* experience in one of GNU/Linux distributions and basic terminal commands
* experience in software development tools and libraries: OpenCV, Git, TensorFlow.
* hands-on experience with a Python
* lecture slides of the week 6

----
## A. Setting up the virtual environment
1. Follow the intsruction in [this link](https://virtualenvwrapper.readthedocs.io/en/latest/index.html) to install and configure **mkvirtualenv** in your debian-based Linux distro. Here we will use Ubuntu 18.04 LTS for running qiBullet demos.
2. Create a virtual enviornment by typing 
    ```shell
    murat@scioi::mlr-qiBullet$ mkvirtualenv -p python3 mlrDemos
    # after typing the command above your promt should change
    (mlrDemos) murat@scioi::mlr-qiBullet$ 
    ```
3. Visit [qi-Bullet github repository](https://github.com/softbankrobotics-research/qibullet) to follow see the requiments for the installations and install them while you are in the virtual enviornment.
    ```shell
    (mlrDemos) murat@scioi::mlr-qiBullet$ pip install numpy
    (mlrDemos) murat@scioi::mlr-qiBullet$ pip install pybullet
    (mlrDemos) murat@scioi::mlr-qiBullet$ pip install qibullet
    (mlrDemos) murat@scioi::mlr-qiBullet$ pip install scipy matplotlib seaborn   # multiple packages 
    (mlrDemos) murat@scioi::mlr-qiBullet$ pip install tensorflow                 # optional
    (mlrDemos) murat@scioi::mlr-qiBullet$ pip install opencv-contrib-python      # optional
    ```
Note that installing pybullet and opencv might take a couple of minutes.   
4. List the installed packages in your virtual environment by typing: pip list  
5. Download the qiBullet examples manualy from the [GitHub repository](https://github.com/softbankrobotics-research/qibullet/tree/master/examples), or alternatively, clone the whole qiBullet repository:  
5.1 Read [tldr version](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)) of the Apache Licence v2 requirements.  
         $ git clone https://github.com/softbankrobotics-research/qibullet.git
6. List the example demos in the example file changing your working directory to the location of you examples, e.g., `qiBullet/examples` if you cloned the qiBullet repository:

        $ cd qibullet/examples
        $ ls
        light_position.py    pepper_joints_error.py  README.md
        multi_simulation.py  pepper_lasers.py        robot_joint_control.py
        pepper_basic.py      pepper_shadowing.py     robot_ros_test.py
7.  Run one of the example files to test your setup. 
    ```shell
        $ python pepper_basic.py 
    ```
    You should see a pepper robot in an empty world. 
    
## Demos with the Pepper robot
To run the demos below, you must activate **mlrDemos** virtual environment by: workon mlrDemos
1. To spawn the pepper and nao robots: **python pepper_nao_spawn.py**
2. To read RGB cameras and dept sensor data: **python pepper_camera.py**
3. To list the pepper robot joint and their range: **python pepper_joint_info.py**
4. To randomly move the joints while reading top camera images: **python pepper_joint_control.py**
