import REST
import requests
import json
import methods
import collections


URL = 'https://gorest.co.in/public/v1/'


class Comments(methods.methods):

    def __init__(self, name=None, email=None, body=None, post_id=None, comment_id=None):


        super().__init__()

        self.cooment_id = comment_id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body


    def get_setter(self):

        if self.comment_id:
            self.url = 'https://gorest.co.in/public/v1/comments/' + self.comment_id
        elif self.post_id:
            self.url = 'https://gorest.co.in/public/v1/posts/' + self.post_id + '/comments'
        else:
            self.url = 'https://gorest.co.in/public/v1/comments/'

####all comments for an user ?



    def post_setter(self):

        self.data = {
            'name':self.name,
            'email':self.email,
            'body':self.body
        }

        self.tp = 'comments'

        self.url = 'https://gorest.co.in/public/v1/posts/' + self.post_id + '/comments'


    def del_setter(self):

        self.url = 'https://gorest.co.in/public/v1/comments/' + self.id





#
# action = Comments('1391','CommentTestPosaadst', 'rest@dsaeqw.com', 'body tessadsadsat post')
#
# action.delete_method()
