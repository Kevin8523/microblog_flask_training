from flask import Flask

app = Flask(__name__) # __name__ gives each file a unique name

# List of items with dictionaries of items
stores = [
	{
		'name': 'My Wonderful Store',
		'items': [
			{
			'name': 'My Item'
			'price': 15.99
			}
		]
	}
]

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}			>> Create a store with a given name
@app.route('/store', methods=['POST'])
def create_store():
	pass

# GET /store/<string:name>			>> Get a store for a given name and return some data about it
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
	pass

# GET /stores 						>> Return a list of all the stores
@app.route('/store') 
def get_stores():
	pass

# POST /store/<string:name>/item  	>> Create an item inside a specific store with a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	pass

# GET /store/<string:name>/item  	>> Get all the items from the store
@app.route('/store/<string:name>/item') 
def get_item_in_store(name):
	pass

app.run(port=5000) # port = area of computer where it will receive the requests

