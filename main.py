import pymongo
from pymongo import MongoClient 

host_info = ''
username = ''
password = ''

host = f'mongodb+srv://{username}:{password}@{host_info}'
port = 27017

client = MongoClient(host, port)

# db
db = client.test # if test db does not exist, create new one.
# db = client["test"] # same as above.
print(db) # basic info of db.
print(dir(db)) # list of db.
print(db.name) # test

# collection
collect = db.collect # call collection called 'collect'. if collect does not exist, create new one.
#collect = db["collect"]

# document insert
user_info = {'id':'testid','pw':'testpw', 'email':'test@test.com', 'items':{'gun':1, 'apple':10}, 'tags':['tag1', 'tag2', 'tag3']}
collect_id = collect.insert_one(user_info).inserted_id

data = list()
data.append({'id':'aaa', 'name':'john', 'age':100})
data.append({'id':'bbb', 'name':'bob', 'age':4})
data.append({'id':'ccc', 'name':'bob', 'age':29})
data.append({'id':'eee', 'name':'idk', 'age':12})
data.append({'id':'123', 'name':'why name?', 'age':97})
collect.insert_many(data)

print(collect.count())

# .find_one() vs .find()
print(collect.find_one())
print(collect.find_one({'id':'testid'}))
print(collect.find_one({'id':'ifnotexist'}))

for item in collect.find():
    print(item)

test_id_data = collect.find({'id':'testid'})

for item in collect.find().sort("age"): # using sort
    print(item)


# update