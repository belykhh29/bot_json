import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)



@app.route('/')
def index():
    with open('user_data.json', 'r') as file:
        user_data = json.load(file)

    return render_template('user_table.html', user_data=user_data.values())

@app.route('/users')
def get_users():
    try:
        with open('users2.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = {}

    return jsonify(data)

@app.route('/save_users')
def save_users():
    # Do something to get the data you want to save (e.g., data = {...})
    data = {'login': {}}  # Replace this with the actual data you want to save
    with open('users2.json', 'w') as file:
        json.dump(data, file)

    return "Data saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)

