from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print request.headers

    resp = make_response('ok', 200)
    resp.headers['Access-Control-Allow-Origin'] =  'http://m.zhutao.xyz'
    resp.headers['Access-Control-Allow-Credentials'] =  'true'
    resp.set_cookie('wechat', 'wechat')

    #return 'Hello, World!'
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
