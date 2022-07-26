from models import Contact, Email, Phone

def get_users():
    return Contact.objects.all()

def add_user(name, email='', phone=''):
    new_email = Email()
    new_email.value = email
    new_phone = Phone()
    new_phone.value = phone
    Contact(name=name, email=new_email, phone=new_phone).save()

def delete_user(id):
    Contact.objects(id=id).delete()

def find_contact(id):
    return Contact.objects(id=id)

def edit_user(id, phone, email, name):
    new_email = Email()
    new_email.value = email
    new_phone = Phone()
    new_phone.value = phone
    Contact.objects(id=id).update(name=name,  email=new_email, phone=new_phone)