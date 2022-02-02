import pytest
import requests
import json
import collections
import methods
import users
import posts
import comments
import todos
import tomlintegrator
import random
path = 'tomlfiles/users.toml'

# am incercat mai multe feluri de assert-uri
# pentru unele teste cand stiu sigur ca urmeaza o greseala am folosit conditia != "status_code pentru eroare"
# pentru testele unde nu ma astept la greseala folosesc assert de tip == "status_code pentru succes rqeust"
# asta formeaza cumva o inconstanta a testelor dar in acelasi timp le separa pe cele pozitive de cele negative, cred:D"
# n am mai testat prin "GET" pentru fiecare test, sa revin la ideea asta ? doar testez ce status code intoarce actiunea pe care o fac (post / delete)



def test_one(): # incercare de post user fara token de autentificare

    methods.methods.headers = {}
    integrator = tomlintegrator.Integrator('tomlfiles/test_one.toml')
    integrator.analyse_data()
    assert integrator.users[0].response != 401, 'authentication failed - you cant create users without an autehntication token'

def test_two(): # crearea si stergea unui user

    integrator = tomlintegrator.Integrator('tomlfiles/test_two.toml')
    integrator.analyse_data()
    assert integrator.users[0].response == 201, 'post failed'
    Parent = methods.methods()
    Parent.delete_by_id('users', str(integrator.users[0].responseDict['data']['id']))
    # assert Parent.response != 401, 'authentication failed' # sa verific mereu authentication ?
    assert Parent.response == 204, 'delete failed'

