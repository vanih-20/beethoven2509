products = []
def create_product(product):
    global products
    if len(product) ==0:


        product.id=1
    else:
        product.id = products[len(products)-1].id+1
    products.append(product)



def read_all():
    return products



def read_by_id(id): #return first occurance index of product
    for product in product:
        if product.id == id:
            return products
    return None



def update(product):
    old_product = read_by_id(product.id)
    if old_product == None:
        return
    old_product.name = product.name
    old_product.description = product.description
    old_product.category = product.tags
    old_product.stock = product.stock
    old_product.price = product.price



def delete_by_id(id):
    product = read_by_id(id)
    products.remove(product)