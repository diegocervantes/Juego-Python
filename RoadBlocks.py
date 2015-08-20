import os
import time
import sys
 
from colorama import init, Fore, Back, Style
from tkinter import *
 
init()
def find(m,caracter):
	for i in range (0,len(m)):
		for j in range (0,len(m[i])):
			if (m[i][j] == caracter):
				return i, j

def menu(): #Esta es la funcion sin animaciones
	os.system("cls")
	
	menu=["                                     Jugar", "                                    Creditos"]
	menu1=["                                   > Jugar <", "                                  > Creditos <" ]

	print(Fore.CYAN)
	print ("                            ______                 _ ")
	print ("                           (_____ \               | |")
	print ("                            _____) )___  _____  __| |")
	print ("                           |  __  // _ \(____ |/ _  |")
	print ("                           | |  \ \ |_| / ___ ( (_| |")
	print ("                           |_|   |_\___/\_____|\____|")
	print ("                        ______  _             _          ")
	print ("                       (____  \| |           | |         ")
	print ("                        ____)  ) | ___   ____| |  _  ___ ")
	print ("                       |  __  (| |/ _ \ / ___) |_/ )/___)")
	print ("                       | |__)  ) | |_| ( (___|  _ (|___ |")
	print ("                       |______/ \_)___/ \____)_| \_|___/ ")
	print ("")
	print(Fore.RESET) 
	
	if menuvar==0:
		print (menu1[0])
		print (menu[1])


	if menuvar==1:
		print (menu[0])
		print (menu1[1])




def creditos():
	os.system('cls' if os.name == 'nt' else 'clear')
	print (Style.BRIGHT)
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print ("")
	print(Fore.BLUE + "                                   CREADORES:")
	print ("")
	print(Fore.RED + "                              Fredy Alvarez Bejar")
	print(Fore.GREEN + "                            Diego Cervantes Pacheco")
	print(Fore.YELLOW + "                              Omar Cardenas Chire")
	print(Fore.CYAN + "                        Jose Zevallos Delgado De La Flor")
	print(Fore.RESET + Style.RESET_ALL) 
	time.sleep(2)
	print ("                     Presiona <<esc>> para regresar al menu ")

def ganaste():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print(Style.BRIGHT  + Fore.YELLOW)
	print("     _____      ____        __      _     ____      _____   ________    _____ ")
	print("    / ___ \    (    )      /  \    / )   (    )    / ____\ (___  ___)  / ___/ ")
	print("   / /   \_)   / /\ \     / /\ \  / /    / /\ \   ( (___       ) )    ( (__   ")
	print("  ( (  ____   ( (__) )    ) ) ) ) ) )   ( (__) )   \___ \     ( (      ) __)  ")
	print("  ( ( (__  )   )    (    ( ( ( ( ( (     )    (        ) )     ) )    ( (     ")
	print("   \ \__/ /   /  /\  \   / /  \ \/ /    /  /\  \   ___/ /     ( (      \ \___ ")
	print("    \____/   /__(  )__\ (_/    \__/    /__(  )__\ /____/      /__\      \____\ ")
	print(Fore.RESET + Style.RESET_ALL) 
	time.sleep(3)

def mover(dirx, diry):
	global x, y, portx, porty, port1x, port1y, bla
	while (bla) :
		x += dirx
		y += diry
		if (mapa[x][y] == '+' ) :
			bla=False
			printMatrix(mapa)
			perdiste()
			break
		if (mapa[x][y] == '*' ) :
			x -= dirx
			y -= diry
			bla = False
			break
		if (mapa[x][y] == 'X'  ) :
			printMatrix(mapa)
			bla=False
			siguienteMapa()
			break       
		if mapa[x][y] == 'z':
			x = portx + dirx
			y = porty + diry
		if mapa[x][y] == 'p':
			x = port1x + dirx
			y = port1y + diry
		if mapa[x][y] == 'u':
			arriba("arriba")
			break
		if mapa[x][y] == 'l':
			izquierda("izquierda")	
			break         
		if mapa[x][y] == 'r':
			derecha("derecha")	
			break
		if mapa[x][y] == 'd':
			abajo("abajo")
			break		         
		printMatrix(mapa)

