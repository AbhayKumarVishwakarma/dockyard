from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

items = []

@app.route('/', methods=['GET'])
def get_data():
    return render_template('index.html')


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    item = request.json
    items.append(item)
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if 0 <= item_id < len(items):
        return jsonify(items[item_id])
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if 0 <= item_id < len(items):
        items[item_id] = request.json
        return jsonify(items[item_id])
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        deleted = items.pop(item_id)
        return jsonify(deleted)
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
