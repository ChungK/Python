def login(_id):
    users = ['Rom', 'Chung']
    for user in users:
        if user == _id:
            return True
    return False