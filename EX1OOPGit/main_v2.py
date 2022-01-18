import requests
import json
import collections
import methods
import users
import posts
import comments
import todos



new_user_one = users.Users('Test1', 'test1@popa.com', 'male', 'active', '999')
new_user_one.post_method()
new_user_two = users.Users('', 'Test2', 'test2@popa.com', 'male', 'active')
new_user_two.post_method()
one_Object = methods.methods()
# print(one_Object.idsREST)
one_Object.delete_all_v2()