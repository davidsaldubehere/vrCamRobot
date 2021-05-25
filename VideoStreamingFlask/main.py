
from flask import Flask, render_template, Response, redirect, url_for, request
app = Flask(__name__)
import time
import explorerhat
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move',methods = ['POST', 'GET'])
def move():
    left = request.json['left']
    right = request.json['right']
    if left == "true" and right == "true":
        explorerhat.motor.forwards(100)
    elif left == "true":
        explorerhat.motor.two.forwards(50)
        time.sleep(1)
        explorerhat.motor.forwards(100)
    elif right == "true":
        explorerhat.motor.one.forwards(50)
        time.sleep(1)
        explorerhat.motor.forwards(100)
    else:
        explorerhat.motor.forwards(0)
    
    return "moving"




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, ssl_context=('cert.pem', 'key.pem'))
