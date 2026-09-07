def get_user(user_id):
    fake_db = {
        1:{'id':1,'name':'ali'},
        2: {'id': 2, 'name': 'ashkan'},
        3: {'id': 3, 'name': 'iman'},
    }

    if user_id not in fake_db:
        raise LookupError('user_id not found')
    return fake_db[user_id]