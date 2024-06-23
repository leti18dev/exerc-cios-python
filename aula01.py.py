#criando uma função a partir desse codigo.
import math as m
#def defini uma função em python, sempre return o resultado ou o metodo 
def area_circulo(raio):
  a = m.pi * raio ** 2
  return(a)

#aqui chamamos a função a qual criamos 

raio = float(input('raio:  ')) 
x = area_circulo(raio)
print(f'Area: {x:.3f}')


 