def arriba(event):
	global bla
	if estado==0:
		global menuvar
		menuvar-=1
		if menuvar < 0:
			menuvar=1
		menu()
	if estado==1:
		bla = True	
		mover(-1,0)

def abajo(event):
	global bla
	if estado==0:
		global menuvar
		menuvar+=1
		if menuvar > 1:
			menuvar=0
		menu()
	if estado==1:
		bla = True	
		mover(1,0)	

def derecha(event):
	global bla
	if estado==1:
		bla = True	
		mover(0,1)	

def izquierda(event):
	global bla
	if estado==1:
		bla = True	
		mover(0,-1)	

def enter(event):
	global estado
	if estado==0:
		if menuvar==0:
			estado=1
			os.system('cls' if os.name == 'nt' else 'clear')
			if mapaN==1:
				print("")
				print("")
				print("")
				print("")
				print("")
				print("")
				print("")
				print("")
				print("")
				print("")
				print("                                    NIVEL", mapaN)
				time.sleep(0.5)
				os.system('cls' if os.name == 'nt' else 'clear')
			printMatrix(mapa)
		if menuvar==1:
			creditos()



def escape(event):
	global estado, mapaN, mapa
	global menuvar
	global x,y, portx, porty, port1x, port1y
	mapaN = 1
	mapa = mapa1
	x, y = find(mapa,'J')
	if  find(mapa, 'p'):
		portx, porty = find(mapa, 'p')
	if find(mapa, 'z'):
		port1x, port1y = find(mapa, 'z')
	menuvar=0
	estado=0

	os.system('cls' if os.name == 'nt' else 'clear')
	menu()
	 
def printMatrix(m) :

	os.system('cls' if os.name == 'nt' else 'clear')
	for i in range (0,len(m)):
		for j in range (0,len(m[i])):
			if ( i == x and j == y):
				print (Fore.GREEN + "*", end='')
			elif (m[i][j] == 'J'):
				print (Fore.WHITE + " ", end='')
			elif (m[i][j] == 'X'):
				print (Fore.RED + "X", end='')
			elif (m[i][j] == '+'):
				print (Fore.WHITE + " ", end='')
			elif (m[i][j] == '*'):
				print (Fore.WHITE + "█", end='')
			elif m[i][j] == 'z':
				print (Fore.CYAN + "@", end='')
			elif m[i][j] == 'p':
				print (Fore.CYAN + "@", end='')
			elif m[i][j] == 'u':
				print (Fore.YELLOW + "^", end='')
			elif m[i][j] == 'l':
				print (Fore.YELLOW + "<", end='')
			elif m[i][j] == 'r':
				print (Fore.YELLOW + ">", end='')
			elif m[i][j] == 'd':
				print (Fore.YELLOW + "v", end='')		
			else:
				print (Fore.WHITE + " ", end='')
			

		print ("")
	
	time.sleep(0.03)


def siguienteMapa():
	global x, y, portx, porty, port1x, port1y, bla
	global mapaN, estado, menuvar
	global mapa
	mapas={1:mapa1, 2:mapa2, 3:mapa3, 4:mapa4, 5:mapa5, 6:mapa6, 7:mapa7, 8:mapa8}
	mapaN+=1
	os.system('cls' if os.name == 'nt' else 'clear')	
	if mapaN>len(mapas):
		bla = False
		ganaste()
		creditos()

	else:
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("                                    NIVEL", mapaN)
		time.sleep(0.5)
		os.system('cls' if os.name == 'nt' else 'clear')
		mapa=mapas[mapaN]
		x, y = find(mapa,'J')
		if  find(mapa, 'p'):
			portx, porty = find(mapa, 'p')
		if find(mapa, 'z'):
			port1x, port1y = find(mapa, 'z')

		printMatrix(mapa)

