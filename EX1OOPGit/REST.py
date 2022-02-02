import collections


class REST:

    idsREST = collections.defaultdict(list)

    # def __init__(self):
        # self.ids = collections.defaultdict(list)
    @staticmethod
    def set_ids(key, value):
        REST.idsREST[key].append(value)

    def selected_method(self, action):

        if action.methodtp == 'get':
            print("tp: ")
            tp = str(input())
            print("id: (if u don t want a specific user, leave it blank)")
            id = str(input())
            response = action.get_method(tp, id)
            return response
        elif action.methodtp == 'post':
            print("tp: ")
            tp = str(input())
            if tp == 'users':
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
            elif tp == 'posts':
                print("id: ")
                id = str(input())
                print('title: ')
                title = str(input())
                print('body: ')
                body = str(input())
                action.post_method_new_post(id, title, body)
            elif tp == 'comments':
                print("id: ")
                id = str(input())
                print('name: ')
                name = str(input())
                print('email: ')
                email = str(input())
                print('body: ')
                body = str(input())
                action.post_method_new_comment(id, name, email, body)
            elif tp == 'todos':
                print("id: ")
                id = str(input())
                print('user: ')
                user = str(input())
                print('title: ')
                title = str(input())
                print('status: ')
                status = str(input())
        elif action.methodtp == 'delete':
            print('id: ')
            id = str(input())
            action.delete_method(id)
