import web
from savingsmodel import SavingsModel
from customermodel import CustomerModel
from base import render,  withprivilege

model = SavingsModel()
custmodel = CustomerModel()

class Savings:

    def GET(self):
        if withprivilege():
            savings = model.get_allsavings()
            return render.savings(savings)
        else:
            raise web.notfound()

class Contributions:

    def GET(self):
        if withprivilege():
            return
        else:
            raise web.notfound()

class Loans:

    def GET(self):
        if withprivilege():
            loans = model.get_loans()
            return render.savingsloan(loans)
        else:
            raise web.notfound()

class AddLoan:
    def GET(self):
        if withprivilege():
            customers = custmodel.get_customers()
            return render.savingsnewloan(customers)
        else:
            raise web.notfound()

    def POST(self):
        data = web.input()


class Guidelines:

    def GET(self):
        if withprivilege():
            guides = model.get_guidelines()
            return render.savingsguide(guides)
        else:
            raise web.notfound()

class Customers:
    def GET(self):
        if withprivilege():
            customers = custmodel.get_customers()
            return render.savingscustomers(customers)
        else:
            raise web.notfound()

class AddCustomer:
    def GET(self):
        if withprivilege():
            return render.savingsnewcustomer("")
        else:
            raise web.notfound()

    def POST(self):
        data = web.input()
        if not self.userisexist(data.name):
            custmodel.new_customer(data.name, data.address, data.cellno, data.email)
            raise web.seeother("/savings/customers")
        else:
            error_msg = "Username already exist"
            return render.savingsnewcustomer(error_msg)

    def userisexist(self,name):
        user = custmodel.get_customerbyname(name)
        if user is None:
            return False
        else:
            return True
