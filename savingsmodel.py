#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mc185104
#
# Created:     01/27/2014
# Copyright:   (c) mc185104 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime
from model import Model

class SavingsModel:

    db = Model().getDB()
    def get_allsavings(self):
        return

    def get_guidelines(self):
        return

    def get_loans(self):
        return self.db.select(['loans', 'customers'], where='loans.customerid=customers.id', order='loans.id DESC')

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


