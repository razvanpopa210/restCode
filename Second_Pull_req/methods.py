import REST
import requests
import json
import collections
from abc import abstractmethod
import toml
URL = 'https://gorest.co.in/public/v1/'


class methods():

    idsREST = collections.defaultdict(list)

    # def __init__(self):
        # self.ids = collections.defaultdict(list)
    @staticmethod
    def set_ids(key, value):
        methods.idsREST[key].append(value)


    def __init__(self):

        self.url = 'https://gorest.co.in/public/v1/'
        self.headers ={'Authorization': 'Bearer cfc389c1c50611ea6166ddd106f643feb7af468119a3bcb0f7851872dc1e6755'}
        self.data = {}
        self.tp = ''
        self.response_dict = {}

    def set_status(self):

        code_dict = {
            200: 'OK. Everything worked as expected.',
            201: 'Resource was successfully created in response to a POST request',
            204: 'Resource was successfully created in response to a DELETE request',
            304: 'The resource was not modified. You can use the cached version',
            400: 'The resource was not modified. You can use the cached version.',
            401: 'Authentication failed',
            403: 'The authenticated user is not allowed to access the specified REST endpoint',
            404: 'The requested resource does not exist.',
            405: 'Method not allowed. Please check the Allow header for the allowed HTTP methods.',
            415: 'Unsupported media tp. The requested content tp or version number is invalid.',
            422: 'Data validation failed (in response to a POST request, for example). Please check the response body for detailed error messages.',
            429: 'Too many requests. The request was rejected due to rate limiting.',
            500: 'Internal server error'
        }

        try:
            self.status = code_dict[self.response]
        except KeyError:
            print(f'{self.response} code is unknown')

        print('Code: ',self.response, " ", self.status)

    @abstractmethod
    def get_setter(self):
        pass

    @abstractmethod
    def post_setter(self):
        pass

    @abstractmethod
    def del_setter(self):
        pass



    def get_method(self):


        self.get_setter()
        response = requests.get(self.url, verify=False, headers=self.headers)
        self.response = response.status_code
        self.set_status()
        print(response.content)
        return response
    


    def post_method(self):
        
        self.post_setter()
        response = requests.post(self.url, verify=False, data=self.data, headers= self.headers)
        self.responseDict = json.loads(response.content.decode('utf-8'))
        self.response = response.status_code
        print(response.content)
        self.set_status()
        self.set_ids(self.tp, self.responseDict['data']['id'])




    def delete_method(self):

        self.del_setter()
        response = requests.delete(self.url, verify=False, headers=self.headers)
        self.response = response.status_code
        self.set_status()
        print(response.content)

    def delete_all(self, tp, id):

        response = requests.delete(URL + tp + '/' + id, verify=False, headers=self.headers)
        self.response = response.status_code
        self.set_status()

    def delete_all_v2(self):
        print(methods.idsREST)
        for i in methods.idsREST:
            for j in methods.idsREST[i]:
                response = requests.delete(URL + str(i) + '/' + str(j), verify=False, headers=self.headers)

                self.response = response.status_code
                self.set_status()

    def delete_all_v3(self):
        print(methods.idsREST)
        for value in methods.idsREST.get('users'):
            response = requests.delete(URL +'users/' + str(value), verify=False, headers=self.headers)
            self.response = response.status_code
            self.set_status()

