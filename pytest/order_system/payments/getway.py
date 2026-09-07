def process_payment(user_id , amount):
    if amount <= 0:
        raise ValueError('Amount must be grater than 0')
    return {'user_id':user_id , 'amount':amount , 'status':'paid'}