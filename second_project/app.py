from flask import Flask,render_template,redirect,url_for

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    miylist=[1,2,3,4,5]
    return render_template('index.html',mylist=miylist)
@app.route('/other')
def other():
    word='Hello World'
    return render_template('other.html',word=word)

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.template_filter('repeat')
def  repeat(s,time=2):
        return s*time

@app.route('/redirect_home')
def redirect_home():
     return redirect(url_for('index'))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)