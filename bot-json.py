import telebot
import json

bot = telebot.TeleBot('6370996369:AAEqn8epM8aKiMM9zzAEHYSjOkz0K_PU5nE')

#Create
user_data_dict = {}

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

@bot.message_handler(commands=['START, start'])
def welcome(message):
    message_user = message.text
    user_m_list = ['START', 'start']

    if message_user in user_m_list:

        bot.send_message(message.chat.id,
                         "Hello! We would love to register you into our base if you're not registered")

        choice_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        l_button = telebot.types.KeyboardButton("POST")
        s_button = telebot.types.KeyboardButton("GET")

        choice_markup.row(l_button, s_button)
        bot.send_message(message.chat.id, "Please, choose the action:", reply_markup=choice_markup)

        bot.register_next_step_handler(message, choice_log_postget)

    else:

        welcome_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        start_button = telebot.types.KeyboardButton("START")
        welcome_markup.row(start_button)

        w_answer = 'Nah, you must be wrong! Press the button  "START" to continue'
        bot.send_message(message.chat.id, w_answer, reply_markup=welcome_markup)
        bot.register_next_step_handler(message, welcome)


@bot.message_handler(commands=["POST", "GET", 'post', 'get'])
def choice_log_postget(message):
    users_choice = message.text
    users_choice_list1 = ['POST', 'post']
    users_choice_list = ['GET', 'get']

    if users_choice in users_choice_list:

        give_loginid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        giveloginid_button = telebot.types.KeyboardButton(r'Give permit to take my ID')

        give_loginid_markup.row(giveloginid_button)

        # l_answer = f"Okay! Then give us permit to take your ID:"
        # bot.send_message(message.chat.id, l_answer, reply_markup=give_loginid_markup)
        bot.send_message(message.chat.id, f'Write a login for get data')

        bot.register_next_step_handler(message, log_in)

    elif users_choice in users_choice_list1:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesignuplid_button = telebot.types.KeyboardButton(r'Give my ID as a login')

        give_signupid_markup.row(givesignuplid_button)

        bot.send_message(message.chat.id, f'Write new login for data')
        # s_answer = f"Great! For the first, we need to get your Telegram ID to start registering"
        # bot.send_message(message.chat.id, s_answer, reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, log_post)

    else:
        
        bot.send_message(message.chat.id, 'ERROR: Invalid choice')
        bot.send_message(message.chat.id, 'Please, write again POST or GET')
        bot.register_next_step_handler(message, choice_log_postget)

def log_in(message):
    try:
        
        login_choice = message.text
        
        if login_choice in user_data_dict:
            
            user_data = user_data_dict[login_choice]
            # Display user information
            format_data = format_user_data(user_data, message)
            
            bot.send_message(message.chat.id, f"\n{format_data}")
            bot.send_message(message.chat.id, f'If you want to continue working on the database, choose "POST or "GET"')

            bot.register_next_step_handler(message, choice_log_postget)
            
        else:
            
            bot.send_message(message.chat.id,
                             "Login not found. Please choose 'GET' to try again or 'POST' to enter your "
                             "information.")
            bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:
        
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def log_post(message):
    try:
        
        login = message.text.lower()
        #print(f"DEBUG: log_post - login: {login}")

        if login in user_data_dict:
        # and login in user_data_dict[user_id]):

            bot.send_message(message.chat.id,
                             "Login already exists. Please choose 'Login' to view or update your information.")
            bot.register_next_step_handler(message, choice_log_postget)

        else:
            
            # Initialize a new user entry
            user_data_dict[login] = {'login': login}

            bot.send_message(message.chat.id,
                             f"Great! Your login is {login}\n\n Please, let us know your first name, write it to me")
            bot.register_next_step_handler(message, post_first, login=login)

            return login

    except Exception as e:
        
        #print(f"DEBUG: log_post - Exception: {e}")
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_first(message, **kwargs):
    try:
        
        first_name = message.text
        login = kwargs.get('login')
        user_data_dict[login]['first_name'] = first_name
        # print(f"DEBUG: post_first - login: {login}")

        bot.send_message(message.chat.id, f'Great! Now your first name is {first_name.title()}\n\n Please, let us know '
                                          f'your last name, write it to me')
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
                         f"Great! Now your street and house number is {address.tit} Please, let us memorize your post "
                         f"code, write it")
        bot.register_next_step_handler(message, post_index, login=login)

        return address

    except Exception as e:
        
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def post_index(message, **kwargs):
    try:

        login = kwargs.get('login')
        # country = kwargs.get('country')
        # city = kwarg.get('city')
        # address = kwargs.get('address')

        index = message.text.lower()

        user_data_dict.setdefault(login, {})
        user_data_dict[login]['post_code'] = message.text

        # bot.send_message(chat_id, f"Great! Your full address is {country.title()}, {city.title()},\n{address.title(
        # )}, {index.title()}\n\n Now let us know your email address, please " f"write it")

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
        user_data_dict.setdefault(login, {})
        user_data_dict[login]['phone_number'] = message.text

        with open('user_data.json', 'w') as file:
            json.dump(user_data_dict, file)

        # bot.send_message(chat_id, "Data successfully saved!")

        bot.send_message(message.chat.id,
                         f'Great! Your phone number is {phone_number}\n\nData successfully saved!')
        bot.send_messagea(message.chat.id, f"Choose again, POST or GET to continue.")
        bot.register_next_step_handler(message, choice_log_postget)

        # return choice_log_postget
        # bot.register_message_handler(message, choice_log_POSTGET)
        # bot.register_next_step_handler(message, post_email)

    except Exception as e:

        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)

def format_user_data(user_data, message):
    try:

        if isinstance(user_data_dict, dict) and user_data_dict:
            login = user_data['login']

            data = (f'Here\'s your data:\n\n'
                    f'Login: {login}\n'
                    f'First Name: {user_data["first_name"]}\n'
                    f'Last Name: {user_data["last_name"]}\n'
                    f'Country: {user_data["country"]}\n'
                    f'City: {user_data["city"]}\n'
                    f'Address: {user_data["address"]}\n'
                    f'Post Code: {user_data["post_code"]}\n'
                    f'Email: {user_data["email_address"]}\n'
                    f'Phone Number: {user_data["phone_number"]}')
            
            # bot.register_next_step_handler(message, choice_log_postget)

            return data
        
        else:
        
            return "User data not found or invalid."
            
    except Exception as e:
        
        return f"Error formatting user data: {e}"


bot.infinity_polling()
