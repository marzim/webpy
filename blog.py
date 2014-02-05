import web
from base import session, render, withprivilege
from blogmodel import BlogModel
from loginmodel import LoginModel
from urlify import URLify

blogmodel = BlogModel()
loginmodel = LoginModel()

class Blog:

    def GET(self):
        posts = blogmodel.get_allposts()
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

        if withprivilege():
            form = self.form()
            return render.blognew(form)
        else:
            raise web.seeother('/blog')

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.blognew(form)
        blogmodel.new_post(form.d.title, form.d.content, session.login)
        raise web.seeother('/blog')

class Edit:
    def GET(self, id):
        if not withprivilege():
            raise web.seeother('/blog')

        try:
            post = blogmodel.get_anonymouspost(int(id))
            form = New.form()
            form.fill(post)
            return render.blogedit(post, form)
        except:
            None

    def POST(self, id):
        form = New.form()
        post = blogmodel.get_anonymouspost(int(id))
        if not form.validates():
            return render.blogedit(post, form)

        blogmodel.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/blog')

class View:
    def GET(self, id):
        """View single post"""
        post = blogmodel.get_anonymouspost(int(id))
        user = loginmodel.get_userbyid(int(post['userid']))['user']
        content = URLify().formatstring(post.content)
        return render.blogview(post, user, content)

class Delete:
    def GET(self, id):
        if not withprivilege:
            raise web.seeother('/blog')

    def POST(self, id):
        blogmodel.del_post(int(id))
        raise web.seeother('/blog')
