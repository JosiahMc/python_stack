students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


print students[0]['first_name']+" "+students[0]['last_name']
print students[1]['first_name']+" "+students[1]['last_name']
print students[2]['first_name']+" "+students[2]['last_name']
print students[3]['first_name']+" "+students[3]['last_name']

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for person in users:
    print person
    for idx in range(0, len(users[person])):
        print idx+1, " - ", users [person][idx]["first_name"], users[person][idx]["last_name"], " - ", len(users[person][idx]["first_name"]+users[person][idx]["last_name"])

