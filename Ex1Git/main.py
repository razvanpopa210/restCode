import requests
import json
import collections

URL = 'https://gorest.co.in/public/v1/'



class REST:

    idsREST = collections.defaultdict(list)

    # def __init__(self):
        # self.ids = collections.defaultdict(list)
    @staticmethod
    def set_ids(key, value):
        REST.idsREST[key].append(value)

    def selected_method(self, action):

        if action.methodType == 'get':
            print("type: ")
            type = str(input())
            print("id: (if u don t want a specific user, leave it blank)")
            id = str(input())
            response = action.get_method(type, id)
            return response
        elif action.methodType == 'post':
            print("type: ")
            type = str(input())
            if type == 'users':
                print('name: ')
                name = str(input())
                print('email: ')
                email = str(input())
                print('gender: ')
                gender = str(input())
                print('status: ')
                status = str(input())
                respons = action.post_method_new_user(name, email, gender, status)
                return respons
            elif type == 'posts':
                print("id: ")
                id = str(input())
                print('title: ')
                title = str(input())
                print('body: ')
                body = str(input())
                action.post_method_new_post(id, title, body)
            elif type == 'comments':
                print("id: ")
                id = str(input())
                print('name: ')
                name = str(input())
                print('email: ')
                email = str(input())
                print('body: ')
                body = str(input())
                action.post_method_new_comment(id, name, email, body)
            elif type == 'todos':
                print("id: ")
                id = str(input())
                print('user: ')
                user = str(input())
                print('title: ')
                title = str(input())
                print('status: ')
                status = str(input())
        elif action.methodType == 'delete':
            print('id: ')
            id = str(input())
            action.delete_method(id)

class methods(REST):

    def __init__(self, methodType):

        assert methodType == 'get' or methodType == 'post' or \
               methodType == 'put' or methodType == 'delete',\
            f"Method '{methodType}' dosen't exist or there is a typo"

        self.methodType = methodType
        # self.ids = collections.defaultdict(list)
        self.status = ''
        self.response = 0

    def set_status(self):


        response_dict = {
            200: 'OK. Everything worked as expected.',
            201: 'Resource was successfully created in response to a POST request',
            204: 'Resource was successfully created in response to a DELETE request',
            304: 'The resource was not modified. You can use the cached version',
            400: 'The resource was not modified. You can use the cached version.',
            401: 'Authentication failed',
            403: 'The authenticated user is not allowed to access the specified REST endpoint',
            404: 'The requested resource does not exist.',
            405: 'Method not allowed. Please check the Allow header for the allowed HTTP methods.',
            415: 'Unsupported media type. The requested content type or version number is invalid.',
            422: 'Data validation failed (in response to a POST request, for example). Please check the response body for detailed error messages.',
            429: 'Too many requests. The request was rejected due to rate limiting.',
            500: 'Internal server error'
        }

        try:
            self.status = response_dict[self.response]
        except KeyError:
            print(f'{self.response} code is unknown')

        print(self.status)




    def get_method(self, type, id):


        if (type != 'users' and type != 'posts' and type != 'comments' and type!='todos'):
            print ('not the right type')
            return 0
        if id:
            geturl = URL + str(type) + '/' +str(id)
            print ('you selected the user ' + id)
            response = requests.get(geturl, verify=False, headers={
                'Authorization': 'access_token cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'})
        else:
            geturl = URL + str(type)
            print('no user selected')
            response = requests.get(geturl, verify=False, headers={
            'Authorization': 'access_token cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'})
        
        self.response = response.status_code
        self.set_status()

        # print(response.content)
        return response

    def post_method_new_user(self, name, email, gender, status):

        data = {
            'name':name,
            'email':email,
            'gender':gender,
            'status':status
        }

        response = requests.post(URL + 'users', verify=False, data=data,  headers={
            'Authorization': 'Bearer cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'})
        responseDict = json.loads(response.content.decode('utf-8'))
        # self.ids['user'].append(responseDict['data']['id'])
        self.response = response.status_code
        self.set_status()
        REST.set_ids('users', responseDict['data']['id'])
        # print(response.content)
        return response

    def post_method_new_post(self, id, title, body):

        data = {
            'title':title,
            'body':body
        }

        response = requests.post(URL +'users/' + id +'/' + 'posts', verify=False, data=data, headers={
            'Authorization': 'Bearer cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'})
        responseDict = json.loads(response.content.decode('utf-8'))
        # self.ids['post'].append(responseDict['data']['id'])
        self.response = response.status_code
        self.set_status()
        REST.set_ids('posts', responseDict['data']['id'])
        # print(response.content)

        return 0

    def post_method_new_comment(self, id, name, email, body):

        data = {
            'name':name,
            'email':email,
            'body':body
        }

        response = requests.post(URL +'posts/' + id + '/comments', verify=False, data=data, headers={
            'Authorization': 'Bearer cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'})
        responseDict = json.loads(response.content.decode('utf-8'))
        # self.ids['comment'].append(responseDict['data']['id'])
        self.response = response.status_code
        self.set_status()
        REST.set_ids('comments', responseDict['data']['id'])
        # print(response.content)

        return 0

    def post_method_new_todos(self, id, user, title, status):

        data = {
            'user':user,
            'title':title,
            'status':status
        }

        response = requests.post(URL +'users/' + id + '/' + 'todos', verify=False, data=data, headers={
            'Authorization': 'Bearer cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'})
        responseDict = json.loads(response.content.decode('utf-8'))
        # self.ids['todo'].append(responseDict['data']['id'])
        self.response = response.status_code
        self.set_status()
        REST.set_ids('todos', responseDict['data']['id'])



        return 0


    def delete_method(self, id):
        print('What u want to delete ?')
        print('type: ')
        type = str(input())
        while (type != 'users' and type != 'posts' and type != 'comments' and type!='todos'):
            print ('not the right type (users, posts, comments, todos), try again')
            type=(str(input()))


        response = requests.delete(URL + type +'/' + id, verify=False, headers={
                'Authorization': 'Bearer cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'})

        self.response = response.status_code
        self.set_status()
        # print(response.content)

    def delete_all(self, type, id):


        response = requests.delete(URL + type +'/' + id, verify=False, headers={
                'Authorization': 'Bearer cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'})

        self.response = response.status_code
        self.set_status()




#delete test id 1485, post id 1499, comment 1439, to do 2061


print("hello. this script will run until u give ok the value 0. if u want to continue, plis give ok the value 1")
print('ok: ')
ok = int(input())
# idsDict = collections.defaultdict(list)
rest_obj = REST()
while (ok == 1):
    print('Method:')
    methodType = str(input())
    action = methods(methodType)
    rest_obj.selected_method(action)
    print('id-uri: ', rest_obj.idsREST)
    print('ok: ')
    ok = int(input())

print('You want to del everything ? y / n ?')
delete = str(input())
if delete == 'y':
    for key in rest_obj.idsREST:
        for value in rest_obj.idsREST[key]:
            action.delete_all(key, str(value))
print ('verify: ')

action.get_method('users', str(rest_obj.idsREST['users'][0]))

print("the script has reach the end")

# action = methods('get')
#
# response = selected_method(action)
# responseDict = json.loads(response.content.decode('utf-8'))
# print(type(responseDict['data']['id']))



# actions.get_method(type, id)

# response=requests.get('https://gorest.co.in/public/v1/users/2113', verify=False)
# print (response.content)