
from flask  import Flask, jsonify, request

app = Flask(__name__)

items = {1: "Ramesh"}

@app.route('/')
def home():
    return "Welcome to Flask API"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def post_items():
    i = max(items, default=0) + 1
    data = request.json
    items[i] = data['name']
    return jsonify(items), 201

@app.route('/items/<int:i>', methods=['PUT'])
def put_items(i):
    if i in items:
        data = request.json
        items[i] = data['name']
        return jsonify(items)
    return jsonify({"message": "Item not found"}), 404

@app.route('/items/<int:i>', methods=['DELETE'])
def delete_items(i):
    if i in items:
        del items[i]
        return jsonify({"message": "Item deleted"})
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
