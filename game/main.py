import random



def seleccion():
  n=input("Piedra, Papel o Tijera: ")

  if n=='piedra':
    n=1
    print("Usuario: Piedra")
  elif n=='papel':
    n=2
    print("Usuario: Papel")
  elif  n=='tijera':
    n=3
    print("Usuario: Tijera")
  elif n!='piedra'or n!='papel' or n!='tijera':
    print('Escribe solo: Piedra, Papel o Tijera')
  
  m=random.randrange(1,4)
  return n, m

def logica_juego(n,m,usuario_gano, maquina_gano):
  
  if n==m==1:
    print("Maquina: Piedra")
    print ("Empate!")
  if n==m==2:
    print("Maquina: Papel")
    print ("Empate!")
  if n==m==3:
    print("Maquina: Tijera")
    print ("Empate!")
  
  if n==1 and m==2:
    print("Maquina: Papel!")
    print ("Perdiste!")
    maquina_gano+=1
  if n==1 and m==3:
    print("Maquina: Tijera!")
    print ("Ganaste!")
    usuario_gano+=1
  
  if n==2 and m==1:
    print("Maquina: Piedra!")
    print ("Ganaste!")
    usuario_gano+=1
  if n==2 and m==3:
    print("Maquina: Tijera!")
    print ("Perdiste!")
    maquina_gano+=1
  if n==3 and m==2:
    print("Maquina: Papel!")
    print ("Ganaste!")
    usuario_gano+=1
  if n==3 and m==1:
    print("Maquina: Piedra!")
    print ("Perdiste!")
    maquina_gano+=1

  return usuario_gano, maquina_gano
    



def ejecucion():
  usuario_gano=0
  maquina_gano=0
  while True:
    n,m=seleccion()
    usuario_gano,maquina_gano=logica_juego(n,m,usuario_gano,maquina_gano)
   
    if usuario_gano==2:
      break
    if maquina_gano==2:
      break
ejecucion()