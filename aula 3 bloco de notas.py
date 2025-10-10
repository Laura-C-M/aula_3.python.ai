import pyautogui
from time import sleep

pyautogui.press('win')#clica na tecla windows
sleep(1)#serve para criar um compasso de espera

pyautogui.write('bloco de notas')#escreve bloco de notas na pesquisa do windows
sleep(1)

pyautogui.press('enter')
sleep(2)

pyautogui.hotkey('alt','o')#abre a opção formatar
sleep(1.5)

pyautogui.press('down')#seta para baixo para escolher fonte
sleep(2)

pyautogui.press('enter')
sleep(2)

pyautogui.write('Georgia')#seta para baixo para escolher fonte
sleep(2)
pyautogui.press('tab')
sleep(0.5)

pyautogui.write('Negrito')#seta para baixo para escolher fonte
sleep(2)

pyautogui.press('tab')
sleep(0.5)

pyautogui.write('20')#seta para baixo para escolher fonte
sleep(2)

pyautogui.press('enter')
sleep(2)

pyautogui.write('Bom dia', interval=0.5)#escreve o texto escolhido no bloco de notas
sleep(2)

pyautogui.hotkey('Ctrl','Shift','S')#usa um atalho para guardar a nota no pc
sleep(2)

pyautogui.write('texto1')#escolhe o nome para o ficheiro
sleep(2)

pyautogui.press('enter')
sleep(2)

pyautogui.press('left')#seta para a esquerda para substituir o ficheiro
sleep(2)

pyautogui.press('enter')
sleep(2)

pyautogui.hotkey('alt','f4')#fecha a aplicação
sleep(0.5)