def perdiste():
	global x, y, portx, porty, port1x, port1y
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("                                    PERDISTE")
	time.sleep(0.5)
	x, y = find(mapa,'J')
	printMatrix(mapa)
	



mapa1 = ["+++++++++++++++++++++++++++++++++++++++++++++++++",
        "+                                               +",
        "+                                               +",
        "+      **J        ***                **X        +",
        "+                 ***                 *         +",
        "+                 *              *              +",
        "+                 *                     *       +",
        "+    *  *                     *   *     *       +",
        "+     * *                    **** *             +",
        "+     *                                 *       +",
        "+                                      **       +",
        "+                        **            **       +",
        "+                         *                     +",
        "+             ** *       ***                    +",
        "+             ***                               +",
        "+             **                  **            +",
        "+      **                         **            +",
        "+      **                         *             +",
        "+        *            **                        +",
        "+                    ***                        +",
        "+                   * **                        +",
        "+                                               +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++"]
mapa2 =["+++++++++++++++++++++++++++++++++++++++++++++++++",
        "+                                               +",
        "+****             **                   ***      +",
        "+****             ****                 ***      +",
        "+**                                     **      +",
        "+**               **                    **      +",
        "+                 ***                           +",
        "+                                               +",
        "+                                               +",
        "+                                               +",
        "+                  *******                     p+",
        "+   **             **                           +",
        "+ * **               z                         X+",
        "+                   **                          +",
        "+                   **             *****        +",
        "+                                  *****        +",
        "+                                               +",
        "+**      **                                     +",
        "+**    ****                                     +",
        "+**      J                                      +",
        "+****                                           +",
        "+****                                           +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++"]

mapa3 =["+++++++++++++++++++++++++++++++++++++++++++++++++",
        "+    *                                  *       +",
        "+                    **                 *p   l  +",
        "+    ***                   **          *****    +",
        "+      *             **                  *      +",
        "+      ***          **         ******    *      +",
        "+      ***         **     *                   * +",
        "+                         ***                ** +",
        "+                                            ** +",
        "+     *             *********                ** +",
        "+   ***             *       *                   +",
        "+     ****d           z   X *                   +",
        "+     *             *       *                   +",
        "+                   ****** **                   +",
        "+                                               +",
        "+         r               u                     +",
        "+    ***       ****                             +",
        "+    *                                  *   *** +",
        "+    *                          **      *  **** +",
        "+    ***      *             ******              +",
        "+            **                           *     +",
        "+             *                  ***      *   J +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++"]

mapa4=[ "+++++++++++++++++++++++++++++++++++++++++++++++++",
		"+                                  *****     *  +",
        "+                                  *   *     *  +",
        "+                                  * z *     *  +",
        "+                        *             *     *  +",
        "+                        *           *** X      +",
        "+                        *                      +",
        "+                      * *                    * +",
        "+  r    d              * *****                * +",
		"+                      *                      * +", 
		"+                       *                     * +", 
		"+                       *                 ***** +", 
		"+                       *                       +", 
		"+    *      *            *                      +", 
		"+     * p  *             *                      +", 
		"+      *  *              *                      +", 
		"+       **               *                      +", 
		"+       **                                      +",
        "+      *  *                                     +",
        "+     *    *                                    +",
        "+    *  r   *                                   +",
        "+                                               +",
        "+  J     * r         u                          +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++"]


mapa5=[ "+++++++++++++++++++++++++++++++++++++++++++++++++",
		"+                                             **+", 
		"+    J         *** ***                *****     +", 
		"+               *   *                     *     +", 
		"+               *   *                     *     +", 
		"+***       p    *****                     *     +", 
		"+  *                                      *     +", 
		"+***               *                            +", 
		"+*         u                d                   +", 
		"+***                                            +", 
		"+  *                                            +", 
		"+***                       ***                  +", 
		"+*                         *X*                  +", 
		"+***                       * *                  +", 
		"+  *                       * *                  +", 
		"+***                                            +", 
		"+                                               +", 
		"+                                      *        +", 
		"+    *   **                        *****        +", 
		"+        **       *                            *+", 
		"+        ****     *                      ****   +", 
		"+        ****               z                 * +", 
		"+++++++++++++++++++++++++++++++++++++++++++++++++"]

