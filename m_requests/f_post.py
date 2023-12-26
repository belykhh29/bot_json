
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

user_data_dict = {}

@app.route('/json-example', methods=['POST', 'GET', 'DELETE', 'PUT'])
def json_example():
    try:

        if request.method == 'POST':

            data = request.get_json()  # Get JSON data from the request
            with open('kek.json', 'w') as file:
                json.dump(data, file)  # Write JSON data to 'kek.json'

            return jsonify({"message": "Data successfully saved!"})

        else:

            data = request.get_json()
            with open('kek.json', 'w') as file:
                json.dump(data, file)  # Write JSON data to 'kek.json'

            return jsonify(f'{data}')

    except Exception as e:

        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
   app.run(debug = True)