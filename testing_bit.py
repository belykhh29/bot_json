import urllib.parse
import telebot
import json
import requests
import re

bot = telebot.TeleBot('6675934034:AAGsheR9_43zRrHk0l9ggrbkFvZqSuKAly4')
user_data_dict = {}

class ValidationError(Exception):
    """Raises when password is not valid."""
pattern1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

# Load existing user data from JSON file
try:
    with open('user_data.json', 'r') as file:
        user_data_dict = json.load(file)
except FileNotFoundError:
    user_data_dict = {}
except json.decoder.JSONDecodeError:
    user_data_dict = {}


@bot.message_handler(content_types=['text'])
def start(message):
    starting = message.text
    start_list = ['/start', 'start', 'старт']

    if starting in start_list:

        welcome_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        start_button = telebot.types.KeyboardButton("START")
        welcome_markup.row(start_button)

        bot.send_message(message.chat.id, 'Hi! Click the button "START"!', reply_markup=welcome_markup)
        bot.register_next_step_handler(message, welcome)

    else:

        bot.send_message(message.chat.id, f'ERROR!\n\n Write again /start')
        bot.register_next_step_handler(message, start)


@bot.message_handler(commands=['START', 'start'])
def welcome(message):
    message_user = message.text
    user_m_list = ['START', 'start']

    if message_user in user_m_list:

        bot.send_message(message.chat.id,
                         "Hello! We would love to register you into our base if you're not registered")

        choice_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        l_button = telebot.types.KeyboardButton("POST")
        s_button = telebot.types.KeyboardButton("GET")
        u_button = telebot.types.KeyboardButton('UPDATE')
        d_button = telebot.types.KeyboardButton("DELETE")

        choice_markup.row(l_button, s_button)
        choice_markup.row(u_button, d_button)

        bot.send_message(message.chat.id, "Please, choose the action:", reply_markup=choice_markup)

        bot.register_next_step_handler(message, choice_log_postget)

    else:

        welcome_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        start_button = telebot.types.KeyboardButton("START")
        welcome_markup.row(start_button)

        w_answer = 'Nah, you must be wrong! Press the button  "START" to continue'
        bot.send_message(message.chat.id, w_answer, reply_markup=welcome_markup)
        bot.register_next_step_handler(message, welcome)


# Function to choose a request in JSON
@bot.message_handler(commands=["POST", "GET", 'post', 'get', 'DELETE', 'UPDATE', 'Delete', 'Update', 'delete', 'update',
                               'Post', 'Get'])
def choice_log_postget(message):
    users_choice = message.text

    users_choice_list = ['GET', 'get', 'Get']
    users_choice_list1 = ['POST', 'post', 'Post']
    user_choice_list2 = ['UPDATE', 'Update', 'update']
    user_choice_list3 = ['DELETE', 'Delete', 'delete']

    if users_choice in users_choice_list:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
        newlogin_button = telebot.types.KeyboardButton(r'Write manually login')

        give_signupid_markup.row(givesid_button, newlogin_button)

        bot.send_message(message.chat.id, f'Choose the option how to get a data:', reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, new_or_id, users_choice=users_choice)

    elif users_choice in users_choice_list1:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
        newlogin_button = telebot.types.KeyboardButton(r'Write manually login')

        give_signupid_markup.row(givesid_button, newlogin_button)

        bot.send_message(message.chat.id, f'Choose the option how to post a data into base:',
                         reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, new_or_id, users_choice=users_choice)

    elif users_choice in user_choice_list2:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
        newlogin_button = telebot.types.KeyboardButton(r'Write manually login')

        give_signupid_markup.row(givesid_button, newlogin_button)

        bot.send_message(message.chat.id, f'Choose the option how to update a data in our base:',
                         reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, new_or_id, users_choice=users_choice)

    elif users_choice in user_choice_list3:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
        newlogin_button = telebot.types.KeyboardButton(r'Write manually login')

        give_signupid_markup.row(givesid_button, newlogin_button)

        bot.send_message(message.chat.id, f'Choose the option how to delete a data:',
                         reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, new_or_id, users_choice=users_choice)

    else:
        bot.send_message(message.chat.id, 'ERROR: Invalid choice')
        bot.send_message(message.chat.id, 'Please, write again POST or GET or UPDATE or DELETE')
        bot.register_next_step_handler(message, choice_log_postget)

# Function to choose Telegram Username as login or manually login
def new_or_id(message, **kwargs):
    choice_user = message.text.lower()
    users_choice = kwargs.get('users_choice')

    users_choice_list = ['GET', 'get', 'Get']
    users_choice_list1 = ['POST', 'post', 'Post']
    users_choice_list2 = ['UPDATE', 'Update', 'update']
    users_choice_list3 = ['DELETE', 'Delete', 'delete']

    try:

        if choice_user == 'take my id as a login':
            # username = message.from_user.username
            # login = username
            agree_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            agree_button = telebot.types.KeyboardButton(r'✅')

            agree_markup.row(agree_button)

            bot.send_message(message.chat.id, f'Please, press the button for get permission to take your Telegram '
                                              f'username as a login in our base:', reply_markup=agree_markup)

            # GET
            if users_choice in users_choice_list:
                bot.register_next_step_handler(message, log_pass)

            elif users_choice in users_choice_list1:
                bot.register_next_step_handler(message, log_post)

            elif users_choice in users_choice_list2:
                bot.register_next_step_handler(message, update_info)

            elif users_choice in users_choice_list3:
                bot.register_next_step_handler(message, start_delete_process)


        elif choice_user == 'write manually login':
            bot.send_message(message.chat.id, 'Okay! Then write a login for get a data from our base')

            if users_choice in users_choice_list:
                bot.register_next_step_handler(message, log_pass)

            elif users_choice in users_choice_list1:
                bot.register_next_step_handler(message, log_post)

            elif users_choice in users_choice_list2:
                bot.register_next_step_handler(message, update_info)

            elif users_choice in users_choice_list3:
                bot.register_next_step_handler(message, start_delete_process)


        else:

            bot.send_message(message.chat.id, 'ERROR: Invalid choice')
            bot.send_message(message.chat.id, 'Please, choose the option again')
            bot.register_next_step_handler(message, new_or_id)


    except Exception as e:

        bot.register_next_step_handler(message, choice_log_postget)
        return f"Error: {e}"


# Function to make a request DEL data in JSON
def start_delete_process(message):
    try:
        login = message.text

        if login in user_data_dict:

            if login in user_data_dict:

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                delete_data_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                yes_button = telebot.types.KeyboardButton(r'Yes')
                no_button = telebot.types.KeyboardButton(r'No')

                delete_data_markup.row(yes_button, no_button)

                bot.send_message(message.chat.id,
                                 f"Here's {login}'s data:\n\n{format_data}\n\nDo you really want to delete this data?")
                bot.send_message(message.chat.id,
                                 f'Choose the option: Y/N, Yes/No', reply_markup=delete_data_markup)

                bot.register_next_step_handler(message, delete_user_data, login=login)

            else:

                bot.send_message(message.chat.id,
                                 f"Login {login} wasn't found. Please choose 'GET' to try again, 'POST' to enter your "
                                 "information or 'UPDATE' to change information in login's base or 'DELETE' to delete "
                                 "data")
                bot.register_next_step_handler(message, choice_log_postget)


        elif login == r"✅":

            username = message.from_user.username
            login = username

            if login in user_data_dict:

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                delete_data_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                yes_button = telebot.types.KeyboardButton(r'Yes')
                no_button = telebot.types.KeyboardButton(r'No')

                delete_data_markup.row(yes_button, no_button)

                bot.send_message(message.chat.id,
                                 f"Here's {login}'s data:\n\n{format_data}\n\nDo you really want to delete this data?")
                bot.send_message(message.chat.id,
                                 f'Choose the option: Y/N, Yes/No', reply_markup=delete_data_markup)

                bot.register_next_step_handler(message, delete_user_data, login=login)

            else:

                bot.send_message(message.chat.id, f"Your login {login} not found")
                bot.send_message(message.chat.id, f"Please choose 'GET' to try again, 'POST' to enter your "
                                                  "information or 'UPDATE' to change information in login's base or "
                                                  "'DELETE' to delete data")

                bot.register_next_step_handler(message, choice_log_postget)

        else:

            bot.send_message(message.chat.id,
                             f"Login {login} wasn't found. Please choose 'GET' to try again, 'POST' to enter your "
                             "information or 'UPDATE' to change information in login's base.")
            bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:

        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST”, “GET", "UPDATE", "DELETE" to continue')

        bot.register_next_step_handler(message, choice_log_postget)

