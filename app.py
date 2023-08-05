from flask import Flask, request, jsonify
import requests
import json
from Controller.IgController import process_instagram_profile

app = Flask(__name__)

# Your function to make the API request and process the response

# Define the route to handle requests with a username parameter.
@app.route('/')
def home():
  return 'hello'

@app.route('/<username>')
def get_instagram_profile(username):
    result = process_instagram_profile(username)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
