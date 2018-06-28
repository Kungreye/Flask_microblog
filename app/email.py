from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail


def send_async_email(app, msg):
    with app.app_context():     # application context, request context.
        mail.send(msg)



def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()

"""
Because current_app is really a proxy object, dynamically mapped to the application instance. 
So passing the proxy object would be the same as using current_app directly in the thread. 
We want to access the real application instance stored inside the proxy object, and pass that as the app argument. 
Use current_app._get_current_object() to extract the actual application instance from inside the proxy object, 
and then pass it to the thread as argument.
"""