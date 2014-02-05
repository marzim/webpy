#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mc185104
#
# Created:     11/12/2013
# Copyright:   (c) mc185104 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime
from model import Model

class BlogModel:

    db = Model().getDB()
    def get_posts(self,id):
        try:
            return self.db.select('entries', where='userid='+ str(id), order='id DESC')
        except IndexError:
            return None

    def get_allposts(self):
        return self.db.select('entries', order='id DESC')

    def get_post(self,id,uid):
        try:
            return self.db.select('entries', where='id=$id and userid='+ str(uid), vars=locals())[0]
        except IndexError:
            return None

    def get_anonymouspost(self,id):
        try:
            return self.db.select('entries', where='id=$id', vars=locals())[0]
        except IndexError:
            return None

    def new_post(self,title, text, userid):
        self.db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow(), userid=userid)

    def del_post(self,id):
        self.db.delete('entries', where="id=$id", vars=locals())

    def update_post(self,id, title, text):
        self.db.update('entries', where="id=$id", vars=locals(), title=title, content=text)


