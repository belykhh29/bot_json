import telebot
# import json

# from post_data import new_or_id_post1
# from get_data import new_or_id_get1
# from update_data import new_or_id_update1
# from delete_user import new_or_id_del1


bot = telebot.TeleBot('6370996369:AAEqn8epM8aKiMM9zzAEHYSjOkz0K_PU5nE')

# Load existing user data from JSON file
import time







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


@bot.message_handler(commands=["POST", "GET", 'post', 'get', 'DELETE', 'UPDATE', 'Delete', 'Update', 'delete', 'update', 'Post', 'Get'])
def choice_log_postget(message):
    users_choice = message.text

    users_choice_list = ['GET', 'get', 'Get']
    users_choice_list1 = ['POST', 'post', 'Post']
    user_choice_list2 = ['UPDATE', 'Update', 'update']
    user_choice_list3 = ['DELETE', 'Delete', 'delete']

    if users_choice in users_choice_list:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
        newlogin_button = telebot.types.KeyboardButton(r'Write another login')

        give_signupid_markup.row(givesid_button, newlogin_button)

        bot.send_message(message.chat.id, f'Choose the option how to get a data:', reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, new_or_id_get)

    elif users_choice in users_choice_list1:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
        newlogin_button = telebot.types.KeyboardButton(r'Write new login')

        give_signupid_markup.row(givesid_button, newlogin_button)

        bot.send_message(message.chat.id, f'Choose the option how to post a data into base:',
                         reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, new_or_id_post)

    elif users_choice in user_choice_list2:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
        newlogin_button = telebot.types.KeyboardButton(r'Write a users login')

        give_signupid_markup.row(givesid_button, newlogin_button)

        bot.send_message(message.chat.id, f'Choose the option how to update a data in our base:',
                         reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, new_or_id_update)

    elif users_choice in user_choice_list3:

        give_signupid_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        givesid_button = telebot.types.KeyboardButton(r'Take my ID as a login')
        newlogin_button = telebot.types.KeyboardButton(r'Write another login')

        give_signupid_markup.row(givesid_button, newlogin_button)

        bot.send_message(message.chat.id, f'Choose the option how to delete a data:',
                         reply_markup=give_signupid_markup)

        bot.register_next_step_handler(message, new_or_id_del)

    else:
        bot.send_message(message.chat.id, 'ERROR: Invalid choice')
        bot.send_message(message.chat.id, 'Please, write again POST or GET or UPDATE or DELETE')
        bot.register_next_step_handler(message, choice_log_postget)


def new_or_id_post(message):
    from post_data import new_or_id_post1


def new_or_id_get(message):
    from get_data import new_or_id_get1


def new_or_id_update(message):
    from update_data import new_or_id_update1

def new_or_id_del(message):
    from delete_user import new_or_id_del1

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


bot.infinity_polling(timeout=10)
# bot.infinity_polling()
while True:
    try:
        bot.infinity_polling()
    except telebot.apihelper.ApiTelegramException as e:
        if "Conflict" in str(e):
            # Подождите некоторое время и повторите попытку
            time.sleep(1)
        else:
            raise
