import json
# import
user_data_dict = {}

try:
    with open('../../user_data.json', 'r') as file:
        user_data_dict = json.load(file)
except FileNotFoundError:
    user_data_dict = {}
except json.decoder.JSONDecodeError:
    user_data_dict = {}

def format_user_data1(user_data):
    try:

        if isinstance(user_data_dict, dict) and user_data_dict:

            login = user_data['login']

            data = (f'\n\n'
                    f'Login: {login}\n\n'
                    f'1. First Name: {user_data["first_name"]}\n'
                    f'2. Last Name: {user_data["last_name"]}\n'
                    f'3. Country: {user_data["country"]}\n'
                    f'4. City: {user_data["city"]}\n'
                    f'5. Address: {user_data["address"]}\n'
                    f'6. Post Code: {user_data["post_code"]}\n'
                    f'7. Email: {user_data["email_address"]}\n'
                    f'8. Phone Number: {user_data["phone_number"]}')

            # bot.send_message(message.chat.id, f'If you want to continue working on the database, write /start again')
            return data

        else:
            return "User data not found or invalid."

    except Exception as e:
        return f"Error formatting user data: {e}"

def format_update_data1(user_data):
    try:

        if isinstance(user_data_dict, dict) and user_data_dict:

            login = user_data['login']

            data = (f'Here\'s your new data:\n'
                    f'1. Login: {login}\n'
                    f'2. First Name: {user_data["first_name"]}\n'
                    f'3. Last Name: {user_data["last_name"]}\n'
                    f'4. Country: {user_data["country"]}\n'
                    f'5. City: {user_data["city"]}\n'
                    f'6. Address: {user_data["address"]}\n'
                    f'7. Post Code: {user_data["post_code"]}\n'
                    f'8. Email: {user_data["email_address"]}\n'
                    f'9. Phone Number: {user_data["phone_number"]}')

            return data
        else:
            return "User data not found or invalid."

    except Exception as e:
        return f"Error formatting user data: {e}"
