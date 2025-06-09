from mysql import connector
from database.connection import create_connection

def insert(data):
    conn= create_connection()
    sql = """INSERT INTO productos (NombreDelProducto, Descripcion, Precio, CantidadEnStock, Codigo, CodigoDeBarra, Categoria)
            VALUES(%s,%s,%s,%s,%s,%s,%s)
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert(productos) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_id(_id):
    conn= create_connection()
    sql = f"""SELECT * FROM productos WHERE ProductoID = {_id}"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        productos=cur.fetchone()
        return productos
    except connector.Error as err:
        print(f"Error at select_by_id(productos) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_all():
    conn= create_connection()
    sql= """SELECT ProductoID, NombreDelProducto, Descripcion, Precio, CantidadEnStock, Codigo, CodigoDeBarra, Categoria FROM productos"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        productos = cur.fetchall()
        return productos
    except connector.Error as err:
        print(f"Error at select_all(producto) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def update(_id,data):
    conn= create_connection()
    sql = f"""UPDATE productos SET
            NombreDelProducto = %s,
            Descripcion = %s,
            Precio = %s, 
            CantidadEnStock = %s,
            Codigo = %s,
            CodigoDeBarra= %s,
            Categoria= %s
        WHERE ProductoID = {_id}
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at update(producto) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_parameter(param):
    conn= create_connection()
    param= f"%{param}%"
    sql = """SELECT ProductoID, NombreDelProducto, Descripcion, Precio, CantidadEnStock, Codigo, CodigoDeBarra, Categoria
        FROM productos
        WHERE NombreDelProducto LIKE %s OR CantidadEnStock LIKE %s"""
    try:
        cur= conn.cursor()
        cur.execute(sql, (param,param))
        productos=cur.fetchall()
        return productos
    except connector.Error as err:
        print(f"Error at select_by_parameter(productos): {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def delete(_id):
    conn= create_connection()
    sql = f"""DELETE FROM productos
        WHERE ProductoID = {_id}
            """
    try:
        cur= conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


def update_product_stock(product_id, nuevo_stock):
    if nuevo_stock <= 0:
        print("La cantidad vendida es menor cero.")
        return 0

    conn = create_connection() 
    sql_select = f"SELECT CantidadEnStock FROM productos WHERE ProductoID = {product_id}"
    sql_update = f"UPDATE productos SET CantidadEnStock = {nuevo_stock} WHERE ProductoID = {product_id} "

    try:
        cur = conn.cursor()

        # Verificar stock actual
        cur.execute(sql_select, (product_id,))
        result = cur.fetchone()
        if not result:
            print(f"Producto '{product_id}' no encontrado.")
            return 0

        stock_actual = result[0]


        cur.execute(sql_update, (product_id, nuevo_stock)) # Actualizar stock
        conn.commit()
        print(f"Stock actualizado para '{product_id}'. Stock actual: {nuevo_stock}")
        return cur.rowcount

    except Exception as e:
        print(f"Error al actualizar stock para '{product_id}': {e}")
        return 0
    
    finally:
        cur.close()
        conn.close()



def productos_mas_vendidos():
    pass

def add_stock_producto(nuevo_stock,_id):
    conn = create_connection() 
    sql_update = f"UPDATE productos SET CantidadEnStock = CantidadEnStock + {nuevo_stock} WHERE ProductoID = {_id} "

    try:
        cur= conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error al actualizar stock para '{nuevo_stock}': {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
