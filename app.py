from flask import Flask, render_template, jsonify
from config import config
from extensions import socketio
from routes import bp
from extensions import celery

app = Flask(__name__)
app.config['CELERY_RESULT_BACKEND'] = config['celery']['result_backend']
app.config['BROKER_URL'] = config['celery']['broker_url']

# install blueprints
app.register_blueprint(bp)

# install apps
socketio.init_app(app)

def main():
    app.run(host='localhost', port=3030, debug=True)

if __name__ == '__main__':
    main()