import REST
import requests
import json
import methods
import collections


URL = 'https://gorest.co.in/public/v1/'


class Posts(methods.methods):

    def __init__(self, title, body, post_id=None):

        super().__init__()
        self.id = post_id
        self.title = title
        self.body = body

    def get_setter(self):
        if self.id:
            self.url = 'https://gorest.co.in/public/v1/posts/' + self.id
        else:
            self.url = 'https://gorest.co.in/public/v1/posts/'

    def post_setter(self):
        data = {
            'title':self.title,
            'body':self.body
        }
        self.tp = 'posts'
        self.url = 'https://gorest.co.in/public/v1/users/' + self.id + '/posts'

    def del_setter(self):
        self.url = 'https://gorest.co.in/public/v1/posts/' + self.id





# action = Posts('1792','TitluTestPost', 'body test post')
#
# action.delete_method()
