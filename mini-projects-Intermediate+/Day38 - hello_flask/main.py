from flask import Flask, request, jsonify

app = Flask(__name__)

fake_db = {}


@app.route("/username/<name>")
def greet(name: str):
    return f"Hello {name}"


# GET - Read item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = fake_db.get(item_id)
    if item:
        return jsonify({"item_id": item_id, "value": item})
    else:
        return jsonify({"error": "Item not found"}), 404


# POST - Create item
@app.route('/items/<int:item_id>', methods=['POST'])
def create_item(item_id):

    value = request.json.get('value')
    fake_db[item_id] = value
    return jsonify({"message": "Item created", "item_id": item_id, "value": value}), 201


# PUT - Update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in fake_db:
        return jsonify({"error": "Item not found"}), 404
    new_value = request.json.get('value')
    fake_db[item_id] = new_value
    return jsonify({"message": "Item updated", "item_id": item_id, "new_value": new_value})


# DELETE - Delete item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in fake_db:
        del fake_db[item_id]
        return jsonify({"message": "Item deleted", "item_id": item_id})
    else:
        return jsonify({"error": "Item not found"}), 404
@app.route("/")
def home():
    1 / 0  # Intentional error
    return "Hello"
if __name__ == '__main__':
    app.run(debug=True)

# curl http://127.0.0.1:5000/items/1
# curl -X POST -H "Content-Type: application/json" -d '{"value":"Banana"}' http://127.0.0.1:5000/items/1
# curl -X PUT -H "Content-Type: application/json" -d '{"value":"Updated Banana"}' http://127.0.0.1:5000/items/1
