
from flask_cors import CORS
from flask import request
from PIL import Image
from flask import render_template
from flask import Flask,send_file

import sys
sys.path.append("../")
from test import predict


 
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'
 
@app.route("/upload1", methods=['post', 'get'])
def upload1():

    f = request.files['file']
    print(f.filename)
    f.save('before.bmp')
    # # image_file = Image.open(f.filename)  # open colour image
    # # image_file = image_file.convert('1')  # convert image to black and white
    # # path = '../vue/star/public/result.png'//需要保存到的路径
    # # image_file.save(path)
    print('success')
    return 'success'

@app.route("/upload2", methods=['post', 'get'])
def upload2():

    f = request.files['file']
    print(f.filename)
    f.save('after.bmp')
    # # image_file = Image.open(f.filename)  # open colour image
    # # image_file = image_file.convert('1')  # convert image to black and white
    # # path = '../vue/star/public/result.png'//需要保存到的路径
    # # image_file.save(path)
    print('success')
    return 'success'

@app.route("/work", methods=['post', 'get'])
def work():
    path = './result.png'
    predict("before.bmp","after.bmp","net-6.pt",path)
    image_path = 'result.png'

    # 返回 BMP 图片
    return send_file(image_path, mimetype='image/png')
    # return 'success'

if __name__ == '__main__':
    app.run()