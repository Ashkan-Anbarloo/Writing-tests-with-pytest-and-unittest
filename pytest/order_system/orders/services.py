def create_order(user_id , product_id):
    if not user_id or not product_id:
        raise ValueError('user_id and product_id cannot be empty')
    return {'user_id': user_id, 'product_id': product_id , 'status':'created'}