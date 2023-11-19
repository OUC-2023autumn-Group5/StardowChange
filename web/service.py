from flask import Flask
from gevent import pywsgi

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    #返回报文
    return 'Hello World!'
 
if __name__ == '__main__':
    app.run()
