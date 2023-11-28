from flask import Flask
from flask_cors import CORS
from flask import request
from PIL import Image
from flask import render_template

 
app = Flask(__name__)
cors = CORS(app)



@app.route('/')
def hello_world():
    return 'Hello World!'
 
@app.route("/upload", methods=['post', 'get'])
def upload():

    f = request.files['file']
    print(f.filename)
    f.save(f.filename)
 
    # image_file = Image.open(f.filename)  # open colour image
    # image_file = image_file.convert('1')  # convert image to black and white
    # path = '../vue/star/public/result.png'//需要保存到的路径
    # image_file.save(path)
    #在这里调用模型的函数，还有点bug，上传的时候需要输入确定的文件名才能运行，这样的路径确定你也方便调用，
    #现在只能做到这了，并且初始model就要有两张确定的路径名在里面
    #并且之后上传的文件的名称都得是一对，这样才能得到结果
    #剩下的部分会在之后继续完善，一测前可能就只能这样了
    return 'success'


if __name__ == '__main__':
    app.run()