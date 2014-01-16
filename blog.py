import web
from base import session, render, logged, model

class Blog:

    def GET(self):
        posts = model.get_allposts()
        return render.blog(posts)

class New:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
            size=30,
            description="Post title:"),
        web.form.Textarea('content', web.form.notnull,
            rows=30, cols=80,
            description="Post content:"),
        web.form.Button('Post entry'),
    )

    def GET(self):
        if not logged():
            raise web.seeother('/')

        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content, session.login)
        raise web.seeother('/')

class Edit:
    def GET(self, id):
        if not logged():
            raise web.seeother('/')

        try:
            post = model.get_anonymouspost(int(id))
            form = New.form()
            form.fill(post)
            return render.blogedit(post, form)
        except:
            None

    def POST(self, id):
        form = New.form()
        post = model.get_anonymouspost(int(id))
        if not form.validates():
            return render.blogedit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/')

class View:
    def GET(self, id):
        """View single post"""
        post = model.get_anonymouspost(int(id))
        return render.blogview(post)

class Delete:
    def GET(self, id):
        if not logged():
            raise web.seeother('/')

    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')
