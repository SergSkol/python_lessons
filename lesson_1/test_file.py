import pandas

d= {'a': [1,2,3], 'b': [4, 5, 6]}
print('create dict...')
print(pandas.DataFrame(d))

d['c'] = [3,2,1]
print('add key value pair...')
print(pandas.DataFrame(d))

d['a'] = ['a', 'a', 'a']
print('change key value pair...')
print(pandas.DataFrame(d))

del d['a']
print('delete key value pair...')
print(pandas.DataFrame(d))
