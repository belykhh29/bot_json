# Telegram User Database Bot

## Overview

THIS IS TECHNICAL TASK, INTO PORTFOLIO

This Telegram bot serves as a simple user database manager, allowing users to store, retrieve, update, and delete their personal information in a persistent storage (in this case, a JSON file).

## Features

1. **User Data Management:**
   - **POST:** Add new user data to the database.
   - **GET:** Retrieve existing user data.
   - **UPDATE:** Modify and update user information.
   - **DELETE:** Delete user data.

2. **User Interaction:**
   - The bot communicates with users via Telegram messages.
   - Users can interact with the bot by providing textual information.

3. **Persistent Storage:**
   - User data is stored in a JSON file (`user_data.json`), ensuring persistence across bot restarts.

## How to Use

1. **Start the Bot:**
   - Start a chat with the bot on Telegram.
   - Send the command `/start` to initiate the interaction.

2. **User Data Operations:**
   - Use commands like `POST`, `GET`, `UPDATE`, and `DELETE` to manage user data.
   - Follow the bot's prompts to provide the necessary information.

3. **Data Retrieval:**
   - Use the `GET` command to retrieve stored user data.
   - Provide the login information when prompted.

4. **Data Update:**
   - Use the `UPDATE` command to modify existing user data.
   - Follow the bot's prompts to update specific fields.

5. **Data Deletion:**
   - Use the `DELETE` command to remove user data.
   - Confirm the deletion when prompted.

6. **Persistent Storage:**
   - User data is stored in the `user_data.json` file.
   - This file is updated in real-time as users interact with the bot.

## Example Usage

1. **POST:**
   - Send the command `POST` to add new user data.
   - Follow the prompts to provide information like first name, last name, etc.

2. **GET:**
   - Send the command `GET` to retrieve stored user data.
   - Provide the login information when prompted.

3. **UPDATE:**
   - Send the command `UPDATE` to modify existing user data.
   - Follow the prompts to update specific fields.

4. **DELETE:**
   - Send the command `DELETE` to remove user data.
   - Confirm the deletion when prompted.

## Requirements

- Python 3.10
- Python-Telegram-Bot library (`pyTelegramBotAPI`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/belykhh29/bot_json.git