# Function to delete a data in JSON
def delete_user_data(message, **kwargs):
    try:
        login_to_delete = kwargs.get('login')
        user_data = user_data_dict[login_to_delete]
        users_choice = message.text

        if users_choice == 'Yes':

            # Проверка наличия логина в базе данных
            # if login_to_delete in user_data_dict:
            del user_data_dict[login_to_delete]

            # Сохранение обновленной JSON-информации
            with open('user_data.json', 'w') as file:
                json.dump(user_data_dict, file)

            bot.send_message(message.chat.id, f"User data for login '{login_to_delete}' has been deleted.")
            bot.send_message(message.chat.id, "Come back with commands: /start, POST, GET, UPDATE, DELETE")

            url_delete = f'http://127.0.0.1:5000/json-example?login={login_to_delete}'
            r = requests.delete(url_delete)
            print(r.status_code)

            bot.register_next_step_handler(message, choice_log_postget)


        elif users_choice == 'No':

            bot.send_message(message.chat.id, f'Okay! Let me know if you want to delete the data')
            bot.send_message(message.chat.id, f"Please, write the \"POST\", \"GET\", \"UPDATE\" or \"DELETE\" "
                                              f"to continue working with me")

            bot.register_next_step_handler(message, choice_log_postget)

        else:

            bot.send_message(message.chat.id, f'ERROR: Incorrect choice, please choose "Yes" or "No" to continue.')
            bot.send_message(message.chat.id, "Please try again or check the login.")

            bot.register_next_step_handler(message, start_delete_process)

    except Exception as e:

        bot.send_message(message.chat.id, f"ERROR: {e}")
        bot.send_message(message.chat.id, "Please, try again with commands: /start, POST, GET, UPDATE, DELETE")

        bot.register_next_step_handler(message, start_delete_process)



# Function to make a request UPDATE in JSON
def update_info(message):
    try:

        # update()
        login = message.text
        url_get = f'http://127.0.0.1:5000/json-example?login={login}'  # Modify this line
        r = requests.get(url_get)

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

            url_get = f'http://127.0.0.1:5000/json-example?login={login}'  # Modify this line
            r = requests.get(url_get)

            if login in url_get:

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                bot.send_message(message.chat.id, f"\n{format_data}")
                bot.send_message(message.chat.id,
                                 f'If you want to change info in this base, write the number or name of stroke')

                bot.register_next_step_handler(message, number_update_stroke, login=login)


            else:

                bot.send_message(message.chat.id,
                                 "Login not found. \nPlease choose 'GET' to try again or 'POST' to enter your "
                                 "information.")
                bot.register_next_step_handler(message, choice_log_postget)
            print(r.json())

        else:

            bot.send_message(message.chat.id,
                             "Login not found. \nPlease choose 'GET' to try again or 'POST' to enter your "
                             "information.")
            bot.register_next_step_handler(message, choice_log_postget)


    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET"')
        bot.register_next_step_handler(message, choice_log_postget)

# Function to choose a stroke for UPDATE in JSON file
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
        answer = f'Okay! Then write new info into "First Name" stroke:'
        bot.send_message(message.chat.id, answer)

    elif key_message in list2:
        answer = 'Okay! Then write new info into "Last Name" stroke:'
        bot.send_message(message.chat.id, answer)

    elif key_message in list3:
        answer = 'Okay! Then write new info into "Country" stroke:'
        bot.send_message(message.chat.id, answer)

    elif key_message in list4:
        answer = 'Okay! Then write new info into "City" stroke:'
        bot.send_message(message.chat.id, answer)

    elif key_message in list5:
        answer = 'Okay! Then write new info into "Address" stroke:'
        bot.send_message(message.chat.id, answer)

    elif key_message in list6:
        answer = 'Okay! Then write new info into "Post Code" stroke:'
        bot.send_message(message.chat.id, answer)

    elif key_message in list7:
        answer = 'Okay! Then write new info into "Email" stroke:'
        bot.send_message(message.chat.id, answer)

    elif key_message in list8:
        answer = 'Okay! Then write new info into "Phone number" stroke:'
        bot.send_message(message.chat.id, answer)

    else:
        answer = f'ERROR'
        bot.send_message(message.chat.id, answer)

    bot.register_next_step_handler(message, update_key, login=login, key_message=key_message)

