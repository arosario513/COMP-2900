# Jupyter Setup
Jupyter is a module for python in which you can write code and view data on a webpage
## Prerequisites
- First, you got to make sure Python is installed
- Type the following inside a terminal:
```
python --version
```
If it shows you the version, then you have Python set up properly, if not, make sure to fix any problems beforehand
## Making a virtual environment
It's good practice to setup a virtual environment for your project to isolate it, and avoid conflicts
- Create a folder and cd into it 
```
mkdir ExampleProject
cd ExampleProject
```
- Inside the folder, run this command:
```
python -m venv venv
```
This will create the virtual environment
To use it, you have to run the activate command, which is different for each OS 

### Windows
```
venv\Scripts\activate.bat
```
### Linux/Mac
```
source venv/bin/activate
```
Now you should be inside the virtual environment
It should look something like this:
```
(venv) C:\Users\alberto\ExampleProject>
```
or 
```
(venv) alberto@debian$
```
### Getting out of venv
To exit the virtual environment just type:
```
deactivate
```
## Installing the module
To install the module you simply run this command:

### For Jupyter Notebook
```
pip install notebook
```
### For Jupyter Lab
```
pip install jupyterlab
```
## Running Jupyter
Run the command for the version you installed:
```
jupyter notebook
```
or
```
jupyter lab
```
It should open the browser with the Jupyter homepage
## Issues
If there's any issues, be sure to check out Jupyter's [website](https://jupyter.org/)
