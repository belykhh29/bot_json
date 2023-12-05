import telebot
import json

from bot_json_test import choice_log_postget, bot
from json_data import user_data_dict, format_user_data

bot = telebot.TeleBot('6370996369:AAEqn8epM8aKiMM9zzAEHYSjOkz0K_PU5nE')



def new_or_id_update1(message):
    choice_user = message.text.lower()
    try:
        if choice_user == 'take my id as a login':
            # username = message.from_user.username
            # login = username
            agree_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            agree_button = telebot.types.KeyboardButton(r'✅')

            agree_markup.row(agree_button)

            bot.send_message(message.chat.id, f'Please, press the button for get permission to take your Telegram '
                                              f'username as a login in our base:', reply_markup=agree_markup)
            bot.register_next_step_handler(message, update_info)


        elif choice_user == 'write a users login':

            bot.send_message(message.chat.id, 'Okay! Then write a login for get and update a data from our base')
            bot.register_next_step_handler(message, update_info)

        else:

            bot.send_message(message.chat.id, 'ERROR: Invalid choice')
            bot.send_message(message.chat.id, 'Please, choose the option again')
            bot.register_next_step_handler(message, new_or_id_update1)

    except Exception as e:
        return f"Error: {e}"

def update_info(message):
    try:

        login = message.text

        if login in user_data_dict:

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

            bot.send_message(message.chat.id, f"\n{format_data}")
            bot.send_message(message.chat.id,
                             f'If you want to change info in this base, write the number of stroke')

            bot.register_next_step_handler(message, number_update_stroke, login=login)

        elif login == r"✅":

            username = message.from_user.username
            login = username

            if login in user_data_dict:

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                bot.send_message(message.chat.id, f"\n{format_data}")
                bot.send_message(message.chat.id,
                                 f'If you want to change info in this base, write the number or name of stroke')

                bot.register_next_step_handler(message, number_update_stroke, login=login)


            else:

                bot.send_message(message.chat.id,
                                 "Login not found. Please choose 'GET' to try again or 'POST' to enter your "
                                 "information.")
                bot.register_next_step_handler(message, choice_log_postget)

        else:

            bot.send_message(message.chat.id,
                             "Login not found. Please choose 'GET' to try again or 'POST' to enter your "
                             "information.")
            bot.register_next_step_handler(message, choice_log_postget)


    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET"')
        bot.register_next_step_handler(message, choice_log_postget)


def number_update_stroke(message, **kwargs):
    key_message = message.text.lower()

    login = kwargs.get('login')

    list1 = ['1', 'first name', 'first']
    list2 = ['2', 'last name', 'last']
    list3 = ['3', 'country']
    list4 = ['4', 'city']
    list5 = ['5', 'address']
    list6 = ['6', 'post', 'post code', 'code']
    list7 = ['7', 'email', 'email address']
    list8 = ['8', 'phone', 'phone number', 'number']

    if key_message in list1:
        answer = 'Okay! Then write new info into "First Name" stroke:'
        bot.send_message(message.chat.id, answer)

        bot.register_next_step_handler(message, update_key1, login=login)

    elif key_message in list2:
        answer = 'Okay! Then write new info into "Last Name" stroke:'
        bot.send_message(message.chat.id, answer)

        bot.register_next_step_handler(message, update_key2, login=login)

    elif key_message in list3:
        answer = 'Okay! Then write new info into "Country" stroke:'
        bot.send_message(message.chat.id, answer)

        bot.register_next_step_handler(message, update_key3, login=login)

    elif key_message in list4:
        answer = 'Okay! Then write new info into "City" stroke:'
        bot.send_message(message.chat.id, answer)

        bot.register_next_step_handler(message, update_key4, login=login)

    elif key_message in list5:
        answer = 'Okay! Then write new info into "Address" stroke:'
        bot.send_message(message.chat.id, answer)

        bot.register_next_step_handler(message, update_key5, login=login)

    elif key_message in list6:
        answer = 'Okay! Then write new info into "Post Code" stroke:'
        bot.send_message(message.chat.id, answer)

        bot.register_next_step_handler(message, update_key6, login=login)

    elif key_message in list7:
        answer = 'Okay! Then write new info into "Email" stroke:'
        bot.send_message(message.chat.id, answer)

        bot.register_next_step_handler(message, update_key7, login=login)

    elif key_message in list8:
        answer = 'Okay! Then write new info into "Phone number" stroke:'
        bot.send_message(message.chat.id, answer)

        bot.register_next_step_handler(message, update_key8, login=login)

    else:
        answer = f'ERROR'
        bot.send_message(message.chat.id, answer)



