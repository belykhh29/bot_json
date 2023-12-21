# import requests
#
#
# with open('user_data_test2.json') as inputfile:
#     json_file = inputfile.read()
#
# response = requests.post('http://93.95.97.207/users', data=json_file)
# # response = requests.post('http://127.0.0.1:5000', data = {'login':{}})
#
#
# print(response.text)

import json
from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__)


@app.route('/json-example', methods=['POST', 'GET'])
def json_example():
    try:

        if request.method == 'POST':

            data = request.get_json()  # Get JSON data from the request
            with open('kek.json', 'w') as file:
                json.dump(data, file)  # Write JSON data to 'kek.json'

            return jsonify({"message": "Data successfully saved!"})

        else:

            data = request.get_json()
            with open('kek.json', 'w') as file:
                json.dump(data, file)  # Write JSON data to 'kek.json'

            return jsonify(f'{data}')

    except Exception as e:

        return jsonify({"error": str(e)}), 500


# @app.route('/json-example1', methods=['POST'])
# def json_example():
#    kek = {}
#
#    with open('kek.json', 'w') as file:
#       json.dump(kek, file)
#
#    return 'JSON Object Example'


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)



