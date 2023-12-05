import telebot
import json

from bot_json_test import choice_log_postget, bot
from json_data import user_data_dict, format_user_data


def new_or_id_post1(message):
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
            bot.register_next_step_handler(message, log_post)


        elif choice_user == 'write new login':
            bot.send_message(message.chat.id, 'Okay! Then write new login for add a data into our base')

            bot.register_next_step_handler(message, log_post)

        else:

            bot.send_message(message.chat.id, 'ERROR: Invalid choice')
            bot.send_message(message.chat.id, 'Please, choose the option again')
            bot.register_next_step_handler(message, new_or_id_post1)


    except Exception as e:
        return f"Error: {e}"

def log_post(message):
    try:

        login = message.text.lower()
        # print(f"DEBUG: log_post - login: {login}")

        if login in user_data_dict:
            #     and login in user_data_dict[user_id]):

            bot.send_message(message.chat.id,
                             "Login already exists. Please choose 'POST, GET, UPDATE, DELETE' to continue working with data.")
            bot.register_next_step_handler(message, choice_log_postget)

        elif login == r'✅':

            if login in user_data_dict:
                #     and login in user_data_dict[user_id]):

                bot.send_message(message.chat.id,
                                 "Login already exists. Please choose 'POST, GET, UPDATE, DELETE' to continue working with data.")
                bot.register_next_step_handler(message, choice_log_postget)

            else:

                username = message.from_user.username
                login = username
                user_data_dict[login] = {'login': login}

                bot.send_message(message.chat.id,
                                 f"Great! Your login is {login}\n Please, write the first name of user to continue")
                bot.register_next_step_handler(message, post_first, login=login)

                return login

        else:
            # Initialize a new user entry
            user_data_dict[login] = {'login': login}

            bot.send_message(message.chat.id,
                             f"Great! Your login is {login}\n\n Please, let us know your first name, write it to me")
            bot.register_next_step_handler(message, post_first, login=login)

            return login

    except Exception as e:

        # print(f"DEBUG: log_post - Exception: {e}")

        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET" or "UPDATE" or "DELETE" ')
        bot.register_next_step_handler(message, choice_log_postget)



def post_first(message, **kwargs):
    try:

        first_name = message.text
        login = kwargs.get('login')

        # print(f"DEBUG: post_first - login: {login}")

        user_data_dict[login]['first_name'] = first_name

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

        # login = log_post()
        # country = post_country()
        # city = post_city()
        # address = post_address()

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
        bot.send_message(message.chat.id, f"Choose again, POST or GET to continue.")
        bot.register_next_step_handler(message, choice_log_postget)

        # return choice_log_postget
        # bot.register_message_handler(message, choice_log_POSTGET)
        # bot.register_next_step_handler(message, post_email)

    except Exception as e:

        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)
