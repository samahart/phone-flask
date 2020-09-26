from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(host='0.0.0.0', port=80)
