[[_TOC_]]

# qiBullet installation guide

This document presents a walk-through installation and tutorials to introduce the qiBullet simulation environment. Note that these tutorials require fulfilling the below items, though not necessarily all of them.

* experience in one of GNU/Linux distributions and basic terminal commands 
* experience in software development tools and libraries:  OpenCV, Git, TensorFlow.
* hands-on experience with a Python

## Known Issues
* **Windows:** On Windows we are using **Python >= 3.5**. On Python 2.7 the installation of the package `pybullet` is not straight forward because of the outdated C++-compiler version used by Python 2.7 by default. More Information on C++ compiler Versions in python on Windows: https://wiki.python.org/moin/WindowsCompilers

* **Windows:** While installing `pyBullet` on Windows the following warning might appear. It seems to be harmless and can be ignored. It was observed to happen with **python >= 3.8**.

        WARNING: Subprocess output does not appear to be encoded as cp1252

* older versions of pip might make problems. You might need to update your `pip` version and install `wheel`. For this you can use this line

        pip install --upgrade pip setuptools wheel 

## 0. OpenCV
OpenCV is not strictly necessary, but recommended for working with image processing in qiBullet. You can use the following command to install the opencv package

        pip install opencv-python

you also might want to install additional modules

        pip install opencv-contrib-python

More information can be found here: https://pypi.org/project/opencv-python/


## A. Setting up the virtual environment
In this tutorial we are using a virtual environment for our experiments in order to avoid conflicts of python packages with other experiments. This step is not strictly necessary, but advisable.

1. Open a terminal and type the commands below to install the software for creating an isolated python environment for the qiBullet demos. These may or may not work without sudo -H.

        $ sudo pip install  virtualenv  
        $ sudo -H pip install virtualenvwrapper

2. Open your ~/.bashrc then paste the below lines and save (Follow this [link](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) for more information).

        export WORKON_HOME=$HOME/.virtualenvs
        export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
        source /usr/local/bin/virtualenvwrapper.sh

3. Source your .bashrc by typing:

        $ source ~/.bashrc

4. Create a virtual environment named qiBulletDemos

        $ mkvirtualenv -p python2.7 qiBulletDemos

    **NOTE: on Windows use Python >= 3.5**	

5. Type workon to see your **qiBulletDemos** was created

        $ workon 
        p3robotenv
        qiBulletDemos # this is the environment that you are looking for!

6. Type below command to activate your virtual environment. Your terminal prompt should change.

        $ workon qiBulletDemos
        (qiBulletDemos) murat@scioi::~$ 

From now on, you can install any python libraries with the version number that you need for your application. Any installation in this virtual environment will not affect anything outside.  

7. With the following command you can deactivate your virtual environment. The prompt should change back.

        (qiBulletDemos) murat@scioi::~$ deactivate
        murat@scioi::~$ 

Now, your virtual environment is ready to install qiBullet.

## B. Install qiBullet
1. Activate the virtual environment that we created in the previous step.

        $ workon qiBulletDemos
        (qiBulletDemos) murat@scioi::~$ 

**NOTE:** all following steps will be executed in this virtual environment.

2. Install necessary Python packages. To run qiBullet demos and data visualization, you need to install the following packages.

        $ pip install numpy
        $ pip install scipy 
        $ pip install matplotlib  
        $ pip install seaborn
        $ pip install scikit-learn  
        $ pip install pybullet

    **NOTE:** installing `pybullet` might take a couple minutes. The code is being compiled in the background.

3. You can check whether the packages were correctly installed by listing them:

        $ pip list
 

4. Install qiBullet.

        $ pip install qibullet 
	
5. Run below lines to verify your installation.

        (qiBulletDemos) murat@scioi::~$ python
        Python 2.7.12 (default, Oct  8 2019, 14:14:10) 
        [GCC 5.4.0 20160609] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import qibullet
        pybullet build time: Mar 17 2020 17:43:49
        >>> 
	
## C. first steps with qiBullet

**NOTE:** a detailed tutorial on how to work with the qiBullet can be found here:  
https://github.com/softbankrobotics-research/qibullet/wiki/Tutorials:-Virtual-Robot

1. Download the qiBullet examples manualy from the [GitHub repository](https://github.com/softbankrobotics-research/qibullet/tree/master/examples), or alternatively, clone the whole qiBullet repository:  

         $ git clone https://github.com/softbankrobotics-research/qibullet.git

 2. Change your working directory to the location of you examples, e.g., `qiBullet/examples` if you cloned the qiBullet repository:

        $ cd qibullet/examples
        $ ls
        light_position.py    pepper_joints_error.py  README.md
        multi_simulation.py  pepper_lasers.py        robot_joint_control.py
        pepper_basic.py      pepper_shadowing.py     robot_ros_test.py

 3. Run one of the example files to test your setup. 

        $ python pepper_basic.py 
 
 4. You should be seeing the below simulation environment  [snapshot](https://github.com/muratkrty/pepper-robot-tutorials/blob/master/assets/qiBullet1.png). Now you can play with the repository to run different example files.  

![](https://raw.githubusercontent.com/muratkrty/pepper-robot-tutorials/master/assets/qiBullet1.png) 