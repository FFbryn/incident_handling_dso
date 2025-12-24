from flask import Flask, request
import logging
import time

app = Flask(__name__)
logging.basicConfig(
    filename='app.log',
    level=logging.WARNING,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/')
def index():
    return "Incident Handling Demo App is Running"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return "Login endpoint ready. Use POST method to authenticate."
    password = request.form.get('password')

    if password != 'admin123':
        app.logger.warning(
            "Failed login attempt from IP %s",
            request.remote_addr
        )
        time.sleep(2)  # simple rate limiting
        return "Login Failed", 401
    return "Login Success", 200

if __name__ == '__main__':
    app.run(host='10.10.93.47', port=5000)
