from flask import Flask, jsonify
from Controller.IgController import process_instagram_profile, process_instagram_story, process_instagram_media

app = Flask(__name__)

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
      'type_route': {
        '/profile': 'USERNAME',
        '/story': 'USERNAME',
        '/media': 'to use this api, you just add base_url + url'
        },
      'z_note': None
    }]
  }

@app.route('/profile/<username>')
def get_instagram_profile(username):
  result = process_instagram_profile(username)
  return jsonify(result)

@app.route('/story/<username>')
def get_instagram_praofile(username):
  result = process_instagram_story(username)
  return jsonify(result)

@app.route('/media', methods=['GET'])
def get_instagram_media():
    result = process_instagram_media()
    return jsonify(result)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
