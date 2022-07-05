import random

y = input('Qual sua jogada: ')
jogadaMaquina = [
  "pedra",
  "papel",
  "tesoura",
]
x = random.randint(0, 2)
valorMaquina = jogadaMaquina[x]

if y != "pedra" and y != "papel" and y != "tesoura":
  print("Escreve direito burro!")
else:
  print("A Maquina jogou:",valorMaquina)
  if y == "pedra":
    if valorMaquina == "papel":
      print("Perdeu!")
    elif valorMaquina == "tesoura":
      print("Ganhou!")
    else:
      print("Empate!")
  elif y == "papel":
    if valorMaquina == "papel":
      print("Empate!")
    elif valorMaquina == "tesoura":
      print("Perdeu!")
    else:
      print("Ganhou!")
  elif y == "tesoura":
    if valorMaquina == "papel":
      print("Ganhou!")
    elif valorMaquina == "tesoura":
      print("Empate!")
    else:
      print("Perdeu!")