# Function to UPDATE a data in JSON
def update_key(message, **kwargs):
    global format_data
    key_update = message.text
    key_message = kwargs.get('key_message')
    login = kwargs.get('login')

    list1 = ['1', 'first name', 'first']
    list2 = ['2', 'last name', 'last']
    list3 = ['3', 'country']
    list4 = ['4', 'city']
    list5 = ['5', 'address']
    list6 = ['6', 'post', 'post code', 'code']
    list7 = ['7', 'email', 'email address']
    list8 = ['8', 'phone', 'phone number', 'number']

    try:

        if key_message in list1:

            # Check if the login exists in the data
            if login in user_data_dict:
                # Modify the value
                user_data_dict[login]['first_name'] = key_update

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                url_post = 'http://127.0.0.1:5000/json-example'
                # post_response_json = response.post.json()

                r = requests.put(url_post, json=user_data)
                print(r.json)
                print(r.status_code)

            bot.send_message(message.chat.id,
                             f'Great! Now your first name is {key_update}\n\nHere\'s your new info:{format_data}')
            bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
            bot.register_next_step_handler(message, choice_log_postget)

        elif key_message in list2:

            if login in user_data_dict:
                # Modify the value (e.g., change the first_name)
                user_data_dict[login]['last_name'] = key_update

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                url_post = 'http://127.0.0.1:5000/json-example'
                # post_response_json = response.post.json()

                r = requests.put(url_post, json=user_data)
                print(r.json)
                print(r.status_code)

                bot.send_message(message.chat.id,
                                 f'Great! Now your last name is {key_update}\n\nHere\'s your new info:{format_data}')
                bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
                bot.register_next_step_handler(message, choice_log_postget)

        elif key_message in list3:

            # Check if the login exists in the data
            if login in user_data_dict:
                # Modify the value (e.g., change the first_name)
                user_data_dict[login]['country'] = key_update

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                url_post = 'http://127.0.0.1:5000/json-example'
                # post_response_json = response.post.json()

                r = requests.put(url_post, json=user_data)
                print(r.json)
                print(r.status_code)

            bot.send_message(message.chat.id,
                             f'Great! Now your country is {key_update}\n\nHere\'s your new info {format_data}')
            bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
            bot.register_next_step_handler(message, choice_log_postget)

        elif key_message in list4:

            # Check if the login exists in the data
            if login in user_data_dict:
                # Modify the value (e.g., change the first_name)
                user_data_dict[login]['city'] = key_update

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                url_post = 'http://127.0.0.1:5000/json-example'
                # post_response_json = response.post.json()

                r = requests.put(url_post, json=user_data)
                print(r.json)
                print(r.status_code)

            bot.send_message(message.chat.id,
                             f'Great! Now your city is {key_update}\n\nHere\'s your new info:{format_data}')
            bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
            bot.register_next_step_handler(message, choice_log_postget)

        elif key_message in list5:

            # Check if the login exists in the data
            if login in user_data_dict:
                # Modify the value (e.g., change the first_name)
                user_data_dict[login]['address'] = key_update

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                url_post = 'http://127.0.0.1:5000/json-example'
                # post_response_json = response.post.json()

                r = requests.put(url_post, json=user_data)
                print(r.json)
                print(r.status_code)

            bot.send_message(message.chat.id,
                             f"Great! Now your address is {key_update}\n\nHere's your new info:{format_data}")
            bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')

        elif key_message in list6:

            # Check if the login exists in the data
            if login in user_data_dict:
                # Modify the value (e.g., change the first_name)
                user_data_dict[login]['post_code'] = key_update

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                url_post = 'http://127.0.0.1:5000/json-example'
                # post_response_json = response.post.json()

                r = requests.put(url_post, json=user_data)
                print(r.json)
                print(r.status_code)

            bot.send_message(f"Great! Now your postcode is {key_update}\n\nHere's your new data:{format_data}",
                             message.chat.id)
            bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
            bot.register_next_step_handler(message, choice_log_postget)

        elif key_message in list7:

            # Check if the login exists in the data
            if login in user_data_dict:
                # Modify the value (e.g., change the first_name)
                user_data_dict[login]['email_address'] = key_update

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                url_post = 'http://127.0.0.1:5000/json-example'
                # post_response_json = response.post.json()

                r = requests.put(url_post, json=user_data)
                print(r.json)
                print(r.status_code)

            bot.send_message(message.chat.id,
                             f"Great! Now your email is {key_update}\n\nHere's your new info:{format_data}")
            bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
            bot.register_next_step_handler(message, choice_log_postget)

        elif key_message in list8:

            if login in user_data_dict:
                # Modify the value (e.g., change the first_name)
                user_data_dict[login]['phone_number'] = key_update

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)

                url_post = 'http://127.0.0.1:5000/json-example'
                # post_response_json = response.post.json()

                r = requests.put(url_post, json=user_data)
                print(r.json)
                print(r.status_code)

            bot.send_message(message.chat.id,
                             f"Great! Now your phone number is {key_update}\n\nHere's your new info:{format_data}")
            bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
            bot.register_next_step_handler(message, choice_log_postget)

        else:

            bot.send_message(message.chat.id, f"Sorry, but I can't recognize your text. Please try again")
            bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE" or "DELETE"')
            bot.register_next_step_handler(message, choice_log_postget)



    except Exception as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id,
                         f"Please, try again and choose \"POST\" or \"GET\" or \"UPDATE\" or \"DELETE\" to continue.")
        bot.register_next_step_handler(message, choice_log_postget)



def log_pass(message):
    try:
        login = message.text

        # Отправить запрос на сервер Flask, чтобы проверить наличие логина
        url_check_login = 'http://127.0.0.1:5000/check-login'  # Измените на свой URL
        data = {'login': login}
        response = requests.post(url_check_login, json=data)

        if response.status_code == 200 and response.json().get('exists', False):
            # Логин существует на сервере Flask, переход к следующему шагу
            user_data = response.json().get('user_data', {})
            bot.send_message(message.chat.id, f"Great! Now write the password for {login}")
            bot.register_next_step_handler(message, log_in, login=login)

        elif login == r"✅":
            # Логин взят из профиля пользователя
            username = message.from_user.username
            login = username

            # Повторить проверку логина на сервере Flask
            url_check_login = 'http://127.0.0.1:5000/check-login'  # Измените на свой URL
            data = {'login': login}
            response = requests.post(url_check_login, json=data)
            print(response.json())

            if response.status_code == 200 and response.json().get('exists', False):
                # Логин существует на сервере Flask, переход к следующему шагу
                user_data = response.json().get('user_data', {})
                bot.send_message(message.chat.id, f"Great! Now write the password for {login}")
                bot.register_next_step_handler(message, log_in, login=login)

            else:
                bot.send_message(message.chat.id, f"Login {login} was not found.\n")
                bot.send_message(message.chat.id,
                                 'Please choose \'GET\' to try again, \'POST\', \'GET\', \'UPDATE\' or \'DELETE\'.')
                bot.register_next_step_handler(message, choice_log_postget)

        else:
            bot.send_message(message.chat.id, f"Login {login} was not found.\n")
            bot.send_message(message.chat.id,
                             'Please choose \'GET\' to try again, \'POST\', \'GET\', \'UPDATE\' or \'DELETE\'.')
            bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET”')
        bot.register_next_step_handler(message, choice_log_postget)

# Function to make a request GET in JSON and get data
def log_in(message, **kwargs):
    try:
        user_pass = message.text
        login = kwargs.get('login')

        url_get = f'http://127.0.0.1:5000/json-example?login={login}'  # Параметры передаются в URL
        r = requests.get(url_get)

        if r.status_code == 200:
            flask_data = r.json()
            exists = flask_data.get('exists', False)

            if exists:
                user_data = flask_data.get('user_data', {})

                # Check if the expected fields are present in the received data
                required_fields = ['login', 'first_name', 'last_name', 'country', 'city', 'address', 'post_code',
                                   'email_address', 'phone_number', 'password']
                if all(field in user_data for field in required_fields):
                    format_data = format_user_data(user_data)
                    bot.send_message(message.chat.id, f"Here's {login}'s data:\n\n{format_data}")
                else:
                    bot.send_message(message.chat.id, f"Error: Incomplete data received from Flask.")
            else:
                bot.send_message(message.chat.id, f"User with login {login} not found.")
        else:
            # If there is an error in the GET request, print the error message
            print("Error from Flask:", r.json())
            bot.send_message(message.chat.id, f"Error retrieving {login}'s data.")

        # Continue with your existing code...
        bot.send_message(message.chat.id, f'If you want to continue working on our base, write POST or GET or UPDATE or DELETE')
        bot.register_next_step_handler(message, choice_log_postget)
    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET”')
        bot.register_next_step_handler(message, choice_log_postget)


# Function to make a request POST in JSON and save data
def log_post(message):
    login = message.text.lower()

    try:

        print(f"DEBUG: log_post - login: {login}")

        if login != r'✅':

            if login in user_data_dict:
                #     and login in user_data_dict[user_id]):

                bot.send_message(message.chat.id, "Login already exists. Please choose 'POST, GET, UPDATE, DELETE' "
                                                  "to continue working with data.")
                bot.register_next_step_handler(message, choice_log_postget)

            else:
                # Initialize a new user entry
                user_data_dict[login] = {'login': login}

                bot.send_message(message.chat.id,
                                 f"Great! Your login is {login}\n\n Please, write your new password for {login}")
                bot.register_next_step_handler(message, post_pass, login=login, pattern=pattern1)

                # return login


        else:

            username = message.from_user.username
            login = username

            if login in user_data_dict:
                #     and login in user_data_dict[user_id]):

                bot.send_message(message.chat.id, "Login already exists. Please choose 'POST, GET, UPDATE, DELETE' "
                                                  "to continue working with data.")
                bot.register_next_step_handler(message, choice_log_postget)

            else:

                username = message.from_user.username
                login = username
                user_data_dict[login] = {'login': login}

                bot.send_message(message.chat.id,
                                 f"Great! Your login is {login}\n\n Please, write your new password for {login}")
                bot.register_next_step_handler(message, post_pass, login=login, pattern=pattern1)

                # return login

    except Exception as e:
        print(f"DEBUG: log_post - login: {login}")

        # print(f"DEBUG: log_post - Exception: {e}")

        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET" or "UPDATE" or "DELETE" ')
        bot.register_next_step_handler(message, choice_log_postget)

