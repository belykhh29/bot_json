#TESTING CODE

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_user_data():
    try:
        with open('kek.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError:
        return {}

def save_user_data(user_data):
    with open('kek.json', 'w') as file:
        json.dump(user_data, file)

user_data_dict = load_user_data()  # Загрузить данные из файла при запуске приложения

@app.route('/check-login', methods=['POST'])
def check_login():
    try:
        data = request.get_json()
        login = data.get('login')

        if login in user_data_dict:
            return jsonify({"exists": True, "user_data": user_data_dict[login]})
        else:
            return jsonify({"exists": False})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/json-example', methods=['POST', 'GET', 'PUT', 'DELETE'])
def json_example():
    try:
        global user_data_dict  # Используем глобальную переменную для хранения данных

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
            login = request.args.get('login') or request.view_args.get('login')

            if login:
                # Check if the login exists in user_data_dict and format the response
                if login in user_data_dict:
                    user_info = user_data_dict[login]
                    formatted_user_data = {
                        user_info.get('login'): {
                            'first_name': user_info.get('first_name'),
                            'last_name': user_info.get('last_name'),
                            'country': user_info.get('country'),
                            'city': user_info.get('city'),
                            'address': user_info.get('address'),
                            'post_code': user_info.get('post_code'),
                            'email_address': user_info.get('email_address'),
                            'phone_number': user_info.get('phone_number'),
                            'password': user_info.get('password')
                        }}
                    return jsonify(formatted_user_data)
                else:
                    return jsonify({"error": f"User with login {login} not found"}), 404
            else:
                return jsonify({"error": "Missing login parameter"}), 400

    except Exception as e:

        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
   app.run(debug = True)



#PREVIOUS CODE
# import json
# from flask import Flask, request, jsonify
# app = Flask(__name__)
#
# user_data_dict = {}
#
# @app.route('/json-example', methods=['POST', 'GET', 'DELETE', 'PUT'])
# def json_example():
#     try:
#
#         if request.method == 'POST':
#
#             data = request.get_json()  # Get JSON data from the request
#             with open('kek.json', 'w') as file:
#                 json.dump(data, file)  # Write JSON data to 'kek.json'
#
#             return jsonify({"message": "Data successfully saved!"})
#
#         else:
#
#             data = request.get_json()
#             with open('kek.json', 'w') as file:
#                 json.dump(data, file)  # Write JSON data to 'kek.json'
#
#             return jsonify(f'{data}')
#
#     except Exception as e:
#
#         return jsonify({"error": str(e)}), 500
#
#
# if __name__ == '__main__':
#    app.run(debug = True)