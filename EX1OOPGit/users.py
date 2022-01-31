import REST
import requests
import json
import methods
import collections


URL = 'https://gorest.co.in/public/v1/'


class Users(methods.methods):

    def __init__(self, name, email, gender, status, id=None):

        super().__init__()

        # self.email = '12'
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status
        self.id = id

    def get_setter(self):
        if self.id:
            self.url = 'https://gorest.co.in/public/v1/users/' + str(self.id)
        else:
            self.url = 'https://gorest.co.in/public/v1/users/'

    def post_setter(self):

        self.data = {
            'name': self.name,
            'email': self.email,
            'gender': self.gender,
            'status': self.status
        }
        self.tp = 'users'
        self.url = 'https://gorest.co.in/public/v1/users'


    def del_setter(self):
        self.url = 'https://gorest.co.in/public/v1/users/' + str(self.id)






# action = Users('70','RazvanPopa211112', 'rzv222@w22zv.com', 'male','active')
# # print (action.token)
# action.delete_method()