def test_three(): # crearea unui user - post si stergea postului, apoi a userului

    integrator = tomlintegrator.Integrator('tomlfiles/test_three.toml')
    integrator.analyse_data()
    assert integrator.users[0].response == 201, 'post failed'
    assert integrator.posts[0].response == 201, 'post failed'
    Parent = methods.methods()
    Parent.delete_by_id('posts', str(integrator.posts[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('users', str(integrator.users[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'

def test_four(): # crearea unui user - post - comment si stergerea commnetului - postului - userului

    integrator = tomlintegrator.Integrator('tomlfiles/test_four.toml')
    integrator.analyse_data()
    assert integrator.users[0].response == 201, 'post failed'
    assert integrator.posts[0].response == 201, 'post failed'
    assert integrator.comments[0].response == 201, 'post failed'
    Parent = methods.methods()
    Parent.delete_by_id('comments', str(integrator.comments[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('posts', str(integrator.posts[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('users', str(integrator.users[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'

def test_five(): # user --post-commnent --tod.o dar si stergerea lor

    integrator = tomlintegrator.Integrator('tomlfiles/test_five.toml')
    integrator.analyse_data()
    assert integrator.users[0].response == 201, 'post failed'
    assert integrator.posts[0].response == 201, 'post failed'
    assert integrator.comments[0].response == 201, 'post failed'
    assert integrator.todos[0].response == 201, 'post failed'
    Parent = methods.methods()
    Parent.delete_by_id('todos', str(integrator.todos[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('comments', str(integrator.comments[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('posts', str(integrator.posts[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('users', str(integrator.users[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'


def test_six(): # crearea mai multor useri, cu un numar diferit de posturi commenturi si todos precum si stergerea tuturor

    integrator = tomlintegrator.Integrator('tomlfiles/test_six.toml')
    integrator.analyse_data()
    for item in integrator.users:
        assert item.response == 201, 'post failed'
    for item in integrator.posts:
        assert item.response == 201, 'post failed'
    for item in integrator.comments:
        assert item.response == 201, 'post failed'
    for item in integrator.todos:
        assert item.response == 201, 'post failed'

    Parent = methods.methods()

    for item in integrator.todos:
        Parent.delete_by_id('todos', str(item.responseDict['data']['id']))
        assert Parent.response == 204, 'delete failed'

    for item in integrator.comments:
        Parent.delete_by_id('comments', str(item.responseDict['data']['id']))
        assert Parent.response == 204, 'delete failed'

    for item in integrator.posts:
        Parent.delete_by_id('posts', str(item.responseDict['data']['id']))
        assert Parent.response == 204, 'delete failed'

    for item in integrator.users:
        Parent.delete_by_id('users', str(item.responseDict['data']['id']))
        assert Parent.response == 204, 'delete failed'

def test_seven(): # crearea mai multor usori cu posturi commenturi si todos diferite (ca numar / continut) + stergerea doar unora dintre elemente)

    integrator = tomlintegrator.Integrator('tomlfiles/test_six.toml')
    integrator.analyse_data()
    for item in integrator.users:
        assert item.response == 201, 'post failed'
    for item in integrator.posts:
        assert item.response == 201, 'post failed'
    for item in integrator.comments:
        assert item.response == 201, 'post failed'
    for item in integrator.todos:
        assert item.response == 201, 'post failed'

    Parent = methods.methods()

    for i in range(len(integrator.todos)):
        if i % 2 == 0:
            Parent.delete_by_id('todos', str(integrator.todos[i].responseDict['data']['id']))
            assert Parent.response == 204, 'delete failed'

    for i in range(len(integrator.comments)):
        if i % 2 == 1:
            Parent.delete_by_id('comments', str(integrator.comments[i].responseDict['data']['id']))
            assert Parent.response == 204, 'delete failed'

    for i in range(len(integrator.posts)):
        if i % 5 == 0:
            Parent.delete_by_id('posts', str(integrator.posts[i].responseDict['data']['id']))
            assert Parent.response == 204, 'delete failed'

    for i in range(len(integrator.users)):
        if i % 2 == 0:
            Parent.delete_by_id('users', str(integrator.users[i].responseDict['data']['id']))
            assert Parent.response == 204, 'delete failed'

def test_eight(): # alegerea unui user random din cei existenti ceva si crearea unui post pentru el

    get_test = users.Users()
    get_test.get_method()
    assert get_test.response == 200, 'Get Failed'
    x = random.randint(0, len(get_test.responseDict.get('data')) - 1)
    random_user_id = get_test.responseDict.get('data')[x].get('id')
    user_test = users.Users(id=random_user_id)
    user_test.get_method()
    assert user_test.response == 200, 'Get Failed'
    new_post = posts.Posts('Post Test 8', 'Body Post Test 8', str(random_user_id))
    new_post.post_method()
    assert new_post.response == 201, 'post failed'

def test_nine(): # alegerea unui user random din cei existenti ceva si crearea unui post si a unui comment pentru el

    get_test = users.Users()
    get_test.get_method()
    assert get_test.response == 200, 'Get Failed'
    x = random.randint(0, len(get_test.responseDict.get('data')) - 1)
    random_user_id = get_test.responseDict.get('data')[x].get('id')
    user_test = users.Users(id=random_user_id)
    user_test.get_method()
    assert user_test.response == 200, 'Get Failed'
    new_post = posts.Posts('Post Test 9', 'Body Post Test 9', str(random_user_id))
    new_post.post_method()
    assert new_post.response == 201, 'POST post failed'
    new_comment = comments.Comments('CommentTest 9', 'test9@email.com', 'Body Comment Test 9',
                                     str(new_post.responseDict.get('data').get('id')))
    new_comment.post_method()
    assert new_comment.response == 201, 'POST comment failed'

def test_ten():# alegerea unui user random din cei existenti ceva si crearea unui post a unui comment si a unui tod.o pentru el

    get_test = users.Users()
    get_test.get_method()
    assert get_test.response == 200, 'Get Failed'
    x = random.randint(0, len(get_test.responseDict.get('data')) - 1)
    random_user_id = get_test.responseDict.get('data')[x].get('id')
    user_test = users.Users(id=random_user_id)
    user_test.get_method()
    assert user_test.response == 200, 'Get Failed'
    new_post = posts.Posts('Post Test 10', 'Body Post Test 10', str(random_user_id))
    new_post.post_method()
    assert new_post.response == 201, 'POST post failed'
    new_comment = comments.Comments('CommentTest 10', 'test10@email.com', 'Body Comment Test 10',
                                     str(new_post.responseDict.get('data').get('id')))
    new_comment.post_method()
    assert new_comment.response == 201, 'POST comment failed'
    new_todos = todos.Todos('Todos10', '2022-03-01T18:00:00', 'pending', str(user_test.responseDict.get('data').get('id')))
    new_todos.post_method()
    assert new_todos.response == 201, 'POST todo failed'

def test_eleven(): #alegerea unui user random din cei existenti ceva si crearea unui post a unui comment si a unui tod.o pentru el
    # plus stergerea lor

    get_test = users.Users()
    get_test.get_method()
    assert get_test.response == 200, 'Get Failed'
    x = random.randint(0, len(get_test.responseDict.get('data')) - 1)
    random_user_id = get_test.responseDict.get('data')[x].get('id')
    user_test = users.Users(id=random_user_id)
    user_test.get_method()
    assert user_test.response == 200, 'Get Failed'
    new_post = posts.Posts('Post Test 11', 'Body Post Test 11', str(random_user_id))
    new_post.post_method()
    assert new_post.response == 201, 'POST post failed'
    new_comment = comments.Comments('CommentTest 11', 'test11@email.com', 'Body Comment Test 11',
                                     str(new_post.responseDict.get('data').get('id')))
    new_comment.post_method()
    assert new_comment.response == 201, 'POST comment failed'
    new_todos = todos.Todos('Todos11', '2022-03-01T18:00:00', 'pending', str(user_test.responseDict.get('data').get('id')))
    new_todos.post_method()
    assert new_todos.response == 201, 'POST todo failed'
    Parent = methods.methods()
    Parent.delete_by_id('todos', str(new_todos.responseDict.get('data').get('id')))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('comments', str(new_comment.responseDict.get('data').get('id')))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('posts', str(new_post.responseDict.get('data').get('id')))
    assert Parent.response == 204, 'delete failed'



def test_twelve(): # crearea a doi useri cu acceasi adresa de email

    new_user = users.Users('AntiTest12', 'AntiTest122@email.com', 'male', 'active')
    new_user.post_method()
    assert new_user.response == 201, 'POST user failed'
    second_user = users.Users('Second Test12', 'AntiTest122@email.com', 'male', 'active')
    second_user.post_method()
    field = second_user.responseDict.get('data')[0].get('field')
    message = second_user.responseDict.get('data')[0].get('message')
    Parent = methods.methods()
    Parent.delete_by_id('users', new_user.responseDict.get('data').get('id'))
    assert second_user.response != 422, field + " " + second_user.__getattribute__(field) + " " + message
    assert Parent.response == 204, 'detele failed'

def test_thirteen(): # crearea unui usor cu campul "gender" gresit

    new_user = users.Users('AntiTest13', 'Test13@email.com', 'barbat', 'active')
    new_user.post_method()
    # assert new_user.response == 201, 'POST user failed'
    field = new_user.responseDict.get('data')[0].get('field')
    message = new_user.responseDict.get('data')[0].get('message')
    if str(message) == "can't be blank" and str(field) == 'gender':
        message_two = " gender can be only 'male' or 'female'"
    assert new_user.response != 422, field + " " + new_user.__getattribute__(field) + " " + message + message_two

def test_fourteen(): # crearea unui user cu campul "status" gresit

    new_user = users.Users('AntiTest14', 'Test14@email.com', 'male', 'pro active')
    new_user.post_method()
    # assert new_user.response == 201, 'POST user failed'
    field = new_user.responseDict.get('data')[0].get('field')
    message = new_user.responseDict.get('data')[0].get('message')
    if str(message) == "can't be blank" and str(field) == 'status':
        message_two = " status can be only 'active' or 'inactive'"
    assert new_user.response != 422, field + " " + new_user.__getattribute__(field) + " " + message + message_two


def test_fifteen(): # crearea unui usor cu campul "mail" gresit

    new_user = users.Users('AntiTest15', 'Test15email.com', 'male', 'active')
    new_user.post_method()
    # assert new_user.response == 201, 'POST user failed'
    field = new_user.responseDict.get('data')[0].get('field')
    message = new_user.responseDict.get('data')[0].get('message')
    message_two = " email must contain '@'"
    assert new_user.response != 422, field + " " + new_user.__getattribute__(field) + " " + message + message_two

def test_sixteen():

    integrator = tomlintegrator.Integrator('tomlfiles/test_sixteen.toml')
    integrator.analyse_data()
    assert integrator.users[0].response == 201, 'post failed'
    assert integrator.posts[0].response == 201, 'post failed'
    field = integrator.comments[0].responseDict.get('data')[0].get('field')
    message = integrator.comments[0].responseDict.get('data')[0].get('message')
    message_two = " email must contain '@'"
    Parent = methods.methods()
    Parent.delete_by_id('users', str(integrator.users[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    assert integrator.comments[0].response != 422, field + " " + integrator.comments[0].__getattribute__(field) + " " + message + message_two

def test_seventeen(): #crearea unui todos cu campul status gresit

    integrator = tomlintegrator.Integrator('tomlfiles/test_seventeen.toml')
    integrator.analyse_data()
    assert integrator.users[0].response == 201, 'post failed'
    field = integrator.todos[0].responseDict.get('data')[0].get('field')
    message = integrator.todos[0].responseDict.get('data')[0].get('message')
    message_two = " status must be 'pending' or 'completed'"
    Parent = methods.methods()
    Parent.delete_by_id('users', str(integrator.users[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    assert integrator.todos[0].response != 422, field + " " + integrator.todos[0].__getattribute__(field) + " " + message + message_two

def test_eighteen(): #crearea unui todos cu campul due_on completat incorect (nu intoarce eroare, dar completeaza cu null)

    integrator = tomlintegrator.Integrator('tomlfiles/test_eighteen.toml')
    integrator.analyse_data()
    assert integrator.users[0].response == 201, 'post failed'
    due_on_value = integrator.todos[0].responseDict.get('data').get('due_on')
    Parent = methods.methods()
    Parent.delete_by_id('users', str(integrator.users[0].responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    assert due_on_value is not None, 'you enter a bad format for due_on field, the format must be: yyyy:mm:ddThh:mm:ss'

def test_nineteen(): #dubla stergere a aceluiasi user

    new_user = users.Users('Test19s', 'Test19s@email.com', 'male', 'active')
    new_user.post_method()
    assert new_user.response == 201, 'POST user failed'
    Parent = methods.methods()
    Parent.delete_by_id('users', str(new_user.responseDict['data']['id']))
    assert Parent.response == 204, 'delete failed'
    Parent.delete_by_id('users', str(new_user.responseDict['data']['id']))
    assert Parent.response != 404, 'delete failed'

