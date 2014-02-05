#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mc185104
#
# Created:     10/01/2014
# Copyright:   (c) mc185104 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import web
from loginmodel import LoginModel
from base import render, logged, session
import hashlib

model = LoginModel()

class Login:

    #vuser_req = form.Validator("Username not provided.", bool)
    #vpass_req = form.Validator("Password not provided.", bool)
    #vuser_exist = form.Validator("Username doesn't exist.", lambda u: u is None or model.get_user(u.username.strip()) is not None)
    #vpass_exist = form.Validator("Password didn't match", lambda i: hashlib.sha1("sAlT754-"+i.password).hexdigest() == model.get_user(i.username.strip())['pwd'])

    #login_form = form.Form(
    #    form.Textbox("username", description="Username"),
    #    form.Password("password", description="Password"),
    #    form.Button("Submit", type="submit", description="Login"),
    #    validators = [vuser_exist, vpass_exist],
    #    )
    def GET(self):
        """Login page"""
        #f = self.login_form()
        if not logged():
            return render.login("")
        else:
            raise web.seeother('/')

    def POST(self):

        #f = self.login_form()
        f = web.input()
        error_msg = "Incorrect username and password!"
        if not self.authenticate():
            return render.login(error_msg)
        else:
            session.login = model.get_user(f.username.strip())['id']
            if f.username.strip() == "admin":
                session.privilege = 1
            else:
                session.privilege = 0
            session.user = f.username.strip()
            raise web.seeother('/')

    def authenticate(self):
        f = web.input()
        usr = model.get_user(f.username.strip())
        if usr is None:
            return False
        elif usr['pwd'] != hashlib.sha1("sAlT754-"+f.password).hexdigest():
            return False
        else:
            return True
