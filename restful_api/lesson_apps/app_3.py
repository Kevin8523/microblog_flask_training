from flask import Flask, jsonify, request

app = Flask(__name__) # __name__ gives each file a unique name

# List of items with dictionaries of items
stores = [
	{
		'name': 'My Wonderful Store',
		'items': [
			{
			'name': 'My Item',
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
	request_data = request.get_json()  # >> Gets the data in JSON format
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)

# GET /store/<string:name>			>> Get a store for a given name and return some data about it
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
	# Iterate over stores
	# if the store name matches, return it
	# if none match, return an error message
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return	jsonify({'message': 'store not found'})
		

# GET /stores 						>> Return a list of all the stores
@app.route('/store') 
def get_stores():
	return jsonify({'stores': stores})

# POST /store/<string:name>/item  	>> Create an item inside a specific store with a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			stores['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item  	>> Get all the items from the store
@app.route('/store/<string:name>/item') 
def get_item_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items': store['items']})
	return jsonify({'message': 'store not found'})

app.run(port=5000) # port = area of computer where it will receive the requests

