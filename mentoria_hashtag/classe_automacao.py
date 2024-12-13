
# Nesse arquivo há uma versão do robô sem usar classes, e no final uma versão usando classes

import pyautogui
import pyperclip
import time

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////       EXEMPLO SEM USAR CLASSE:       /////////////////////////////////////////////////////


# # abrindo o chrome
# pyautogui.PAUSE = 1 # entre cada comando do pyautogui vai ter o pause de 1 segundo ( de todo o programa )
# pyautogui.press("win")
# pyautogui.write("chrome")
# pyautogui.press("enter")

# # entrando no site da hashtag
# link = "https://www.hashtagtreinamentos.com/blog"
# pyperclip.copy(link)
# pyautogui.hotkey("ctrl","v")
# pyautogui.press("enter")

# # aguardar
# time.sleep(1)

# # clicando no campo de busca
# # pyautogui.click(x=1508, y=585)
# pyautogui.click(x=3084, y=136)

# # pesquisando campo de busca
# texto = "classe"
# pyperclip.copy(texto)
# pyautogui.hotkey("ctrl","v")
# pyautogui.press("enter")

# # aguardar
# time.sleep(1)

# #rolando o scroll para clicar no link 
# pyautogui.scroll(-3000)

# # clicando no campo de busca
# # pyautogui.click(x=1508, y=585)
# pyautogui.click(x=2910, y=589)

# # aguardar
# time.sleep(1)

# # extrair o link
# # pyautogui.click(x=2471, y=640, button="right")
# pyautogui.click(x=2463, y=645, button="right")
# pyautogui.press("up")
# pyautogui.press("up")
# pyautogui.press("enter")

# # printar o texto copiado
# texto = pyperclip.paste()
# print(texto)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# //////////////////////////////////////////////////////////////////////////////
# ///////////////////////   PEGANDO A POSIÇÃO DO MOUSE    //////////////////////

#  esse codigo pega a posição de um elemento na tela, 
# é necessário usalo para ajustar o posicionamento de clicks quando for rodar o codigo em computadores diferentes (pela diferença de tamanho de tela).
# basicamente a coordenada do click vai mudar de acordo com a resolução da tela onde for executado, por isso caso for preciso ajuste o posicionamento com o codigo abaixo:

# execute somente esse codigo abaixo, leve o mouse até onde voce desejar para pegar o posicionamento, aguarde 5 segundos, logo após vai mostrar no terminal a coordenada do click.

# for i in range(5):
#     print(f"pegando posição em {5 - i} segundos")
#     time.sleep(1)

# print(pyautogui.position())

# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////       EXEMPLO USANDO CLASSE:       /////////////////////////////////////////////////////

class MeuRobo():
    def __init__(self,tempo_espera):
        self.tempo_espera = tempo_espera
        pyautogui.PAUSE = 1
        
    def abrir_programa(self, nome_programa):
        pyautogui.press("win")
        pyautogui.write(nome_programa)
        pyautogui.press("enter")
        
    # def entrar_site(self,site):
    #     # site = "https://www.hashtagtreinamentos.com/blog"
    #     pyperclip.copy(site)
    #     pyautogui.hotkey("ctrl","v")
    #     pyautogui.press("enter")
    
    def entrar_site(self,site):
        self.escrever_e_enter(site)
        self.aguardar()
    
    
    # a função de pesquisar no campo de busca é a mesma de pesquisar o site, por isso foi criado somente uma função, uma função generica.
    def escrever_e_enter(self,texto):
        pyperclip.copy(texto)
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")

    def aguardar(self):
        time.sleep(1)
        
    def scroll(self):
        pyautogui.scroll(-3000)
        
    def pesquisar_no_campo(self,texto):
        self.escrever_e_enter(texto)
        self.aguardar()
        
    def clicar(self,x,y,botao="left"):
        pyautogui.click( x, y, button = botao)
        
    def pegar_posicao(self):
        for i in range(5):
            print(f"pegando posição em {5 - i} segundos")
            time.sleep(1)
        print(pyautogui.position())
        
    def extrair_link(self, x, y):
        self.clicar(x, y, botao="right")
        pyautogui.press("up")
        pyautogui.press("up")
        pyautogui.press("enter")

        # printar o texto copiado
        texto = pyperclip.paste()
        print(texto)
        
robo = MeuRobo(3)
robo.abrir_programa("chrome")
robo.entrar_site("https://www.hashtagtreinamentos.com/blog")
robo.clicar(x=3084, y=136)
robo.pesquisar_no_campo("classe")
robo.scroll()
robo.clicar(x=2910, y=589)
robo.aguardar()
robo.extrair_link(x=2453, y=645)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////