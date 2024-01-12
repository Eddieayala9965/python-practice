ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
        },
        {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
        }
    ]
}
# ramit["friends_count"] = {}
print(ramit)
def countFriends(dictionaries):
    count = 0
    for dic in dictionaries['friends']:
        count += 1

    dic = dictionaries.copy()
    dic['friends_count'] = count
    return dic
      

print(countFriends(ramit))
  # // new dict
        # // set new key with your count 
        # return it 
        # if dic == dictionaries['friends']:
        #     count = len[dictionaries['friends']]
        #     print(dictionaries)
        #     return dictionaries
