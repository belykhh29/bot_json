from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('user_data.json', 'r') as file:
        user_data = json.load(file)

    return render_template('user_table.html', user_data=user_data.values())

if __name__ == '__main__':
    app.run(debug=True)
