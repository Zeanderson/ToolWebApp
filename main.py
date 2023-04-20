from flask import Flask, render_template,request

app = Flask(__name__, 
            template_folder='templateFiles',  # HTML 
            static_folder='staticFiles' # CSS & Images 
            )
 
@app.route('/',)
def home():
    return render_template('home.html')
@app.route('/Login')
def login():
    return render_template('login.html')

 
if __name__=='__main__':
    app.run(debug = True)