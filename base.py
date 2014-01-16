import web
import model

web.config.debug = False

urls = (
'/', 'Index',
'/login','login.Login',
'/logout','Logout',
'/register', 'register.Register',
'/view/(\d+)', 'blog.View',
'/new', 'blog.New',
'/delete/(\d+)', 'blog.Delete',
'/edit/(\d+)', 'blog.Edit',
'/blog', 'blog.Blog',
)

app = web.application(urls, globals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'login': 0, 'privilege': 0, 'user': 'anonymous'})

t_globals = {
 'datestr': web.datestr,
 'session': session
 }

render = web.template.render('/home/marzim83/main/webpy/templates', base='base', globals=t_globals)

def logged():
    if session.login > 0:
        return True
    else:
        return False

class Index:
    def GET(self):
        """Show page"""
        return render.index(10)

class Logout:
    def GET(self):
        session.login = 0
        session.kill()
        raise web.seeother('/')

application = app.wsgifunc()
