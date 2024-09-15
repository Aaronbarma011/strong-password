import random
import time
pin = []
con = []
caracteres = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM,.-@#+-_.:+'
idioma = int(input('1 = Español, 2 = English: '))
while True:
    if idioma == 1:
            while True:
                opciones = input ('Pin o contraseña (en minusculas)')
                if opciones == 'pin':
                    x = int(input('Cuantos quieres: '))
                    if x > 10:
                        x = 10
                    for e in range (x):
                        y = random.randint(100000, 999999)
                        pin.append (y)
                    print (pin)
                elif opciones == 'contraseña':
                    min = int(input('Caracteres minimos'))
                    max = int(input('caracteres maximos'))
                    if max > 20:
                          max = 20
                    for i in range (min, max, 1):
                        co = random.choice (caracteres)
                    print (co)
    elif idioma == 2:
            while True:
                opciones = input ('Pin or password (in lowercase)')
                if opciones == 'pin':
                    x = int(input('How many do you want:'))
                    if x > 10:
                          x = 10
                    for e in range (x):
                        y = random.randint(100000, 999999)
                        pin.append (y)
                    print (pin)
                elif opciones == 'password':
                    min = int(input('Minimum characters'))
                    max = int(input('Maximum characters'))
                    if max > 20:
                          max = 20
                    for i in range (min, max, 1):
                        co = random.choice (caracteres)
                        con.append (co)
                    print (con)