mapa6= ["+++++++++++++++++++++++++++++++++++++++++++++++++",
		"+ ********                                  *   +", 
		"+ *       *  d                               *  +", 
		"+ *z  d    *                                 *  +", 
		"+ *        *          ********************   *  +", 
		"+ *r  X   *                         *    *   *  +", 
		"+ ********                          *        *  +", 
		"+  ******      r                    *  *******  +", 
		"+  *                                *        *  +", 
		"+                                   *        *  +", 
		"+ *                            l             *  +", 
		"+                                            *  +", 
		"+                         *                  *  +", 
		"+                         *        ***********  +", 
		"+              *          *        *         *  +", 
		"+              *          *        *         *  +", 
		"+            p*          *        *             +", 
		"+   *          *          *         l       u   +", 
		"+   *          *                                +", 
		"+   *          *                                +", 
		"+   *                      *   u       l    J   +", 
		"+   ***         *                               +", 
		"+++++++++++++++++++++++++++++++++++++++++++++++++"]

mapa7= ["+++++++++++++++++++++++++++++++++++++++++++++++++",
		"+  *****************                      ***** +", 
		"+        *    *                               * +", 
		"+             *       *****       *       ***** +", 
		"+             *           *       *             +", 
		"+                         *       *             +", 
		"+       *                 *   ***************   +", 
		"+       *    *                              *   +", 
		"+       *    *            **********            +", 
		"+       *    *            *  z     *            +", 
		"+       *               J *     X  *            +", 
		"+       *    *            **********  **        +", 
		"+       *    *                             p    +", 
		"+       *    *            *             *       +", 
		"+       *                 *             *       +", 
		"+ *           *                                 +", 
		"+ *           *         ***                     +", 
		"+ *           *                            *    +", 
		"+ *           ***                               +", 
		"+ *           *                                 +", 
		"+        ******                                 +", 
		"+                                               +", 
		"+++++++++++++++++++++++++++++++++++++++++++++++++"]

mapa8 =["+++++++++++++++++++++++++++++++++++++++++++++++++",
        "+                                               +",
        "+                                               +",
        "+       *******z  d                             +",
        "+           ***                                 +",
        "+                                      *        +",
        "+     *   *                            *        +",
        "+     *   *                            *        +",
        "+     *  *         r                  *         +",
        "+     *  *           *****             *X       +",
        "+     ****       *********             *        +",
        "+                                               +",
        "+                                               +",
        "+                         *                     +",
        "+                         *                *    +",
        "+                         ***              *    +",
        "+                         *                *    +",
        "+                  *******                 *    +",
        "+         ****                             *    +",
        "+        ****                           u       +",
        "+********************   *   *************  *****+",
        "+ J                     *                     p +",
        "+++++++++++++++++++++++++++++++++++++++++++++++++"]




bla=True
mapaN=1
mapa=mapa1

x, y = find(mapa,'J')
if  find(mapa, 'p'):
	portx, porty = find(mapa, 'p')
if find(mapa, 'z'):
	port1x, port1y = find(mapa, 'z')



menuvar=0
estado=0 #0=Menú, 1=Juego, 2= Créditos






ventana = Tk()
ventana.title("Road Blocks")
ventana.geometry("200x200")


ventana.bind('<Up>',        arriba)
ventana.bind('<Down>',        abajo)
ventana.bind('<Left>',        izquierda)
ventana.bind('<Right>',        derecha)
ventana.bind('<Return>',        enter)
ventana.bind('<Escape>',        escape)

 
ventana.focus() 

os.system('cls' if os.name == 'nt' else 'clear')
menu()
ventana.mainloop()