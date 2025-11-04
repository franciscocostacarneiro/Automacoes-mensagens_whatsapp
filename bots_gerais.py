# Requests
import pyautogui 
from time import sleep

#BOT DE MINERAÇÃO
#chegando até o lugar da mineração
# sleep(2)
# pyautogui.moveTo(702,511, duration=1)

# for i in range(100):
#     pyautogui.leftClick()
#     sleep(0.2)
# print("Fim do script")

##########################################################################

#BOT ESPECIALISTA EM CLIQUES
#Trata-se de um script mais detalhado da função de clicar
# sleep(2)
# pyautogui.click(x=840, y= 918, clicks=2, interval=0.0, button="left", duration=0.2)
#clicks=2 é a quantidade de clicks que queremos - o método click, por default é realizado com o botão esquerdo do mouse, porém, também temos as funções
#prontas, como a leftClick(), rightClick(), doubleClick(), tripleClick() e middleClick().
#interval=0.0 é o intervalo entre os clicks
#button="left" é o botão que queremos usar
#duration=0.2 é o tempo que leva para o cursor ir até a posição

##########################################################################

#DESAFIO PARA A CRIAÇÃO DE UMA NOVA PASTA
# sleep(2)
# pyautogui.moveTo(1711,516, duration=1)
# sleep(0.5)
# pyautogui.rightClick()
# sleep(0.5)
# pyautogui.move(-50,160, duration=1)
# sleep(0.5)
# pyautogui.click(button="left")
# sleep(0.5)
# pyautogui.move(-400,0, duration=0.5)
# sleep(0.5)
# pyautogui.click(button="left")
# sleep(0.5)
# pyautogui.write("Testando escrever o t", interval=0.05)
# sleep(0.05)
# pyautogui.press("´")
# sleep(0.05)
# pyautogui.write("itulo de uma nova pasta", interval=0.05)
# pyautogui.press("enter")
# print("Fim do script")