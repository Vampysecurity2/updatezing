#updatezing
""" nuevo script de instalaciòn automatizada y ejecuciòn de paginas web"""
import  os
import  webbrowser 

print("bienvenido a updatezing")
print("solamente elige la opcion deseada")
print("menu")
print("")
print ("1.- pagina de la NSA")
print("2.- pagina de la CIA")
print("3.- pagina de la nasa")
print("4.- instalar tools")
print("5.- instalar lenguajes de programacion en termux")
print("6.- complementos de termux")
print("7.- instalar linux")
print("0.- salir")
opcion = int(input("introduce el num deseado:   "))
if opcion == 1:
	webbrowser.open('https://nsa.gov')
elif opcion == 2:
	webbrowser.open('https://cia.gov')
elif opcion == 3:
    webbrowser.open('https://nasa.gov')
elif opcion == 4:
	os.system('apt install nmap crunch whois exiftool -y')
elif opcion == 5:
	os.system('apt install python python2 perl php ruby -y')
elif opcion == 6:
	os.system('apt install git curl wget vim openssl openssh -y')
elif opcion == 7:
    os.system('apt install proot-distro && proot-distro install debian && proot-distro login debian')
elif opcion == 0:
    os.system('exit')
    print("gracias por su preferencia")
else:
	print("esta opcion no es validad Imbecil")