def validate_by_regexp(password, pattern):
    """Валидация пароля по регулярному выражению."""
    if re.match(pattern, password) is None:
        raise ValidationError('Password has incorrect format.')

def post_pass(message, pattern, **kwargs):
    global login
    try:
        user_pass = message.text
        login = kwargs.get('login')

        if re.match(pattern, user_pass) is None:
            raise ValidationError('Password has incorrect format.')

        # Use validate_by_regexp function instead of re.match directly
        validate_by_regexp(user_pass, pattern)

        # Use assert without 'is None', and remove unnecessary with pytest.raises block
        assert validate_by_regexp(user_pass, pattern) is None

        user_data_dict[login]['password'] = user_pass

        bot.send_message(message.chat.id,
                         f"Great! Now your password is {user_pass}\n\n Let's start with your personal "
                         f"data")
        bot.send_message(message.chat.id, f"Write your first name:")

        bot.register_next_step_handler(message, post_first, login=login)

    except ValidationError as e:

        bot.send_message(message.chat.id, f'ERROR: {e}')
        bot.send_message(message.chat.id, 'Please, try to write another password')
        # Pass the pattern argument to post_pass when re-registering the handler
        bot.register_next_step_handler(message, post_pass, login=login, pattern=pattern1)

    except Exception as e:

        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, 'Please, choose again: "POST" or "GET"')
        bot.register_next_step_handler(message, choice_log_postget)

def post_first(message, **kwargs):
    try:

        first_name = message.text
        login = kwargs.get('login')

        # print(f"DEBUG: post_first - login: {login}")

        user_data_dict[login]['first_name'] = first_name

        bot.send_message(message.chat.id, f'Great! Now your first name is {first_name.title()}\n\n Please, write your '
                                          f'last_name')

        bot.register_next_step_handler(message, post_last, login=login)

    except Exception as e:
        # print(f"DEBUG: post_first - Exception: {e}")

        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_last(message, **kwargs):
    try:

        last_name = message.text

        login = kwargs.get('login')

        user_data_dict[login]['last_name'] = last_name

        bot.send_message(message.chat.id, f'Great! Now your last name is {last_name.title()}\n\n Please, let us '
                                          f'know your address, write your country')

        bot.register_next_step_handler(message, post_country, login=login)

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_country(message, **kwargs):
    try:

        login = kwargs.get('login')

        country = message.text.lower()

        user_data_dict[login]['country'] = message.text

        bot.send_message(message.chat.id,
                         f"Great! Now your country is {country.title()}\n\n Please, let us know your "
                         f"city, write the name of your city")
        bot.register_next_step_handler(message, post_city, login=login)

        return country

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_city(message, **kwargs):
    try:

        login = kwargs.get('login')
        city = message.text.lower()
        user_data_dict[login]['city'] = message.text

        bot.send_message(message.chat.id,
                         f"Great! Now your city is {city.title()}\n\n Please, let us know your street "
                         f"and house number, write your street and house number")
        bot.register_next_step_handler(message, post_address, login=login)

        return city

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_address(message, **kwargs):
    try:

        address = message.text.lower()
        login = kwargs.get('login')

        # user_data_dict.setdefault(login, {})
        user_data_dict[login]['address'] = message.text

        # streetaddress.capitalize()
        bot.send_message(message.chat.id,
                         f"Great! Now your street and house number is {address.title()}\n"
                         f"Please, let us memorize your post code, write it")

        bot.register_next_step_handler(message, post_index, login=login)

        return address

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_index(message, **kwargs):
    try:

        login = kwargs.get('login')

        index = message.text.lower()

        user_data_dict.setdefault(login, {})
        user_data_dict[login]['post_code'] = message.text

        bot.send_message(message.chat.id,
                         f"Great! Your post code is  {index.title()}\n\n Now let us know your email address, please "
                         f"write it")
        bot.register_next_step_handler(message, post_email, login=login)

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_email(message, **kwargs):
    try:

        login = kwargs.get('login')

        email_address = message.text.lower()

        user_data_dict[login]['email_address'] = message.text

        bot.send_message(message.chat.id,
                         f'Great! Your email is {email_address}\n\n Now let us know your phone number, please write it')
        bot.register_next_step_handler(message, post_phone, login=login)

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_phone(message, **kwargs):
    try:
        login = kwargs.get('login')
        phone_number = message.text.lower()

        user_data_dict[login]['phone_number'] = message.text

        user_data = user_data_dict.get(login, {})

        # with open('user_data.json', 'w') as file:
        #     json.dump(user_data_dict, file)

        url_post = 'http://127.0.0.1:5000/json-example'

        r = requests.post(url_post, json={login: user_data})
        print(r.json)
        print(r.status_code)

        bot.send_message(message.chat.id,
                         f'Great! Your phone number is {phone_number}\n\nData successfully saved!')
        bot.send_message(message.chat.id, f"Choose again, POST or GET to continue.")
        bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)



def format_user_data(user_data):
    try:
        if isinstance(user_data, dict) and user_data:
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
                    f'8. Phone Number: {user_data["phone_number"]}\n'
                    f'9. Password: {user_data.get("password", "")}')
            return data
        else:
            return "User data not found or invalid."
    except Exception as e:
        return f"Error formatting user data: {e}"



bot.infinity_polling()





