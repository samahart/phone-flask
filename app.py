from flask import Flask, send_file
import os
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

FILE_TYPES = ('.png', '.jpeg', '.jpg')
img_idx = -1
images_path = os.path.join('static', 'temp')
images = [os.path.join(images_path, img) for img in os.listdir(images_path) if img.endswith(FILE_TYPES) ]
images_len = len(images)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/picture', methods=['GET'])
def picture():
    global img_idx
    img_idx += 1
    img_idx = img_idx % images_len
    return send_file(images[img_idx])


if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(host='0.0.0.0', port=80)
