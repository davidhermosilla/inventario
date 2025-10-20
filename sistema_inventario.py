class Producto:
    """Clase Producto para encapsular la información basica de un producto"""
    nombre: str
    precio: float
    cantidad: int

    def __init__ (self, nombre = '', precio = 25.0, cantidad = 0):
        """
            Constructor de la clase Producto
            Argumentos:
            nombre -- Nombre del producto
            precio -- Precio del producto
            cantidad -- Cantidad de elementos de ese producto en el inventario
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string")
            
        if (not nombre):
            raise ValueError('El nombre del producto no puede ser vacio')
        
        if not isinstance(precio, float):
            raise TypeError("El precio debe ser un float")
        
        if (precio < 0):
            raise ValueError('El precio no puede ser negativo')

        try:
            cantidad = float(cantidad)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe poder convertirse a número flotante")

        if (cantidad < 0):
            raise ValueError('La cantidad no puede ser menor que 0')

        

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    """
        Metodo para actualizar el precio de un producto
        Argumentos:
        nuevo_precio -- Nuevo precio a modificar
    """
    def actualizar_precio(self,nuevo_precio):
        if (nuevo_precio < 0):
            raise ValueError('El nuevo precio debe ser positivo')
        self.precio = nuevo_precio
    
    """
        Metodo para actualizar la cantidad de productos
        Argumentos:
        nueva_cantidad -- Nuevo precio a modificar
    """
    def actualizar_cantidad(self,nueva_cantidad):
        if (nueva_cantidad < 0):
            raise ValueError('La cantidad debe ser mayor que 0')
        self.cantidad = nueva_cantidad    

    """
        Metodo para calcular el valor total de los productos, devuelve el precio del producto x la cantidad de productos            
    """
    def calcular_valor_total(self):
        return self.precio*self.cantidad

    def __str__(self):
        cadena = 'DATOS DEL PRODUCTO\n'
        cadena += '-------------------\n'
        cadena += 'Nombre Producto:'+self.nombre+ '\n'
        cadena += 'Precio del producto: '+ str(self.precio)+'\n'
        cadena += 'Cantidad de productos: '+str(self.cantidad)+'\n'
        cadena += '-------------------'
        return cadena

class Inventario:
    """
    Clase para gestionar el inventario de productos
    """
    productos = []

    def __init__(self):
        """
        Constructor para crear la clase inventario con un array vacio
        """
        self.productos = []

    """
        Metodo para agregra productos al inventario
        Argumentos:
        producto -- Producto a agregar al inventario
    """
    def agregar_producto(self,producto):

        self.productos.append(producto)
    
    """
        Metodo que busca un producto en el inventario y lo devuelve
        Argumentos:
        nombre -- Nombre del producto a buscar
    """
    def buscar_producto(self,nombre):
        producto = next(filter(lambda p: p.nombre.upper() == nombre.upper(), self.productos), None)
        if producto is None:
            raise ValueError('Producto no encontrado')
        else:
            return producto
        

    """
        Metodo que devuelve el valor total del inventario multiplicando el valor de los productos por su cantidad y sumandolos
    """
    def calcular_valor_inventario(self):
        return sum(p.precio*p.cantidad for p in self.productos)

    """
        Metodo que lista todos los productos del inventario
    """
    def listar_productos(self):
        for p in self.productos:
            print(p)

def pedir_numero(mensaje, condicion=lambda x: True):
    while True:
        try:
            valor_string = input(mensaje)
            valor = float(valor_string)
            if condicion(valor):
                return valor
            print('El valor no cumple la condición.',condicion)
        except:
            try:
                valor = int(valor_string)
                if condicion(valor):
                    return valor
                print('El valor no cumple la condición.',condicion)
            except:
                print('Entrada no valida, intentalo de nuevo')

def pedir_float(mensaje, condicion=lambda x: True):
    while True:
        try:
            valor = float(input(mensaje))
            if condicion(valor):
                return valor
            print('El valor no cumple la condición.',condicion)
        except:
            print('Entrada no valida, intentalo de nuevo')

def pedir_int(mensaje, condicion=lambda x: True):
    while True:
        try:
            valor = int(input(mensaje))
            if condicion(valor):
                return valor
            print('El valor no cumple la condición.',condicion)
        except:
            print('Entrada no valida, intentalo de nuevo')

def pedir_string(mensaje, condicion=lambda x: True):
    while True:
        valor = str(input(mensaje))
        if not valor:
            print('Entrada no valida, intentalo de nuevo')
        else:
            return valor

def menu_principal(inventario):
    op=0
    while True:
        print('1. Agregar producto')
        print('2. Buscar producto')
        print('3. Calcular valor inventario')
        print('4. Listar productos')
        print('5. Actualizar cantidad de producto')
        print('6. Actualizar precio de producto')
        print('7. Salir del programa')
    
        try:
            op = input('Introduzca una opción: ')
            op=int(op)            
        except:
            print('Introduzca una opción valida, intentalo de nuevo')

        match op:
            case 1:
                nombre = pedir_string('Nombre del producto: ')
                precio = pedir_numero('Precio del producto: ', lambda x: x>0)
                cantidad = pedir_int('Cantidad de productos a agregar: ', lambda x: x>0)
                producto = Producto(nombre,precio,cantidad)
                inventario.agregar_producto(producto)
                print('Producto agregado correctamente')
            case 2:
                nombre_buscar = pedir_string('Nombre a buscar: ')
                try:
                    producto = inventario.buscar_producto(nombre_buscar)
                except:
                    print('Producto no encontrado')
                else:
                    print(producto)
            case 3:
                print('El valor del inventario es de: ', inventario.calcular_valor_inventario())
            case 4:
                print('LISTA DE PRODUCTOS')
                inventario.listar_productos()
            case 5:
                nombre_buscar = pedir_string('Nombre de producto a actualizar: ')
                try:
                    producto = inventario.buscar_producto(nombre_buscar)                    
                except:
                    print('Producto no encontrado')
                    
                cantidad = pedir_int('Cantidad de elementos para el producto, '+ str(producto.nombre)+': ',lambda x: x>0)
                producto.actualizar_cantidad(cantidad)
                print('Cantidad de producto actualizada')
            case 6:
                nombre_buscar = pedir_string('Nombre de producto a actualizar: ')
                try:
                    producto = inventario.buscar_producto(nombre_buscar)                    
                except:
                    print('Producto no encontrado')
                
                precio = pedir_numero('Precio del producto, '+str(producto.nombre)+': ',lambda x: x>0)
                producto.actualizar_precio(precio)
                print('Precio de producto actualizada')
            case 7:
                break
            case _:
                continue
            

if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
    