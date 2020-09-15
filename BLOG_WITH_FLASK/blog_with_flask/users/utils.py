import os
import secrets
from PIL import Image
from flask import url_for, current_app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def save_picture(form_picture):
    random_hx=secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hx + f_ext
    picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    from_email = 'nicolasbahindwa@outlook.com'
    to_email = ([user.email]) 
    subject='Password'
    content =  f''' To reset your password, visit the following link
                {url_for ('users.reset_token', token=token, _external=True)}
                if you did not make this request please ignore the precess 
                '''
    
    mail = SendGridAPIClient(key)
    message = Mail(from_email,to_email,subject,content)
    response =mail.send(message)
