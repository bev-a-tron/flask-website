from flask import Flask,render_template,request

app = Flask(__name__)

app.progvars={}
app.num_clips=5

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
