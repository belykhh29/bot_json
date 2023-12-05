import telebot
import json

from bot_json_test import choice_log_postget, bot
from json_data import user_data_dict, format_user_data

bot = telebot.TeleBot('6370996369:AAEqn8epM8aKiMM9zzAEHYSjOkz0K_PU5nE')


def new_or_id_del1(message):
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
            bot.register_next_step_handler(message, start_delete_process)


        elif choice_user == 'write another login':
            bot.send_message(message.chat.id, 'Okay! Then write a login to delete a data from our base')

            bot.register_next_step_handler(message, start_delete_process)

        else:

            bot.send_message(message.chat.id, 'ERROR: Invalid choice')
            bot.send_message(message.chat.id, 'Please, choose the option again')
            bot.register_next_step_handler(message, choice_log_postget)


    except Exception as e:
        return f"Error: {e}"



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
                                 "information or 'UPDATE' to change information in login's base or 'DELETE' to delete data")
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
                                                  "information or 'UPDATE' to change information in login's base or 'DELETE' to delete data")

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



def delete_user_data(message, **kwargs):
    try:
        login_to_delete = kwargs.get('login')

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

            bot.register_next_step_handler(message, choice_log_postget)


        elif users_choice == 'No':

            bot.send_message(message.chat.id, f'Okay! Let me know if you want to delete the data')
            bot.send_message(message.chat.id,
                             f"Please, write the \"POST\", \"GET\", \"UPDATE\" or \"DELETE\" to continue working with me")

            bot.register_next_step_handler(message, choice_log_postget)

        else:

            bot.send_message(message.chat.id, f'ERROR: Incorrect choice, please choose "Yes" or "No" to continue.')
            bot.send_message(message.chat.id, "Please try again or check the login.")

            bot.register_next_step_handler(message, start_delete_process)

    except Exception as e:

        bot.send_message(message.chat.id, f"ERROR: {e}")
        bot.send_message(message.chat.id, "Please, try again with commands: /start, POST, GET, UPDATE, DELETE")

        bot.register_next_step_handler(message, start_delete_process)
