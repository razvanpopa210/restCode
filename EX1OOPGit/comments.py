import REST
import requests
import json
import methods
import collections


URL = 'https://gorest.co.in/public/v1/'


class Comments(methods.methods):

    def __init__(self, name, email, body, id=None, post_id=None):

        super().__init__()

        self.id = id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body


    def get_setter(self):

        if self.id:
            self.url = 'https://gorest.co.in/public/v1/comments/' + self.id
        else:
            self.url = 'https://gorest.co.in/public/v1/comments/'

####all comments for an user ?



    def post_setter(self):

        data = {
            'name':self.name,
            'email':self.email,
            'body':self.body
        }

        self.tp = 'comments'

        self.url = 'https://gorest.co.in/public/v1/posts/' + self.id + '/comments'


    def del_setter(self):

        self.url = 'https://gorest.co.in/public/v1/comments/' + self.id





#
# action = Comments('1391','CommentTestPosaadst', 'rest@dsaeqw.com', 'body tessadsadsat post')
#
# action.delete_method()
