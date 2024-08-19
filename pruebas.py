from database import productos

product_list = productos.select_all()

print (product_list[1])

#lo devuelve como una tupla