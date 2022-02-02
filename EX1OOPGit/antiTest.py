import requests
import json
import collections
import methods
import users
import posts
import comments
import todos
import tomlintegrator
path = 'tomlfiles/users.toml'
import random
def one():

    methods.methods.headers = {}
    integrator = tomlintegrator.Integrator('tomlfiles/test_one.toml')
    integrator.analyse_data()
    print(integrator.users[0].response)
    # assert integrator.users[0].response != 201
    print(integrator.users[0].responseDict)


def five():

    new_user = users.Users('AntiTest12', 'AntiTest122@email.com', 'male', 'active')
    new_user.post_method()
    assert new_user.response == 201, 'POST user failed'
    second_user = users.Users('Second Test12', 'AntiTest122@email.com', 'male', 'active')
    second_user.post_method()
    field = second_user.responseDict.get('data')[0].get('field')
    message = second_user.responseDict.get('data')[0].get('message')
    Parent = methods.methods()
    Parent.delete_by_id('users', new_user.responseDict.get('data').get('id'))
    assert second_user.response != 422, field + second_user.__getattribute__(field) + " " + message

five()

