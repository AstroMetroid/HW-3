## Members
### Garrett Tufts

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```
## Running Program
Adding (5, 'Cherry') to basket_a:
```
127.0.0.1:5000/api/update_basket_a
```
Separating uique fruits from both baskets
```
127.0.0.1:5000/api/unique
```
