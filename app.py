from flask import Flask
import time

app = Flask(__name__)


@app.route('/wait')
def wait():
    time.sleep(10)
    return {'Response': 'waited for 10 seconds'}
@app.route('/instant')
def instant():
    return {'Response': 'instant response'}


if __name__ == '__main__':
    app.run(threaded=True)