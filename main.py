
from flask import Flask,render_template
 
# Creating flask app, also other folders that are in use 
app = Flask(__name__,
            template_folder = "pages"  # HTML pages
            )
 
# The first page that loads --> 
@app.route('/')
def Homepage():
    return render_template('homepage.html','styles.css')



if __name__ == "__main__":
    app.run()