# Scalable-Backend-Workshop
A backend workshop to be presented at DeerHacks 

Setup on Linode:

- install git
- sudo apt install python3
- apt install python3.10-venv
- apt install python3-pip
- python3 -m venv env 
- pip install flask
- you will also have to run `sudo apt-get install libgl1-mesa-glx` to have the necessary graphics drivers
- pip install wheel
- Install all dependencies at and verify that GFPGAN works: https://github.com/TencentARC/GFPGAN
- Note: on Linode you may need to install pytorch before basicsr
  - pip install torch

- install all required dependencies run `pip install -r requirements.txt`


Run backend:
- export FLASK_APP=backend
- export FLASK_ENV=development
- flask run
