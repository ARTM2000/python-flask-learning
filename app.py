from flask import Flask, jsonify, request

app = Flask(__name__) # __name__ just is a unique string name
# app = Flask("some")

stores = [
    {
        "name": "My first store",
        "items": [
            {
                "name": "notebook",
                "price": 15.95
            },
            {
                "name": "notebook2",
                "price": 15.95
            }
        ]
    }
]

# post storing new documents
@app.route("/stores", methods=["POST"])
def create_store():
    req_data = request.get_json(cache=False)
    new_store = {
        "name": req_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

# get all stores
@app.route("/stores")
def get_all_stores():
    return jsonify({"data": stores, "message": "response sent"})

# get a specific store
@app.route("/stores/<string:name>", methods=["GET"]) # default method is GET
def get_store(name):
    store_found = False

    for store in stores:
        if store["name"] == name:
            store_found = True
            return jsonify({"data": store, "message": "Store found"})
    
    if not store_found:
        return jsonify({"data": [], "message": "This store does not exist"})
    

# post store item
@app.route("/stores/<string:name>/add-item", methods=["POST"])
def create_store_item(name):
    req_data = request.get_json(cache=False)
    store_found = False

    for store in stores:
        if store["name"] == name:
            store_found = True
            new_Item = {
                "name": req_data["name"],
                "price": req_data["price"]
            }

            store["items"].append(new_Item)

            return jsonify({"data": store, "message": "Store items updated"})

    if not store_found:
        return jsonify({"data": [], "message": "This store does not exist"})

# get store items
@app.route("/stores/<string:name>/items")
def get_store_items(name):
    store_found = False

    for store in stores:
        if store["name"] == name:
            store_found = True
            return jsonify({"data": store["items"], "message": "Items sent"})

    if not store_found:
        return jsonify({"data": [], "message": "This store does not exist"})
    

app.run(port=5000, debug=True)
