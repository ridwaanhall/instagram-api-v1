from flask import Flask, jsonify
from Controller.IgController import process_instagram_profile, process_instagram_story, process_instagram_media

app = Flask(__name__)

@app.route('/')
def home():
  return {
    'how_to_use': [{
      'text': 'you can use this API from link in routes_available.'
    }],
    'owner': [{
      'name': 'ridwaanhall',
      'address': 'N/A',
      'my_love': 'Afida'
    }],
    'social_media': [{
      'instagram': 'https://www.instagram.com/ridwaanhall',
      'facebook': 'https://www.facebook.com/ridwaanhall',
      'tiktok': 'https://www.tiktok.com/@ridwaanhall',
      'twitter': 'https://twitter.com/ridwaanhall',
      'threads': 'https://www.threads.net/@ridwaanhall',
      'linkedin': 'https://www.linkedin.com/in/ridwaanhall',
      'github': 'https://github.com/ridwaanhall',
      'replit': 'https://replit.com/@ridwaanhall',
      'telegram': 'https://t.me/ridwaanhall'
    }],
    'routes_available': [{
      'url_base':
      'https://instagram-api-v1.ridwaanhall.repl.co',
      'route':
      '/profile/<username>',
      'z_note':
      'this for check instagram user and download profile picture. change <username> to username you need. will show response profile : biography, count_followers, count_following, count_post, full_name, id, is_private, profile_full_HD, profile_img, username.'
    },
    {
      'url_base':
      'https://instagram-api-v1.ridwaanhall.repl.co',
      'route':
      '/story/<username>',
      'z_note':
      'this for check story and download story. change <username> to username you need. will show response highlight : id, thubmnail, title. playlist : height, id, is_video, src, thumbnail, width.'
    }, {
      'url_base':
      'https://instagram-api-v1.ridwaanhall.repl.co',
      'route':
      '/media',
      'z_note':
      'in development stage. for download reels, posts, videos, photos.'
    }],
    'source':
    'save-free'
  }

@app.route('/profile/<username>')
def get_instagram_profile(username):
  result = process_instagram_profile(username)
  return jsonify(result)

@app.route('/story/<username>')
def get_instagram_praofile(username):
  result = process_instagram_story(username)
  return jsonify(result)

@app.route('/media/<path:media_url>', methods=['GET'])
def get_instagram_media(media_url):
    result = process_instagram_media(media_url)
    return jsonify(result)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
