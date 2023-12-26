
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

user_data_dict = {}

@app.route('/json-example', methods=['POST', 'GET'])
def json_example():
    try:

        if request.method == 'POST':
            data = request.get_json()
            user_info = list(data.values())[0]  # Получаем информацию о пользователе
            login = data.get('login')

            # Check for required data
            if login:
                user_data_dict[login] = data
                with open('kek.json', 'w') as file:
                    json.dump(user_data_dict, file)

                    print("Received data:", data)
                return jsonify({"message": "Data successfully saved!"})
            else:
                return jsonify({"error": "Missing user login"}), 400

        elif request.method == 'DEL':

            data = request.get_json() # Get JSON data from the request
            login = data.get('login')

            # Check for required data
            if login:
                if login in user_data_dict:
                    del user_data_dict[login]
                    with open('kek.json', 'w') as file:
                        json.dump(user_data_dict, file)
                    return jsonify({"message": "Data successfully deleted!"})
                else:
                    return jsonify({"error": f"User with login {login} not found"}), 404
            else:
                return jsonify({"error": "Missing user login"}), 400


        elif request.method == 'PUT':

            data = request.get_json()
            login = data.get('login')

            # Check for required data
            if login:
                if login in user_data_dict:

                    user_data_dict[login] = data
                    with open('kek.json', 'w') as file:
                        json.dump(user_data_dict, file)

                    return jsonify({"message": "Data successfully updated!"})

                else:
                    return jsonify({"error": f"User with login {login} not found"}), 404
            else:
                return jsonify({"error": "Missing user login"}), 400

        elif request.method == 'GET':

            data = request.get_json()
            with open('kek.json', 'r') as file:
                json.dump(data, file)  # Write JSON data to 'kek.json'

            return jsonify(f'{data}')

    except Exception as e:

        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
   app.run(debug = True)



