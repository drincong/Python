
from Cliente import Cliente
#from Articulos import articulos


pedro =  Cliente('Pedro', 'Hernandez', 34, '548', 'phernandezn@outlook.es', '+57 6015879651','2346', 'Tienda AB')
print (pedro)
print(pedro.saluda())
pedro.agregar_articulos('Soldadura',1)
pedro.agregar_articulos('Llaves de tuerca',3)
pedro.listar_articulos()
pedro.valida_dni()
pedro.obtener_email()

print("*******************************************************************************************************")

angela = Cliente('Angela','Perez', 45, '234', 'aperez230@gmail.com', '+57 6015124978', '34562345-1', 'Restaurante Los Olivos')
print (angela)
print(angela.saluda()) 
angela.agregar_articulos('Cinta aislante',2)
angela.agregar_articulos('Tuberia 2 pulgadas agua',3)
angela.listar_articulos()
angela.valida_dni()
angela.obtener_email()