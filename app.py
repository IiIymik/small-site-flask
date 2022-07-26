from flask import Flask, render_template, request, redirect
from flask import request
from models import Contact, Email, Phone
from helpers_func import add_user, get_users, delete_user, find_contact, edit_user
import random
import connect

app = Flask(__name__)
app.debug = True
app.env = "development"


@app.route("/", strict_slashes=False)
def index():

    return render_template("index.html", contacts=get_users())

@app.route("/contact", methods=['GET','POST'], strict_slashes=False)
def add_contact():
    if request.method == 'POST':
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        add_user(name=name,phone=phone,email=email)
        return redirect('/')
    else:
        return render_template("contact.html")

@app.route('/contact/<id>', methods=['GET','POST'], strict_slashes=False)        
def edit_contact(id):
    contact = find_contact(id)  
    if request.method == 'POST':
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        edit_user(id, phone=phone, email=email, name=name)
        return redirect('/')
    else:
        return render_template("contact.html", contact=contact)

@app.route('/delete/<id>',  strict_slashes=False)
def delete_contact(id):
    delete_user(id)
    return redirect('/')

if __name__ == "__main__":
    app.run()
