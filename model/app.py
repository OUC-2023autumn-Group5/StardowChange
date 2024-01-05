from flask_cors import CORS
from flask import request
from flask import Flask,send_file
import os
import sys
sys.path.append("../")
from test import predict

app = Flask(__name__)
cors = CORS(app)

# 临时文件路径
img1 = 'tmp/before.bmp'
img2 = 'tmp/after.bmp'
path = 'tmp/result.png'

# No such directory处理
def mkdir(dir):
    if(not os.path.exists(dir)):
        os.mkdir(dir)

@app.route('/')
def hello_world():
    return 'This is a white page!'

@app.route("/upload1", methods=['post', 'get'])
def upload1():
    # 暂存上传的before.bmp文件
    f = request.files['file']
    print(f.filename)
    f.save(img1)
    print('success')
    return 'success'

@app.route("/upload2", methods=['post', 'get'])
def upload2():
    # 暂存上传的after.bmp文件
    f = request.files['file']
    print(f.filename)
    f.save(img2)
    print('success')
    return 'success'

@app.route("/work", methods=['post','get'])
def work():
    if request.method == 'POST':
        # 调用模型开始分析
        predict(img1, img2, "net-8.pt", path)
    elif request.method == 'GET':
        print('success')
    # 返回 BMP 图片
    return send_file(path, mimetype='image/png')
    # return 'success'

if __name__ == '__main__':
    mkdir('tmp')
    app.run()