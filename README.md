# color_detection


######################################### DESCRIPTION #########################################

Author : Flavien CHARTON
Color detection program for RGB images

A short software that enables to find the percentage of a hue range given by
the user in a natural image and save the resulting image thresholded with the
given range.

######################################## INSTALLATION #########################################

Dependencies : python 2.X, OpenCV

In order to use this program, please install Python programming language 
(vers. 2.X) and OpenCV.

********************************** Installation of Python 2.X version (vers. 2.7.Y recommended) ********************************

On Windows: 

	- Download Python MSI Installer from the Python Downloads page
	 http://www.python.org/downloads/ (x86 for 32 bit OS preferable)
	- Double click on the MSi file
	- Follow the instructions from the installer
	- During installation, check in the command prompt if "pip" is going to 
	 be installed
	- If not installed, follow the official installation guide:
	 https://pip.pypa.io/en/stable/installing/
	- After installation completed, check the PATH environment variable
	- If not already set, add the following to your PATH (replace X):
	 C:\Python2X\;C:\Python2X\Scripts\
	 (Assuming Python 2.X is intalled in C: root) 

On Linux:

   The latest versions of CentOS, Fedora, Redhat Enterprise (RHEL) and Ubuntu come
   with Python 2.7.

	- Open a command prompt and do the following to check which version of
	 Python is installed:
	 python --version
	- For Debian and Ubuntu Linux if Python is not installed, do
	 the following (replace X):
	 apt-cache search python | egrep "^python2.[0-9]" --color
	 sudo apt-get install python2.X
	- For Red Hat/ RHEL / CentOS Linux, do the following:
	 sudo yum install python
	- Repeat the first step (check python version)
	- Open a command prompt and do the following to check if "pip" 
	 is installed:
	 command -v pip
	- If not installed, follow the official installation guide:
	 https://pip.pypa.io/en/stable/installing/

************************************************** Installation of OpenCV ******************************************************

On Windows:

	- Go to the following site and follow the instructions (OpenCV from prebuilt binaries):
	 http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html

On Linux:

   	- Go to the following site and follow the instructions:
	 http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html

#################################### RUNNING THE SCRIPT #######################################

On Windows:

   Open a command prompt and do the following (replace X):
   
	C:\Python2X\python.exe C:\<PYTHON_FILE_PATH>\color_detection.py
	
   Or do the following (only if Python is in your PATH environment variable):
   
	python.exe C:\<PYTHON_FILE_PATH>\color_detection.py

On Linux:

   Open a command prompt and do the following:
	
	chmod +x color_detection.py
	
	python color_detection.py
