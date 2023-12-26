
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

# user_data_dict = {}

try:
    with open('kek.json', 'r') as file:
        user_data_dict = json.load(file)
except FileNotFoundError:
    user_data_dict = {}
except json.decoder.JSONDecodeError:
    user_data_dict = {}


@app.route('/json-example', methods=['POST', 'GET', 'PUT', 'DEL', 'DELETE'])
def json_example():
    try:

        if request.method == 'POST':
            try:
                data = request.get_json()
                login = list(data.keys())[0]  # Get the first key in the dictionary

                if login:
                    user_data_dict[login] = data[login]
                    with open('kek.json', 'w') as file:
                        json.dump(user_data_dict, file)

                    print("Received data:", data)
                    return jsonify({"message": f"Data for user {login} successfully saved!"})
                else:
                    return jsonify({"error": "Missing user login"}), 400

            except Exception as e:
                return jsonify({"error": str(e)}), 500
        # elif request.method == 'DEL':
        #
        #     data = request.get_json() # Get JSON data from the request
        #     login = data.get('login')
        #
        #     # Check for required data
        #     # if login:
        #     if login in user_data_dict:
        #         del user_data_dict[login]
        #         with open('kek.json', 'w') as file:
        #             json.dump(user_data_dict, file)
        #         return jsonify({"message": "Data successfully deleted!"})
        #     else:
        #         return jsonify({"error": f"User with login {login} not found"}), 404
        #     # else:
        #     #     return jsonify({"error": "Missing user login"}), 400

        elif request.method == 'DELETE':
            try:
                login = request.args.get('login')

                if login:
                    # Check if the login exists in user_data_dict
                    if login in user_data_dict:
                        del user_data_dict[login]
                        with open('kek.json', 'w') as file:
                            json.dump(user_data_dict, file)
                        return jsonify({"message": "Data successfully deleted!"})
                    else:
                        return jsonify({"error": f"User with login {login} not found"}), 404
                else:
                    return jsonify({"error": "Missing login parameter"}), 400

            except Exception as e:
                return jsonify({"error": str(e)}), 500

        elif request.method == 'PUT':

            data = request.get_json()
            login = data.get('login')

            # Check for required data
            # if login:
            if login in user_data_dict:

                user_data_dict[login] = data
                with open('kek.json', 'w') as file:
                    json.dump(user_data_dict, file)

                return jsonify({"message": "Data successfully updated!"})

            else:
                return jsonify({"error": f"User with login {login} not found"}), 404
            # else:
            #     return jsonify({"error": "Missing user login"}), 400

        elif request.method == 'GET':
            login = request.args.get('login')

            if login:
                # Check if the login exists in user_data_dict and format the response
                if login in user_data_dict:
                    user_info = user_data_dict[login]
                    formatted_user_data = {
                        'first_name': user_info.get('first_name'),
                        'last_name': user_info.get('last_name'),
                        'country': user_info.get('country'),
                        'city': user_info.get('city'),
                        'address': user_info.get('address'),
                        'post_code': user_info.get('post_code'),
                        'email_address': user_info.get('email_address'),
                        'phone_number': user_info.get('phone_number')
                    }
                    return jsonify(formatted_user_data)
                else:
                    return jsonify({"error": f"User with login {login} not found"}), 404
            else:
                return jsonify({"error": "Missing login parameter"}), 400

    except Exception as e:

        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
   app.run(debug = True)



