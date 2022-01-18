import REST
import requests
import json
import methods
import collections


URL = 'https://gorest.co.in/public/v1/'


class Todos(methods.methods):

    def __init__(self, title, status, id=None, user_id=None):

        super().__init__()
        self.id = id
        self.user_id = user_id
        self.title = title
        self.body = body

    def get_setter(self):
        if self.id:
            self.url = 'https://gorest.co.in/public/v1/todos/' + self.id
        else:
            self.url = 'https://gorest.co.in/public/v1/todos/'

####all todos for an user ?

    def post_setter(self):
        data = {

            'title':self.title,
            'due_on':self.due_on,
            'status':self.status
        }

        self.tp = 'todos'

        self.url = 'https://gorest.co.in/public/v1/users/' + self.id + '/todos'

    def del_setter(self):
        self.url = 'https://gorest.co.in/public/v1/todos/' + self.id




#
# action = Todos('1792','TitluTestPost', 'body test post')
#
# action.delete_method()
