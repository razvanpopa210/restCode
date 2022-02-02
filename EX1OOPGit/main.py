import requests
import json
import collections
import methods
import users
import posts
import comments
import todos
import tomlintegrator
path = 'tomlfiles/test_five.toml'

# new_user_one = users.Users('Test1', 'test1@popa.com', 'male', 'active', '999')
# new_user_one.post_method()
# new_user_two = users.Users('Test2', 'test2@popa.com', 'male', 'active')
# new_user_two.post_method()
# new_post = posts.Posts('TestPost', 'TestMain', '2544')
# new_post.post_method()
# print(one_Object.idsREST['posts'])

# new_comm = comments.Comments('best', 'best@email', 'bodybody', '1346')
# new_comm.post_method()
# print(one_Object.idsREST)
# path = 'tomlfiles/users.toml'
#
one_Object = methods.methods()
inte = tomlintegrator.Integrator(path)

inte.analyse_data()
one_Object.delete_all_v3()
