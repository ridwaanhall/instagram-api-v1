from flask import Flask, request, jsonify
import requests
import json
from Controller.IgController import process_instagram_profile

app = Flask(__name__)

# Your function to make the API request and process the response

# Define the route to handle requests with a username parameter.
@app.route('/')
def home():
  return {
    'how_to_use': [{
      'text': 'you can use this API from link in route_api.'
    }],
    'owner': [{
      'name': 'ridwaanhall',
      'address': 'Sleman, DIY',
      'my_love': 'Afida'
    }],
    'route_api': [{
      'base_url': 'https://instagram-api.ridwaanhall.repl.co/',
      'url': 'YOUR USERNAME',
      'z_note': 'to use this api, you just add base_url + url'
    }]
  }

@app.route('/<username>')
def get_instagram_profile(username):
    result = process_instagram_profile(username)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