# #PREVIOUS CODE
# import pytest
# import telebot
# import json
# import requests
# import re
#
# bot = telebot.TeleBot('6370996369:AAEqn8epM8aKiMM9zzAEHYSjOkz0K_PU5nE')
# user_data_dict = {}
#
# class ValidationError(Exception):
#     """Raises when password is not valid."""
#     # pattern1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
#     # pattern2 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
#
#
# pattern1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
# pattern2 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
#
# # Load existing user data from JSON file
# try:
#     with open('user_data.json', 'r') as file:
#         user_data_dict = json.load(file)
# except FileNotFoundError:
#     user_data_dict = {}
# except json.decoder.JSONDecodeError:
#     user_data_dict = {}
#
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     starting = message.text
#     start_list = ['/start', 'start', 'старт']
#
#     if starting in start_list:
#
#         welcome_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         start_button = telebot.types.KeyboardButton("START")
#         welcome_markup.row(start_button)
#
#         bot.send_message(message.chat.id, 'Hi! Click the button "START"!', reply_markup=welcome_markup)
#         bot.register_next_step_handler(message, welcome)
#
#     else:
#
#         bot.send_message(message.chat.id, f'ERROR!\n\n Write again /start')
#         bot.register_next_step_handler(message, start)
#
#
# @bot.message_handler(commands=['START', 'start'])
# def welcome(message):
#     message_user = message.text
#     user_m_list = ['START', 'start']
#
#     if message_user in user_m_list:
#
#         bot.send_message(message.chat.id,
#                          "Hello! We would love to register you into our base if you're not registered")
#
#         choice_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         l_button = telebot.types.KeyboardButton("POST")
#         s_button = telebot.types.KeyboardButton("GET")
#         u_button = telebot.types.KeyboardButton('UPDATE')
#         d_button = telebot.types.KeyboardButton("DELETE")
#
#         choice_markup.row(l_button, s_button)
#         choice_markup.row(u_button, d_button)
#
#         bot.send_message(message.chat.id, "Please, choose the action:", reply_markup=choice_markup)
#
#         bot.register_next_step_handler(message, choice_log_postget)
#
#     else:
#
#         welcome_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         start_button = telebot.types.KeyboardButton("START")
#         welcome_markup.row(start_button)
#
#         w_answer = 'Nah, you must be wrong! Press the button  "START" to continue'
#         bot.send_message(message.chat.id, w_answer, reply_markup=welcome_markup)
#         bot.register_next_step_handler(message, welcome)
#
#
# # Function to choose a request in JSON
# @bot.message_handler(commands=["POST", "GET", 'post', 'get', 'DELETE', 'UPDATE', 'Delete', 'Update', 'delete', 'update',
#                                'Post', 'Get'])
# def choice_log_postget(message):
#     users_choice = message.text
#
#     users_choice_list = ['GET', 'get', 'Get']
#     users_choice_list1 = ['POST', 'post', 'Post']
#     user_choice_list2 = ['UPDATE', 'Update', 'update']
#     user_choice_list3 = ['DELETE', 'Delete', 'delete']
#
#     if users_choice in users_choice_list:
#
#         give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
#         newlogin_button = telebot.types.KeyboardButton(r'Write manually login')
#
#         give_signupid_markup.row(givesid_button, newlogin_button)
#
#         bot.send_message(message.chat.id, f'Choose the option how to get a data:', reply_markup=give_signupid_markup)
#
#         bot.register_next_step_handler(message, new_or_id, users_choice=users_choice)
#
#     elif users_choice in users_choice_list1:
#
#         give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
#         newlogin_button = telebot.types.KeyboardButton(r'Write manually login')
#
#         give_signupid_markup.row(givesid_button, newlogin_button)
#
#         bot.send_message(message.chat.id, f'Choose the option how to post a data into base:',
#                          reply_markup=give_signupid_markup)
#
#         bot.register_next_step_handler(message, new_or_id, users_choice=users_choice)
#
#     elif users_choice in user_choice_list2:
#
#         give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
#         newlogin_button = telebot.types.KeyboardButton(r'Write manually login')
#
#         give_signupid_markup.row(givesid_button, newlogin_button)
#
#         bot.send_message(message.chat.id, f'Choose the option how to update a data in our base:',
#                          reply_markup=give_signupid_markup)
#
#         bot.register_next_step_handler(message, new_or_id, users_choice=users_choice)
#
#     elif users_choice in user_choice_list3:
#
#         give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
#         newlogin_button = telebot.types.KeyboardButton(r'Write manually login')
#
#         give_signupid_markup.row(givesid_button, newlogin_button)
#
#         bot.send_message(message.chat.id, f'Choose the option how to delete a data:',
#                          reply_markup=give_signupid_markup)
#
#         bot.register_next_step_handler(message, new_or_id, users_choice=users_choice)
#
#     else:
#         bot.send_message(message.chat.id, 'ERROR: Invalid choice')
#         bot.send_message(message.chat.id, 'Please, write again POST or GET or UPDATE or DELETE')
#         bot.register_next_step_handler(message, choice_log_postget)
#
#
# # Function to choose Telegram Username as login or manually login
# def new_or_id(message, **kwargs):
#     choice_user = message.text.lower()
#     users_choice = kwargs.get('users_choice')
#
#     users_choice_list = ['GET', 'get', 'Get']
#     users_choice_list1 = ['POST', 'post', 'Post']
#     users_choice_list2 = ['UPDATE', 'Update', 'update']
#     users_choice_list3 = ['DELETE', 'Delete', 'delete']
#
#     try:
#
#         if choice_user == 'take my id as a login':
#             # username = message.from_user.username
#             # login = username
#             agree_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#             agree_button = telebot.types.KeyboardButton(r'✅')
#
#             agree_markup.row(agree_button)
#
#             bot.send_message(message.chat.id, f'Please, press the button for get permission to take your Telegram '
#                                               f'username as a login in our base:', reply_markup=agree_markup)
#
#             # GET
#             if users_choice in users_choice_list:
#                 bot.register_next_step_handler(message, log_pass)
#
#             elif users_choice in users_choice_list1:
#                 bot.register_next_step_handler(message, log_post)
#
#             elif users_choice in users_choice_list2:
#                 bot.register_next_step_handler(message, update_info)
#
#             elif users_choice in users_choice_list3:
#                 bot.register_next_step_handler(message, start_delete_process)
#
#
#         elif choice_user == 'write manually login':
#             bot.send_message(message.chat.id, 'Okay! Then write a login for get a data from our base')
#
#             if users_choice in users_choice_list:
#                 bot.register_next_step_handler(message, log_pass)
#
#             elif users_choice in users_choice_list1:
#                 bot.register_next_step_handler(message, log_post)
#
#             elif users_choice in users_choice_list2:
#                 bot.register_next_step_handler(message, update_info)
#
#             elif users_choice in users_choice_list3:
#                 bot.register_next_step_handler(message, start_delete_process)
#
#
#         else:
#
#             bot.send_message(message.chat.id, 'ERROR: Invalid choice')
#             bot.send_message(message.chat.id, 'Please, choose the option again')
#             bot.register_next_step_handler(message, new_or_id)
#
#
#     except Exception as e:
#
#         bot.register_next_step_handler(message, choice_log_postget)
#         return f"Error: {e}"
#
#
# # Function to make a request DEL data in JSON
# def start_delete_process(message):
#     try:
#         login = message.text
#
#         if login in user_data_dict:
#
#             if login in user_data_dict:
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#                 delete_data_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#                 yes_button = telebot.types.KeyboardButton(r'Yes')
#                 no_button = telebot.types.KeyboardButton(r'No')
#
#                 delete_data_markup.row(yes_button, no_button)
#
#                 bot.send_message(message.chat.id,
#                                  f"Here's {login}'s data:\n\n{format_data}\n\nDo you really want to delete this data?")
#                 bot.send_message(message.chat.id,
#                                  f'Choose the option: Y/N, Yes/No', reply_markup=delete_data_markup)
#
#                 bot.register_next_step_handler(message, delete_user_data, login=login)
#
#             else:
#
#                 bot.send_message(message.chat.id,
#                                  f"Login {login} wasn't found. Please choose 'GET' to try again, 'POST' to enter your "
#                                  "information or 'UPDATE' to change information in login's base or 'DELETE' to delete "
#                                  "data")
#                 bot.register_next_step_handler(message, choice_log_postget)
#
#
#         elif login == r"✅":
#
#             username = message.from_user.username
#             login = username
#
#             if login in user_data_dict:
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#                 delete_data_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#                 yes_button = telebot.types.KeyboardButton(r'Yes')
#                 no_button = telebot.types.KeyboardButton(r'No')
#
#                 delete_data_markup.row(yes_button, no_button)
#
#                 bot.send_message(message.chat.id,
#                                  f"Here's {login}'s data:\n\n{format_data}\n\nDo you really want to delete this data?")
#                 bot.send_message(message.chat.id,
#                                  f'Choose the option: Y/N, Yes/No', reply_markup=delete_data_markup)
#
#                 bot.register_next_step_handler(message, delete_user_data, login=login)
#
#             else:
#
#                 bot.send_message(message.chat.id, f"Your login {login} not found")
#                 bot.send_message(message.chat.id, f"Please choose 'GET' to try again, 'POST' to enter your "
#                                                   "information or 'UPDATE' to change information in login's base or "
#                                                   "'DELETE' to delete data")
#
#                 bot.register_next_step_handler(message, choice_log_postget)
#
#         else:
#
#             bot.send_message(message.chat.id,
#                              f"Login {login} wasn't found. Please choose 'GET' to try again, 'POST' to enter your "
#                              "information or 'UPDATE' to change information in login's base.")
#             bot.register_next_step_handler(message, choice_log_postget)
#
#     except Exception as e:
#
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST”, “GET", "UPDATE", "DELETE" to continue')
#
#         bot.register_next_step_handler(message, choice_log_postget)
#
#
# # Function to delete a data in JSON
# def delete_user_data(message, **kwargs):
#     try:
#         login_to_delete = kwargs.get('login')
#
#         users_choice = message.text
#
#         if users_choice == 'Yes':
#
#             # Проверка наличия логина в базе данных
#             # if login_to_delete in user_data_dict:
#             del user_data_dict[login_to_delete]
#
#             # Сохранение обновленной JSON-информации
#             with open('user_data.json', 'w') as file:
#                 json.dump(user_data_dict, file)
#
#             bot.send_message(message.chat.id, f"User data for login '{login_to_delete}' has been deleted.")
#             bot.send_message(message.chat.id, "Come back with commands: /start, POST, GET, UPDATE, DELETE")
#
#             bot.register_next_step_handler(message, choice_log_postget)
#
#
#         elif users_choice == 'No':
#
#             bot.send_message(message.chat.id, f'Okay! Let me know if you want to delete the data')
#             bot.send_message(message.chat.id, f"Please, write the \"POST\", \"GET\", \"UPDATE\" or \"DELETE\" "
#                                               f"to continue working with me")
#
#             bot.register_next_step_handler(message, choice_log_postget)
#
#         else:
#
#             bot.send_message(message.chat.id, f'ERROR: Incorrect choice, please choose "Yes" or "No" to continue.')
#             bot.send_message(message.chat.id, "Please try again or check the login.")
#
#             bot.register_next_step_handler(message, start_delete_process)
#
#     except Exception as e:
#
#         bot.send_message(message.chat.id, f"ERROR: {e}")
#         bot.send_message(message.chat.id, "Please, try again with commands: /start, POST, GET, UPDATE, DELETE")
#
#         bot.register_next_step_handler(message, start_delete_process)
#
#
# # Function to make a request UPDATE in JSON
# def update_info(message):
#     try:
#
#         # update()
#         login = message.text
#
#         if login in user_data_dict:
#
#             user_data = user_data_dict[login]
#             # Display user information
#             format_data = format_user_data(user_data)
#
#             bot.send_message(message.chat.id, f"\n{format_data}")
#             bot.send_message(message.chat.id,
#                              f'If you want to change info in this base, write the number of stroke')
#
#             bot.register_next_step_handler(message, number_update_stroke, login=login)
#
#         elif login == r"✅":
#
#             username = message.from_user.username
#             login = username
#
#             if login in user_data_dict:
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#                 bot.send_message(message.chat.id, f"\n{format_data}")
#                 bot.send_message(message.chat.id,
#                                  f'If you want to change info in this base, write the number or name of stroke')
#
#                 bot.register_next_step_handler(message, number_update_stroke, login=login)
#
#
#             else:
#
#                 bot.send_message(message.chat.id,
#                                  "Login not found. \nPlease choose 'GET' to try again or 'POST' to enter your "
#                                  "information.")
#                 bot.register_next_step_handler(message, choice_log_postget)
#
#         else:
#
#             bot.send_message(message.chat.id,
#                              "Login not found. \nPlease choose 'GET' to try again or 'POST' to enter your "
#                              "information.")
#             bot.register_next_step_handler(message, choice_log_postget)
#
#
#     except Exception as e:
#
#         bot.send_message(message.chat.id, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET"')
#         bot.register_next_step_handler(message, choice_log_postget)
#
#
# # Function to choose a stroke for UPDATE in JSON file
# def number_update_stroke(message, **kwargs):
#     key_message = message.text.lower()
#
#     login = kwargs.get('login')
#
#     list1 = ['1', 'first name', 'first']
#     list2 = ['2', 'last name', 'last']
#     list3 = ['3', 'country']
#     list4 = ['4', 'city']
#     list5 = ['5', 'address']
#     list6 = ['6', 'post', 'post code', 'code']
#     list7 = ['7', 'email', 'email address']
#     list8 = ['8', 'phone', 'phone number', 'number']
#
#     if key_message in list1:
#         answer = f'Okay! Then write new info into "First Name" stroke:'
#         bot.send_message(message.chat.id, answer)
#
#     elif key_message in list2:
#         answer = 'Okay! Then write new info into "Last Name" stroke:'
#         bot.send_message(message.chat.id, answer)
#
#     elif key_message in list3:
#         answer = 'Okay! Then write new info into "Country" stroke:'
#         bot.send_message(message.chat.id, answer)
#
#     elif key_message in list4:
#         answer = 'Okay! Then write new info into "City" stroke:'
#         bot.send_message(message.chat.id, answer)
#
#     elif key_message in list5:
#         answer = 'Okay! Then write new info into "Address" stroke:'
#         bot.send_message(message.chat.id, answer)
#
#     elif key_message in list6:
#         answer = 'Okay! Then write new info into "Post Code" stroke:'
#         bot.send_message(message.chat.id, answer)
#
#     elif key_message in list7:
#         answer = 'Okay! Then write new info into "Email" stroke:'
#         bot.send_message(message.chat.id, answer)
#
#     elif key_message in list8:
#         answer = 'Okay! Then write new info into "Phone number" stroke:'
#         bot.send_message(message.chat.id, answer)
#
#     else:
#         answer = f'ERROR'
#         bot.send_message(message.chat.id, answer)
#
#     bot.register_next_step_handler(message, update_key, login=login, key_message=key_message)
#
#
# # Function to UPDATE a data in JSON
# def update_key(message, **kwargs):
#     global format_data
#     key_update = message.text
#     key_message = kwargs.get('key_message')
#     login = kwargs.get('login')
#
#     list1 = ['1', 'first name', 'first']
#     list2 = ['2', 'last name', 'last']
#     list3 = ['3', 'country']
#     list4 = ['4', 'city']
#     list5 = ['5', 'address']
#     list6 = ['6', 'post', 'post code', 'code']
#     list7 = ['7', 'email', 'email address']
#     list8 = ['8', 'phone', 'phone number', 'number']
#
#     try:
#
#         if key_message in list1:
#
#             # Check if the login exists in the data
#             if login in user_data_dict:
#                 # Modify the value
#                 user_data_dict[login]['first_name'] = key_update
#
#                 # Save the updated JSON data
#                 with open('user_data.json', 'w') as file:
#                     json.dump(user_data_dict, file)
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#             bot.send_message(message.chat.id,
#                              f'Great! Now your first name is {key_update}\n\nHere\'s your new info:{format_data}')
#             bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
#             bot.register_next_step_handler(message, choice_log_postget)
#
#         elif key_message in list2:
#
#             if login in user_data_dict:
#                 # Modify the value (e.g., change the first_name)
#                 user_data_dict[login]['last_name'] = key_update
#
#                 # Save the updated JSON data
#                 with open('user_data.json', 'w') as file:
#                     json.dump(user_data_dict, file)
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#                 bot.send_message(message.chat.id,
#                                  f'Great! Now your last name is {key_update}\n\nHere\'s your new info:{format_data}')
#                 bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
#                 bot.register_next_step_handler(message, choice_log_postget)
#
#         elif key_message in list3:
#
#             # Check if the login exists in the data
#             if login in user_data_dict:
#                 # Modify the value (e.g., change the first_name)
#                 user_data_dict[login]['country'] = key_update
#
#                 # Save the updated JSON data
#                 with open('user_data.json', 'w') as file:
#                     json.dump(user_data_dict, file)
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#             bot.send_message(message.chat.id,
#                              f'Great! Now your country is {key_update}\n\nHere\'s your new info {format_data}')
#             bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
#             bot.register_next_step_handler(message, choice_log_postget)
#
#         elif key_message in list4:
#
#             # Check if the login exists in the data
#             if login in user_data_dict:
#                 # Modify the value (e.g., change the first_name)
#                 user_data_dict[login]['city'] = key_update
#
#                 # Save the updated JSON data
#                 with open('user_data.json', 'w') as file:
#                     json.dump(user_data_dict, file)
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#             bot.send_message(message.chat.id,
#                              f'Great! Now your city is {key_update}\n\nHere\'s your new info:{format_data}')
#             bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
#             bot.register_next_step_handler(message, choice_log_postget)
#
#         elif key_message in list5:
#
#             # Check if the login exists in the data
#             if login in user_data_dict:
#                 # Modify the value (e.g., change the first_name)
#                 user_data_dict[login]['address'] = key_update
#
#                 # Save the updated JSON data
#                 with open('user_data.json', 'w') as file:
#                     json.dump(user_data_dict, file)
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#             bot.send_message(message.chat.id,
#                              f"Great! Now your address is {key_update}\n\nHere's your new info:{format_data}")
#             bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
#
#         elif key_message in list6:
#
#             # Check if the login exists in the data
#             if login in user_data_dict:
#                 # Modify the value (e.g., change the first_name)
#                 user_data_dict[login]['post_code'] = key_update
#
#                 # Save the updated JSON data
#                 with open('user_data.json', 'w') as file:
#                     json.dump(user_data_dict, file)
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#             bot.send_message(f"Great! Now your postcode is {key_update}\n\nHere's your new data:{format_data}",
#                              message.chat.id)
#             bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
#             bot.register_next_step_handler(message, choice_log_postget)
#
#         elif key_message in list7:
#
#             # Check if the login exists in the data
#             if login in user_data_dict:
#                 # Modify the value (e.g., change the first_name)
#                 user_data_dict[login]['email_address'] = key_update
#
#                 # Save the updated JSON data
#                 with open('user_data.json', 'w') as file:
#                     json.dump(user_data_dict, file)
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#             bot.send_message(message.chat.id,
#                              f"Great! Now your email is {key_update}\n\nHere's your new info:{format_data}")
#             bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
#             bot.register_next_step_handler(message, choice_log_postget)
#
#         elif key_message in list8:
#
#             if login in user_data_dict:
#                 # Modify the value (e.g., change the first_name)
#                 user_data_dict[login]['phone_number'] = key_update
#
#                 # Save the updated JSON data
#                 with open('user_data.json', 'w') as file:
#                     json.dump(user_data_dict, file)
#
#                 user_data = user_data_dict[login]
#                 # Display user information
#                 format_data = format_user_data(user_data)
#
#             bot.send_message(message.chat.id,
#                              f"Great! Now your phone number is {key_update}\n\nHere's your new info:{format_data}")
#             bot.send_message(message.chat.id, f'Come back with commands: /start, POST, GET, UPDATE or DELETE')
#             bot.register_next_step_handler(message, choice_log_postget)
#
#
#
#         else:
#
#             bot.send_message(message.chat.id, f"Sorry, but I can't recognize your text. Please try again")
#             bot.send_message(message.chat.id, f'Please, try again and choose "POST" or "GET" or "UPDATE" or "DELETE"')
#             bot.register_next_step_handler(message, choice_log_postget)
#
#     except Exception as e:
#
#         bot.send_message(message.chat.id, f'ERROR: {e}')
#         bot.send_message(message.chat.id,
#                          f"Please, try again and choose \"POST\" or \"GET\" or \"UPDATE\" or \"DELETE\" to continue.")
#         bot.register_next_step_handler(message, choice_log_postget)
#
#
# def log_pass(message):
#     try:
#         login = message.text
#
#         if login in user_data_dict:
#             user_data = user_data_dict[login]
#             bot.send_message(message.chat.id, f"Great! Now write the password for {login}")
#             bot.register_next_step_handler(message, log_in, login=login)
#
#         elif login == r"✅":
#
#             username = message.from_user.username
#             login = username
#
#             if login in user_data_dict:
#                 user_data = user_data_dict[login]
#                 bot.send_message(message.chat.id, f"Great! Now write the password for {login}")
#                 bot.register_next_step_handler(message, log_in, login=login)
#
#             else:
#
#                 bot.send_message(message.chat.id, f"Login {login} were not founded.\n")
#                 bot.send_message(message.chat.id,
#                                  'Please choose \'GET\' to try again, \'POST\', \'GET\', \'UPDATE\' or \'DELETE\'.')
#
#                 bot.register_next_step_handler(message, choice_log_postget)
#
#     except Exception as e:
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
#
# # Function to make a request GET in JSON and get data
# def log_in(message, **kwargs):
#     try:
#         user_pass = message.text
#         login = kwargs.get('login')
#
#         if login in user_data_dict and 'password' in user_data_dict[login] and user_pass == user_data_dict[login]['password']:
#
#             user_data = user_data_dict[login]
#             # Display user information
#             format_data = format_user_data(user_data)
#             # format_data = format_user_data(user_data)
#
#             # url_post = 'http://127.0.0.1:5000/json-example'
#             # post_response_json = response.post.json()
#
#             # r = requests.get(url_post, json=user_data)
#             # print(r.json)
#             # print(r.status_code)
#
#             bot.send_message(message.chat.id, f"Here's {login}'s data:\n\n{format_data}")
#             bot.send_message(message.chat.id,
#                              f'If you want to continue working on our base, write POST or GET or UPDATE or DELETE')
#             bot.register_next_step_handler(message, choice_log_postget)
#
#         else:
#
#             bot.send_message(message.chat.id,
#                              f"Password incorrect. Please, try again to write the password for {login}")
#             bot.register_next_step_handler(message, log_in, login=login)
#
#     except Exception as e:
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
#
#
# # Function to make a request POST in JSON and save data
# def log_post(message):
#     login = message.text.lower()
#
#     try:
#
#         print(f"DEBUG: log_post - login: {login}")
#
#         if login != r'✅':
#
#             if login in user_data_dict:
#                 #     and login in user_data_dict[user_id]):
#
#                 bot.send_message(message.chat.id, "Login already exists. Please choose 'POST, GET, UPDATE, DELETE' "
#                                                   "to continue working with data.")
#                 bot.register_next_step_handler(message, choice_log_postget)
#
#             else:
#                 # Initialize a new user entry
#                 user_data_dict[login] = {'login': login}
#
#                 bot.send_message(message.chat.id,
#                                  f"Great! Your login is {login}\n\n Please, write your new password for {login}")
#                 bot.register_next_step_handler(message, post_pass, login=login, pattern=pattern1)
#
#                 # return login
#
#
#         else:
#
#             username = message.from_user.username
#             login = username
#
#             if login in user_data_dict:
#                 #     and login in user_data_dict[user_id]):
#
#                 bot.send_message(message.chat.id, "Login already exists. Please choose 'POST, GET, UPDATE, DELETE' "
#                                                   "to continue working with data.")
#                 bot.register_next_step_handler(message, choice_log_postget)
#
#             else:
#
#                 username = message.from_user.username
#                 login = username
#                 user_data_dict[login] = {'login': login}
#
#                 bot.send_message(message.chat.id,
#                                  f"Great! Your login is {login}\n\n Please, write your new password for {login}")
#                 bot.register_next_step_handler(message, post_pass, login=login, pattern=pattern1)
#
#                 # return login
#
#     except Exception as e:
#         print(f"DEBUG: log_post - login: {login}")
#
#         # print(f"DEBUG: log_post - Exception: {e}")
#
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET" or "UPDATE" or "DELETE" ')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def validate_by_regexp(password, pattern):
#     """Валидация пароля по регулярному выражению."""
#     if re.match(pattern, password) is None:
#         raise ValidationError('Password has incorrect format.')
#
# def post_pass(message, pattern, **kwargs):
#     global login
#     try:
#         user_pass = message.text
#         login = kwargs.get('login')
#
#         if re.match(pattern, user_pass) is None:
#             raise ValidationError('Password has incorrect format.')
#
#         # Use validate_by_regexp function instead of re.match directly
#         validate_by_regexp(user_pass, pattern)
#
#         # Use assert without 'is None', and remove unnecessary with pytest.raises block
#         assert validate_by_regexp(user_pass, pattern) is None
#
#         user_data_dict[login]['password'] = user_pass
#
#         bot.send_message(message.chat.id,
#                          f"Great! Now your password is {user_pass}\n\n Let's start with your personal "
#                          f"data")
#         bot.send_message(message.chat.id, f"Write your first name:")
#
#         bot.register_next_step_handler(message, post_first, login=login)
#
#     except ValidationError as e:
#
#         bot.send_message(message.chat.id, f'ERROR: {e}')
#         bot.send_message(message.chat.id, 'Please, try to write another password')
#         # Pass the pattern argument to post_pass when re-registering the handler
#         bot.register_next_step_handler(message, post_pass, login=login, pattern=pattern1)
#
#     except Exception as e:
#
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, 'Please, choose again: "POST" or "GET"')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def post_first(message, **kwargs):
#     try:
#
#         first_name = message.text
#         login = kwargs.get('login')
#
#         # print(f"DEBUG: post_first - login: {login}")
#
#         user_data_dict[login]['first_name'] = first_name
#
#         bot.send_message(message.chat.id, f'Great! Now your first name is {first_name.title()}\n\n Please, write your '
#                                           f'last_name')
#
#         bot.register_next_step_handler(message, post_last, login=login)
#
#     except Exception as e:
#         # print(f"DEBUG: post_first - Exception: {e}")
#
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def post_last(message, **kwargs):
#     try:
#
#         last_name = message.text
#
#         login = kwargs.get('login')
#
#         user_data_dict[login]['last_name'] = last_name
#
#         bot.send_message(message.chat.id, f'Great! Now your last name is {last_name.title()}\n\n Please, let us '
#                                           f'know your address, write your country')
#
#         bot.register_next_step_handler(message, post_country, login=login)
#
#     except Exception as e:
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def post_country(message, **kwargs):
#     try:
#
#         login = kwargs.get('login')
#
#         country = message.text.lower()
#
#         user_data_dict[login]['country'] = message.text
#
#         bot.send_message(message.chat.id,
#                          f"Great! Now your country is {country.title()}\n\n Please, let us know your "
#                          f"city, write the name of your city")
#         bot.register_next_step_handler(message, post_city, login=login)
#
#         return country
#
#     except Exception as e:
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def post_city(message, **kwargs):
#     try:
#
#         login = kwargs.get('login')
#         city = message.text.lower()
#         user_data_dict[login]['city'] = message.text
#
#         bot.send_message(message.chat.id,
#                          f"Great! Now your city is {city.title()}\n\n Please, let us know your street "
#                          f"and house number, write your street and house number")
#         bot.register_next_step_handler(message, post_address, login=login)
#
#         return city
#
#     except Exception as e:
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def post_address(message, **kwargs):
#     try:
#
#         address = message.text.lower()
#         login = kwargs.get('login')
#
#         # user_data_dict.setdefault(login, {})
#         user_data_dict[login]['address'] = message.text
#
#         # streetaddress.capitalize()
#         bot.send_message(message.chat.id,
#                          f"Great! Now your street and house number is {address.title()}\n"
#                          f"Please, let us memorize your post code, write it")
#
#         bot.register_next_step_handler(message, post_index, login=login)
#
#         return address
#
#     except Exception as e:
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def post_index(message, **kwargs):
#     try:
#
#         login = kwargs.get('login')
#
#         index = message.text.lower()
#
#         user_data_dict.setdefault(login, {})
#         user_data_dict[login]['post_code'] = message.text
#
#         bot.send_message(message.chat.id,
#                          f"Great! Your post code is  {index.title()}\n\n Now let us know your email address, please "
#                          f"write it")
#         bot.register_next_step_handler(message, post_email, login=login)
#
#     except Exception as e:
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def post_email(message, **kwargs):
#     try:
#
#         login = kwargs.get('login')
#
#         email_address = message.text.lower()
#
#         user_data_dict[login]['email_address'] = message.text
#
#         bot.send_message(message.chat.id,
#                          f'Great! Your email is {email_address}\n\n Now let us know your phone number, please write it')
#         bot.register_next_step_handler(message, post_phone, login=login)
#
#     except Exception as e:
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
# def post_phone(message, **kwargs):
#     try:
#
#         login = kwargs.get('login')
#
#         phone_number = message.text.lower()
#
#         user_data_dict.setdefault(login, {})
#
#         user_data = user_data_dict[login]['phone_number'] = message.text
#
#         with open('user_data.json', 'w') as file:
#             json.dump(user_data_dict, file)
#
#         url_post1 = 'http://127.0.0.1:5000/save_users'
#         url_post = 'http://127.0.0.1:5000/json-example'
#         # post_response_json = response.post.json()
#
#         r = requests.post(url_post, json=user_data_dict)
#         print(r.json)
#         print(r.status_code)
#
#         # bot.send_message(chat_id, "Data successfully saved!")
#
#         bot.send_message(message.chat.id,
#                          f'Great! Your phone number is {phone_number}\n\nData successfully saved!')
#         bot.send_message(message.chat.id, f"Choose again, POST or GET to continue.")
#         bot.register_next_step_handler(message, choice_log_postget)
#
#
#     except Exception as e:
#
#         bot.reply_to(message, f'ERROR: {e}')
#         bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
#         bot.register_next_step_handler(message, choice_log_postget)
#
#     # 1
#
#
#
# def format_user_data(user_data):
#     try:
#
#         if isinstance(user_data_dict, dict) and user_data_dict:
#
#             login = user_data['login']
#
#             data = (f'\n\n'
#                     f'Login: {login}\n\n'
#                     f'1. First Name: {user_data["first_name"]}\n'
#                     f'2. Last Name: {user_data["last_name"]}\n'
#                     f'3. Country: {user_data["country"]}\n'
#                     f'4. City: {user_data["city"]}\n'
#                     f'5. Address: {user_data["address"]}\n'
#                     f'6. Post Code: {user_data["post_code"]}\n'
#                     f'7. Email: {user_data["email_address"]}\n'
#                     f'8. Phone Number: {user_data["phone_number"]}')
#
#             # bot.send_message(message.chat.id, f'If you want to continue working on the database, write /start again')
#             return data
#
#         else:
#             return "User data not found or invalid."
#
#     except Exception as e:
#         return f"Error formatting user data: {e}"
#
#
# # 2 (not used)
# def format_update_data(user_data):
#     try:
#
#         if isinstance(user_data_dict, dict) and user_data_dict:
#
#             login = user_data['login']
#
#             data = (f'Here\'s your new data:\n'
#                     f'1. Login: {login}\n'
#                     f'2. First Name: {user_data["first_name"]}\n'
#                     f'3. Last Name: {user_data["last_name"]}\n'
#                     f'4. Country: {user_data["country"]}\n'
#                     f'5. City: {user_data["city"]}\n'
#                     f'6. Address: {user_data["address"]}\n'
#                     f'7. Post Code: {user_data["post_code"]}\n'
#                     f'8. Email: {user_data["email_address"]}\n'
#                     f'9. Phone Number: {user_data["phone_number"]}')
#
#             return data
#         else:
#             return "User data not found or invalid."
#
#     except Exception as e:
#         return f"Error formatting user data: {e}"
#
#
# bot.infinity_polling()
