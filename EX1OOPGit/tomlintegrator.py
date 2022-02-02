import toml
import todos
import users
import os
import posts
import comments

# dir = os.path.dirname(__file__)
# dir = str(dir)
# path = os.path.join(dir, '/tomlfiles/users.toml')

path = 'tomlfiles/users.toml'


class Integrator:

    def __init__(self, path):
        self.path = path
        self.data = {}
        self.users = []
        self.posts = []
        self.comments = []
        self.todos = []

    def print_met(self):
        print(self.data)

    def data_setter(self):
        self.data = toml.load(self.path)

    def comments_handle(self, user_comments=None, post_id=None):
        if user_comments == None:
            user_comments = self.data.get('commnets')
        if post_id:
            post_id = str(post_id)
        else:
            post_id = user_comments.get('post_id')
        for key in user_comments:
            var = user_comments.get(key)
            new_comment = comments.Comments(var.get('name'), var.get('email'), var.get('body'), post_id)
            new_comment.post_method()
            self.comments.append(new_comment)

    def posts_handle(self, user_posts=None, user_id=None):

        if user_posts == None:
            user_posts = self.data.get('posts')
        if user_id:
            user_id = str(user_id)
        else:
            user_id = user_posts.get('id')
        for key in user_posts:
            var = user_posts.get(key)
            new_post = posts.Posts(var.get('title'), var.get('body'), user_id)
            new_post.post_method()
            self.posts.append(new_post)

            if var.get('comments'):
                self.comments_handle(var.get('comments'), new_post.responseDict.get('data').get('id'))

    def todos_handle(self, user_todos=None,user_id=None):
        if user_todos == None:
            user_todos = self.data.get('todos')
        if user_id:
            user_id = str(user_id)
        else:
            user_id = user_todos.get('id')

        for key in user_todos:
            var = user_todos.get(key)
            new_todos = todos.Todos(var.get('title'), var.get('due_on'), var.get('status'), str(user_id))
            new_todos.post_method()
            self.todos.append(new_todos)


    def users_handle(self):
        users_dict = self.data.get('users')
        for key in users_dict:
            var = users_dict.get(key)
            new_object = users.Users(var.get('name'), var.get('email'), var.get('gender'), var.get('status'))
            new_object.post_method()
            self.users.append(new_object)

            if var.get('posts'):
                self.posts_handle(var.get('posts'), new_object.responseDict.get('data').get('id'))
            if var.get('todos'):
                self.todos_handle(var.get('todos'), new_object.responseDict.get('data').get('id'))

    def analyse_data(self):
        self.data_setter()
        # assuming that first key is always users
        if self.data.get('users'):
            self.users_handle()
        elif self.data('posts'):
            self.posts_handle()
        elif self.data('comments'):
            self.comments_handle()
        elif self.data('todos'):
            self.todos_handle()

