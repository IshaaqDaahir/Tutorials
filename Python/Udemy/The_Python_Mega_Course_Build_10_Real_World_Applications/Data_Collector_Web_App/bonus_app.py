from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:gd#$%hhjfds_hjff@localhost/height_collector'
db = SQLAlchemy(app)

app.app_context().push()

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("bonus_index.html")

@app.route("/success", methods=["POST"])
def success():
    global file
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename("uploaded" + file.filename))
        with open("uploaded" + file.filename, "a") as f:
            f.write("This was added later!")
        print(file)
        print(type(file))
        return render_template("bonus_index.html", btn="download.html")
    
@app.route("/download")
def download():
    return send_file("uploaded" + file.filename, download_name="yourfile.csv",
                     as_attachment=True)
    
if __name__ == "__main__":
    app.debug=True
    app.run()
