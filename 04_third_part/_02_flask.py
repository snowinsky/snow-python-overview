from flask import Flask
from markupsafe import escape
from flask import request

## https://flask.palletsprojects.com/en/3.0.x/quickstart/
## 官方文档的几个例子居然可以跑，还是外国人靠谱

app = Flask(__name__)

## get 返回html string
@app.route('/', methods=['GET'])
def index():
    return '''
        <form method="post" action="/login">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
    
## get方法带path参数
@app.route('/hello/<username>', methods=['GET'])
def hello(username):
    return f'<h1>欢迎你，我的朋友</h1>: {escape(username)}'

## post方法，接收form中信息  
@app.route('/login', methods=['POST'])    
def login():
    username = request.form['username']
    print(username)
    if(username == 'ABC'):
        return hello(username)
    else:
        return '''
                    <h1>输入用户名不存在，请查证后再输入</h1>
                    <br>
                    <form method="post" action="/login">
                        <p><input type=text name=username>
                        <p><input type=submit value=Login>
                    </form>
                '''

## get方法返回json
@app.route('/notify', methods=['GET'])    
def notify(user='aaa'):
    print("get parameter from query", user)
    return {
        'username': user,
        'status':500,
        'notify': "ssssssssssssssssssss2444"
    }
      
## get方法带query parameter ？key=value
@app.route('/notifyUser', methods=['GET'])
def notifyUser():
    user = request.args.get('user')
    return {
        'username': user,
        'status':500,
        'notify': "ssssssssewert32436b4ysssss2444"
    }


## post方法接收json格式的数据
@app.route('/notify/info', methods=['POST'])
def notifyInfo():
    info = request.json
    print(info)
    return {'info': info}







if __name__ == '__main__':
    app.run()