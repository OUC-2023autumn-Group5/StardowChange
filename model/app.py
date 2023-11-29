from flask import Flask
from flask_cors import CORS
from flask import request
from PIL import Image
from flask import render_template
import sys
sys.path.append("../")
from test import predict


 
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'
 
@app.route("/upload", methods=['post', 'get'])
def upload():

    f = request.files['file']
    print(f.filename)
    f.save('before.bmp')
    # image_file = Image.open(f.filename)  # open colour image
    # image_file = image_file.convert('1')  # convert image to black and white
    # path = '../vue/star/public/result.png'//需要保存到的路径
    # image_file.save(path)
    print('success')
    return 'success'

@app.route("/work", methods=['post', 'get'])
def work():
    f = request.files['file']
    print(f.filename)
    f.save('after.bmp')

    path = '../vue/star/public/result.png'
    predict("before.bmp","after.bmp","net-6.pt",path)
    # image_file = Image.open('before.jpg')
    # image_file = image_file.convert('1')  # convert image to black and white
    # path = '../vue/star/public/result.png' 保存路径
    # image_file.save(path)
    # 函数调用在这写,我用了两个端口分别上传文件，调用到这个端口时，已经将上传的文件重命名为了before.jpg和after.jpg名字你可以改，然后直接调用就行程序就会运行

    return 'success'

if __name__ == '__main__':
    app.run()