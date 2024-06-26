## 实现API， 并且演示 api 的 get , post , 以及其他的request里的param , query , body

# 创建Flask应用
from flask import Flask
app = Flask(__name__)

# 创建视图函数
@app.route('/')# 绑定url
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run()