def update_key1(message, **kwargs):
    global format_data
    key_update = message.text
    login = kwargs.get('login')

    try:
        # with open('user_data.json', 'r') as file:
        #     user_data_dict = json.load(file)

        # Check if the login exists in the data
        if login in user_data_dict:
            # Modify the value (e.g., change the first_name)
            user_data_dict[login]['first_name'] = key_update

            # Save the updated JSON data
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

        bot.send_message(message.chat.id,
                         f'Great! Now your first name is {key_update}\n\nHere\'s your new info:{format_data}')
        bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE')
        bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE"')
        bot.register_next_step_handler(message, choice_log_postget)

def update_key2(message, **kwargs):
    key_update = message.text
    login = kwargs.get('login')

    try:
        # with open('user_data.json', 'r') as file:
        #     user_data_dict = json.load(file)

        # Check if the login exists in the data
        if login in user_data_dict:
            # Modify the value (e.g., change the first_name)
            user_data_dict[login]['last_name'] = key_update

            # Save the updated JSON data
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

            bot.send_message(message.chat.id,
                             f'Great! Now your last name is {key_update}\n\nHere\'s your new info:{format_data}')
            bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE')
            bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE"')
        bot.register_next_step_handler(message, choice_log_postget)

def update_key3(message, **kwargs):
    global format_data
    key_update = message.text
    login = kwargs.get('login')

    try:
        # with open('user_data.json', 'r') as file:
        #     user_data_dict = json.load(file)

        # Check if the login exists in the data
        if login in user_data_dict:
            # Modify the value (e.g., change the first_name)
            user_data_dict[login]['country'] = key_update

            # Save the updated JSON data
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

        bot.send_message(message.chat.id,
                         f'Great! Now your country is {key_update}\n\nHere\'s your new info {format_data}')
        bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE')
        bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE"')
        bot.register_next_step_handler(message, choice_log_postget)

def update_key4(message, **kwargs):
    global format_data
    key_update = message.text
    login = kwargs.get('login')

    try:
        # with open('user_data.json', 'r') as file:
        #     user_data_dict = json.load(file)

        # Check if the login exists in the data
        if login in user_data_dict:
            # Modify the value (e.g., change the first_name)
            user_data_dict[login]['city'] = key_update

            # Save the updated JSON data
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

        bot.send_message(message.chat.id,
                         f'Great! Now your city is {key_update}\n\nHere\'s your new info:{format_data}')
        bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE')
        bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE"')
        bot.register_next_step_handler(message, choice_log_postget)

def update_key5(message, **kwargs):
    global format_data
    key_update = message.text
    login = kwargs.get('login')

    try:
        # with open('user_data.json', 'r') as file:
        #     user_data_dict = json.load(file)

        # Check if the login exists in the data
        if login in user_data_dict:
            # Modify the value (e.g., change the first_name)
            user_data_dict[login]['address'] = key_update

            # Save the updated JSON data
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

        bot.send_message(message.chat.id,
                         f"Great! Now your address is {key_update}\n\nHere's your new info:{format_data}")
        bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE')

    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE"')
        bot.register_next_step_handler(message, choice_log_postget)

def update_key6(message, **kwargs):
    global format_data
    key_update = message.text
    login = kwargs.get('login')

    try:
        # with open('user_data.json', 'r') as file:
        #     user_data_dict = json.load(file)

        # Check if the login exists in the data
        if login in user_data_dict:
            # Modify the value (e.g., change the first_name)
            user_data_dict[login]['post_code'] = key_update

            # Save the updated JSON data
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

        bot.send_message(f"Great! Now your postcode is {key_update}\n\nHere's your new data:{format_data}",
                         message.chat.id)
        bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE')
        bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE"')
        bot.register_next_step_handler(message, choice_log_postget)

def update_key7(message, **kwargs):
    global format_data
    key_update = message.text
    login = kwargs.get('login')

    try:
        # with open('user_data.json', 'r') as file:
        #     user_data_dict = json.load(file)

        # Check if the login exists in the data
        if login in user_data_dict:
            # Modify the value (e.g., change the first_name)
            user_data_dict[login]['email_address'] = key_update

            # Save the updated JSON data
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

        bot.send_message(message.chat.id,
                         f"Great! Now your email is {key_update}\n\nHere's your new info:{format_data}")
        bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE')
        bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE"')
        bot.register_next_step_handler(message, choice_log_postget)

def update_key8(message, **kwargs):
    global format_data
    key_update = message.text
    login = kwargs.get('login')

    try:
        # with open('user_data.json', 'r') as file:
        #     user_data_dict = json.load(file)

        # Check if the login exists in the data
        if login in user_data_dict:
            # Modify the value (e.g., change the first_name)
            user_data_dict[login]['phone_number'] = key_update

            # Save the updated JSON data
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

        bot.send_message(message.chat.id,
                         f"Great! Now your phone number is {key_update}\n\nHere's your new info:{format_data}")
        bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE')
        bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE"')
        bot.register_next_step_handler(message, choice_log_postget)
