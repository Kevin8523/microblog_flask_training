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

## Decorators
A decorator modifies the function that follows it. A common pattern with decorators is to use them to register functions as callbacks for certain events

## Running Flask App
1. export FLASK_APP=microblog.py
2. flask run 
	- http://localhost:5000/ 

## Jinja Templates
- Uses jinja and is called by the render_template() function
- Use templates when you have parts that are commmon across pages as the base and have other pages derived off of that

### Jinja Common functions
- extend
- endfor

## flask_wtf
- forms

### Functions
- DataRequired()

## Command prompt hotkeys
ctrl+c
- Exit from command prompt with website running
ctrl+d (mac) ctrl+z (win)
exit interpreter 


## Databases