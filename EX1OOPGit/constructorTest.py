import toml
path = 'tomlfiles/users.toml'

data = toml.load(path)

if data.get('users').get('user1').get('posts').get('post2'):
    print('bull')
else:
    print('nu bull')