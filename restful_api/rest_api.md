# Running Flask
***Documentation:*** https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world : Currently on Chapter 4

## Virtual Environment
1. Always create a virtual environment (venv) when starting a flask program

### Creating Virtual Environment in Python
python -m venv venv
- 1st venv calls the venv package, and the second names it venv

### Activate Venv
source venv/bin/activate
- Activates

## Running Flask App
1. export FLASK_APP=microblog.py
2. flask run 
	- http://localhost:5000/ 

## End
- CTRL + C

## Tips
- Good practice to set configuration from environment variables, and provide a fallback value when the environment does not define the variable