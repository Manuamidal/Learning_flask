from flask import Flask,request,make_response

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    response=make_response('hello_world')
    response.status_code=200
    response.headers['Custom-Header']='HelloWorld'
    return response

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f"<h1>{num1} + {num2} = {num1+num2}</h1>"

@app.route('/handle_url_param')
def handle_url_param():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting=request.args["greeting"]
        name=request.args["name"]
        return f"<h1>{greeting}, {name}!</h1>"
    else:
        return "<h1>Missing URL Parameters!</h1>"
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)