#Se debe ejecutar el programa teniendo el navegador abierto
import pyautogui, time, webbrowser, sys, pyperclip,os, pickle
clicks1=int(input("how many months do you want to return in Filling date calendar?: ")) #Número de meses a devolverse en el primer calendario
clicks2=int(input("how many months do you want to return in Clear Date calendar?: ")) #Número de meses a devolverse en el segundo calendario
time.sleep(1)
webbrowser.open('https://portal.chicagodealvault.com/re2portal/')#Abre una página web desde el navegador, necesita "webbrowser"
time.sleep(10)
pyautogui.click(935,776) #Click en la caja Usuario
pyautogui.typewrite('Jeffjewell171') #Escribir el usuario
pyautogui.press('esc')
pyautogui.click(924,579) #Click en la caja Contraseña
pyautogui.typewrite('Fiverrtemp22') #Escribir la contraseña
pyautogui.click(816,631) #Click en el botón Iniciar Sesión
time.sleep(5) #Esperar 5 segundos a que cargue la página
pyautogui.click(710,111) #Click en la pestaña: Off Market Properties
time.sleep(4)
pyautogui.click(710,144) #Click en la pestaña: Probate
time.sleep(4)
pyautogui.click(54,354) #Click en el cuadro: Cook
time.sleep(2)
pyautogui.click(58, 381) #Click en el cuadro: Dupage
time.sleep(2)
pyautogui.click(57, 420) #Click en el cuadro: Kane
time.sleep(2)
pyautogui.click(55, 444) #Click en el cuadro: Kendall
time.sleep(2)
pyautogui.click(398,353) #Click en el cuadro: Lake
time.sleep(1)
pyautogui.click(399,384) #Click en el cuadro: McHenry
time.sleep(1)
pyautogui.click(400, 422) #Click en el cuadro: Will
time.sleep(1)
pyautogui.moveTo(1300,514,duration=0.25) #Vamos al calendario: Filling Date (primero)
pyautogui.click(1300,514) #Click en el calendario: Filling Date (primero)
pyautogui.moveTo(1014,546,duration=0.25) #Me muevo a la flecha izquierda para devolver el calendario
for i in range(0,clicks1): #Cantidad de clicks al calendario
    pyautogui.click(1014,546)
    time.sleep(1)
print("You have 5 seconds, Please select the day...")
time.sleep(6) #El programa espera a que el usaurio marque el día en el calendario
pyautogui.moveTo(1814,524,duration=0.25) #Vamos al calendario: Clear Date (segundo)
pyautogui.click(1814,524) #Click en el calendario: Clear Date (segundo)
pyautogui.moveTo(1532,562,duration=0.25) ##Me muevo a la flecha izquierda para devolver el calendario
if clicks2==0: #Cantidad de clicks al calendario
    time.sleep(6)
    print("You have 5 seconds, Please select the day...")
else:
    for i in range(0,clicks2):
        pyautogui.click(1532,562)
        time.sleep(1)
time.sleep(6) #El programa espera a que el usaurio marque el día en el calendario
print("You have 5 seconds, Please select the day...")
pyautogui.click(1000, 661) #Click en: Real State: YES
time.sleep(1)
pyautogui.click(54,694) #Click en el botón: SEARCH
time.sleep(3) #Esperamos a que cargue la pestaña
paginas=int(input("How many pages did the search generate: ")) #Cantidad de páginas que genera la búsqueda
time.sleep(3)
y=538

for i in range(0,paginas):
    for i in range (12):
        pyautogui.click(1884,1003) 
        #Voy a la barra de desplazamiento vertical, parte inferior y bajo 12 veces''' 
    time.sleep(4)
    for x in range (0,20):
        if x == 16:
            for i in range (12):
                pyautogui.click(1884,1003)
        pyautogui.moveTo(114,y,duration=0.25) #Me desplazo a cada uno de los elementos de la lista encontrados
        time.sleep(1)
        pyautogui.click(114,y) #Click en cada uno de los elementos de la lista encontrados
        time.sleep(8) #Espero a que el elemento cargue
        pyautogui.moveTo(840, 234,duration=0.15) #Me muevo a la posición de un posible mensaje de error
        pyautogui.dragRel(45, 0, duration=0.2) #Selecciono la palabra Erro
        #pyautogui.moveTo(595,251,duration=0.15)
        pyautogui.moveTo(850, 234,duration=0.15)
        pyautogui.click(button='right') #abro menú flotante
        pyautogui.moveTo(925,275,duration=0.15)
        pyautogui.click(925,275) #Copio la palabra Erro seleccionada
        Erro = pyperclip.paste()
        if Erro=="Erro":
            pyautogui.click(959,403) #ir a Cerrar Mensaje de Error si no hay Decesed_Address
            time.sleep(1)
            continue
        else:
            pyautogui.moveTo(315,640,duration=0.20) #Me muevo al nombre del Adminsitrator Info
            pyautogui.click(320,640) #Click en el nombre: Administrator Info
            pyautogui.click(320,610)
            pyautogui.click(320,671)
            pyautogui.click(320,608)
            pyautogui.click(320,636)


            time.sleep(6) #Espero a que cargue la info de teléfonos y de e-mail
            pyautogui.moveTo(889, 475,duration=1) #Voy a la Barra de título del popup
            pyautogui.click(button='right') #Activo click derecho para ver menú flotante
            time.sleep(1)
            pyautogui.moveTo(938, 590,duration=0.15) #Ir a Seleccionar todo
            pyautogui.click(938,590)
            pyautogui.moveTo(889, 475,duration=0.25) #Voy de nuevo a la barra de título de la persiana
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(1)
            pyautogui.moveTo(906, 507,duration=0.15) #ir a copiar
            pyautogui.click(906, 507)
            ultima_copia = pyperclip.paste() #Pego el contenido del bufer copiado
            f=open('D:/texto/clipboard.txt', 'a') #Creo un archivo de texto temporal
            f.write('{}'.format(ultima_copia.rstrip('\n'))) #Escribo el contenido del buffer
            
            linea=[]
            def leer_ultimas_lineas(nombre, n):
                with open(nombre) as fname:
                    lineas = [lineas.strip('\n') for lineas in fname.readlines()]
                return lineas[-n:] #Elimino texto dejando las últimas 22 líneas
            f.close()
            
            linea=leer_ultimas_lineas("D:/texto/clipboard.txt",22)
            StrA = "".join(linea) #Convierto las últimas 22 líneas en una cadena
            f=open('D:/texto/Final.txt', 'a') #Creo el archivo que va a contener la lista de e-mails y celulares
            f.write(StrA+'\n') #Escribo en el archivo, un registro en cada renglón
            
            f.close()
            os.remove("D:/texto/clipboard.txt") #Elimino el archivo temporal
            """pyautogui.click(1201,325)
            pyautogui.click(1201,340)
            time.sleep(1)"""
            pyautogui.click(1702, 481,duration=0.15) #Me muevo a la X de la ventana flotante y la Cierro
            x=359
            for i in range(0,28):
                pyautogui.click(x,215)
                x+=10
            x=339
            for i in range(0,10):
                pyautogui.click(x,215)
                x-=10
            time.sleep(1)
            y+=24
    pyautogui.click(171,477)