from flask import Flask

app = Flask(__name__) # __name__ gives each file a unique name

@app.route('/') # 'http://www.google.com/' >> tells app what to learn >> decorator has to act on a method
def home():
	return "Hello, world!" # has to return something



app.run(port=5000) # port = area of computer where it will receive the requests

