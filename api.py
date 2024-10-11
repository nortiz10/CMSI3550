from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "Harry Potter"},
    {"id": 2, "name": "Ron Weasley"},
    {"id": 3, "name": "Hermione Granger"}
]

@app.route('/api/get_names', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/api/add-name', methods=['POST'])
def add_item():
    new_item = request.json
    data.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)
