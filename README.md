# Gophercises Python Solutions

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Concepts I Learnt](#concepts_learnt)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Gophercises Python Solutions is a repository of my Python solutions to coding challenges that can be found on Chris Calhoun's [Gophercises](gophercises.org) website. The solutions to Gophercises are written in [Go](golang.com) so I decided to solve the problems by myself using Python as  [Python](python.org) is my primary language.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.  

### Prerequisites

-Python3  
-SQLite

### Installing

A step by step series of examples that tell you how to get a development env running.

### Windows 10 Users

Please install and set up the following packages first. Ugrade if you find the package already installed:  
* Download [Python 3](https://www.python.org/downloads/). It is advisable to install the package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed. 
   
    Python 3 and above is needed to sucessfully run these programs.

  ```sh
  python -V
  ```  
  
* Download [pip](https://pip.pypa.io/en/latest/installing) and follow the instructions in the link as an installation guide. [Pip](https://pip.pypa.io/en/latest/installing) is the package manager for Python.

* [SQLite3](https://sqlitebrowser.org/) (Ensure it is installed).

* It is advisable to install Django in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this virtual environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:

  ```sh
  py -m pip install virtualenvwrapper-win 
  ```
  
* Create a new virtual environment.  
   
   **N/B**: The angle brackets **< >** should be ignored when typing your environment name.

  ```sh
  mkvirtualenv <envname>
  ```
    

* Change your directory to the directory of the virtual environment.

* Activate the virtual environment with:

  ```sh
  <envname>\Scripts\activate
  ```

* Deactivate the virtual environment with:

  ```sh
  deactivate
  ```

## Concepts I have learnt so far  <a name="concepts_learnt" ></a>  
These are a list of concepts I learnt while trying to solve the coding challenges.
- Threading.  
- Time module in Python.
- Database normalization.
