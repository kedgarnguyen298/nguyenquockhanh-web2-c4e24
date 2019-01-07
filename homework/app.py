from flask import Flask, render_template, redirect, request
import mlab
from mongoengine import Document, StringField, IntField, EmailField

app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        mlab.connect()

        class User(Document):
            fullname = StringField()
            email = EmailField()
            username = StringField()
            password = StringField() 
        
        user = User(
            fullname = request.form["fullname"],
            email = request.form["mail"],
            username = request.form["username"],
            password = request.form["psw"]
        )

        user.save()
        return "Wellcome"


if __name__ == '__main__':
  app.run(debug=True)