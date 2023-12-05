import telebot
import json

from bot_json_test import choice_log_postget, bot
from json_data import user_data_dict, format_user_data

# bot = telebot.TeleBot('6370996369:AAEqn8epM8aKiMM9zzAEHYSjOkz0K_PU5nE')


def new_or_id_get1(message):
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
            bot.register_next_step_handler(message, log_in)


        elif choice_user == 'write another login':
            bot.send_message(message.chat.id, 'Okay! Then write a login for get a data from our base')

            bot.register_next_step_handler(message, log_in)

        else:

            bot.send_message(message.chat.id, 'ERROR: Invalid choice')
            bot.send_message(message.chat.id, 'Please, choose the option again')
            bot.register_next_step_handler(message, new_or_id_get1)


    except Exception as e:
        return f"Error: {e}"

def log_in(message):
    try:
        login = message.text

        if login in user_data_dict:

            user_data = user_data_dict[login]
            # Display user information
            format_data = format_user_data(user_data)

            bot.send_message(message.chat.id, f"Here's {login}'s data:\n\n{format_data}")
            bot.send_message(message.chat.id,
                             f'If you want to continue working on our base, write POST or GET or UPDATE or DELETE')
            bot.register_next_step_handler(message, choice_log_postget)

        elif login == r"✅":

            username = message.from_user.username
            login = username

            if login in user_data_dict:

                user_data = user_data_dict[login]
                # Display user information
                format_data = format_user_data(user_data)
                bot.send_message(message.chat.id, f"Here's yours, {login}, data:{format_data}")
                bot.send_message(message.chat.id,
                                 f"If you want to continue working on our base, write POST or GET or UPDATE or DELETE")

                bot.register_next_step_handler(message, choice_log_postget)

            else:

                bot.send_message(message.chat.id, f"Login {login} wasn't found.")
                bot.send_message(message.chat.id, "Please choose 'GET' to try again, 'POST' to enter your "
                                 "information or 'UPDATE' to change information in login's base.")

                bot.register_next_step_handler(message, choice_log_postget)

        else:

            bot.send_message(message.chat.id,
                             f"Login {login} wasn't found. Please choose 'GET' to try again, 'POST' to enter your "
                             "information or 'UPDATE' to change information in login's base.")
            bot.register_next_step_handler(message, choice_log_postget)

    except Exception as e:
        bot.reply_to(message, f'ERROR: {e}')
        bot.send_message(message.chat.id, f'Please, choose again: “POST” or “GET')
        bot.register_next_step_handler(message, choice_log_postget)
