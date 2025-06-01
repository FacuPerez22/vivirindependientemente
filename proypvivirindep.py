print("*************************************")
print("*******¿PUEDO INDEPENDIZARME?********")  
print("*************************************\n")
print("Vamos a ver si puedes independizarte, para ello te vamos a hacer algunas preguntas.")

nombre = input("¿Cual es tu nombre? ").lower()
edad = int(input("¿Cual es tu edad? "))
ingresos = float(input("¿Cuánto dinero recibes mensualmente por tu labor?  "))
if edad >= 18 and ingresos > 1000:
    print("**¡¡Tienes grandes posibilidades de inpendizarte!!**\n")
    print(f"¡¡Hola {nombre}, ya tienes {edad} años!! vamos a ver si tus ingresos son los correctos entoces puedes independizarte. 'SIN' la necesidad de la ayuda de tus padre. SI tus ingresos totales son suficiente solo si puedes INDEPENDIZARTE \n")
    print("Si tus padres te ayduan economicamente,( aunque estarias dependiedo...) O si tienes departamento propio, O alquilas O compartis gastos, dependiendo tambien el barrio donde quieras vivir. Tambien debes tener en cuenta tus gastos fijos y adicionales, como transporte, comida, ropa, salud y entretenimiento.\n")
    padres = input("¿Tus padres te ayudan? (si/no): ").lower()
    if padres == "si":
        print("Puedes considerar esto en tu presupuesto. servira para imprevistos o ahorros")    
        ayuda_padres = float(input("¿Cuánto dinero te aportan tus padres mensualmente? "))
    elif padres == "no":
        print("Tus padres 'NO' te ayudan, entonces debes planificar bien tus gastos, que no superen tus ingreso!.")
    beca = input("¿Tienes alguna beca? (si/no): ").lower()
    if beca == "si":
        print("es un apoyo adicional bastamte importante. ")
        ayuda_beca = float(input("¿Cuánto dinero recibes mensualmente por la beca? "))
    if beca == "no":
        print("No tienes beca, por lo tanto no tenes un ingreso extra.\n")
else:
    print("Lo siento, no puedes independizarte. Debes tener al menos 18 años y un ingreso mensual mayor a 1000.\n")        
ingresos_totales = (ingresos + ayuda_padres + ayuda_beca)

print(f"\n Tu ingreso total es: {ingresos_totales} ahora {nombre} si y solo si los gastos no superan los ingresos podras ser independiente \n ")
departamento = input("¿Tienes departamento propio, alquilas o compartis gastos? (propio/alquilo/comparto): ").lower()
if departamento == "propio":
    print("Tienes tu propio departamento, esto es buenismo tienes un gasto significativo menos!.\n")
elif departamento == "alquilo":
    print(f"{nombre} alquilar un departamento puede ser costoso, asegúrate de que se ajuste a tu presupuesto y que no supere el 50% de tus ingresos totales de: {ingresos_totales}.\n")
    barrio = input("¿En qué barrio alquilas? (Nueva Córdoba/Alberdi/San Martín): ").lower()
    if barrio == "nueva cordoba":
        print("Alquilar en Nueva Córdoba puede ser costoso, planifica bien tus gastos para no exederte")
        valor_alquiler = float(input("¿Cuánto pagas de alquiler mensualmente en Nueva Cordoba? "))
        if valor_alquiler > ingresos_totales * 0.5:
            print("El alquiler en Nueva Córdoba no debe superar el 50% de tus ingresos, revisa tu presupuesto.")  
        else:
            print(f"{nombre} el alquiler en Nueva Córdoba es adecuado, pagas {valor_alquiler} que no supera el 50% de tus ingresos totales de: {ingresos_totales}.")
    elif barrio == "alberdi": 
        print("Alberdi es una buena opción para alquilar. ")
        valor_alquiler = float(input("¿Cuánto pagas de alquiler mensualmente en Alberdi? "))
        if valor_alquiler > ingresos_totales * 0.5:
            print("El alquiler en Alberdi no debe superar el 50% de tus ingresos, revisa tu presupuesto.")
        else:
            print(f"{nombre} el alquiler en Alberdi es adecuado, pagas {valor_alquiler} que no supera el 50% de tus ingresos totales de: {ingresos_totales}.")  
    elif barrio == "san martin":
        print("San Martín es una zona tranquila para vivir.")
        valor_alquiler = float(input("¿Cuánto pagas de alquiler mensualmente en San Martín? "))
        if valor_alquiler > ingresos_totales * 0.5:
            print("El alquiler en San Martín no debe superar el 50% de tus ingresos, revisa tu presupuesto.")
        else:
            print(f"{nombre} el alquiler en San Martín es adecuado, pagas {valor_alquiler} que no supera el 50% de tus ingresos totales de: {ingresos_totales}.")
    if departamento == "comparto":
        print("Compartir gastos puede ayudarte a ahorrar dinero.")
        valor_alquiler = float(input("¿Cuánto pagas de alquiler mensualmente al compartir gastos? "))
        if valor_alquiler > ingresos_totales * 0.5:
            print("El alquiler a compartir gastos no debe superar el 50% de tus ingresos, revisa tu presupuesto.")
        else:
            print(f"{nombre} el alquiler al compartir gastos es adecuado, pagas {valor_alquiler} que no supera el 50% de tus ingresos totales de: {ingresos_totales}.")
    else:
        print("Barrio no reconocido, asegúrate bien de investigar los costos.\n")

gastos_fijos = float(input(f" vamos ahora por los gastos fijos, hablamos de servicios e impuestos, que no pueden superar el 20% de tu ingresos {ingresos_totales}  "))
if gastos_fijos > ingresos_totales * 0.2:
    print("Tus gastos fijos son demasiado altos, revisa tu presupuesto.")
else:
    print(f"Los gastos fijos son adecuados, pagas {gastos_fijos} que no supera el 20% de tus ingresos totales de: {ingresos_totales}.")

gastos_no_fijos = float(input("Los gastos no fijos, como comida, transporte, ropa, salud y entretenimiento. ¿Cuánto gastas mensualmente en estos conceptos no debe superar el 30% de los ingresos? "))
if gastos_no_fijos > ingresos_totales * 0.3:
    print("Tus gastos no fijos son demasiado altos, revisa tu presupuesto.")
else:
    print(f"Los gastos 'NO FIJOS' son adecuados, pagas {gastos_no_fijos} que no supera el 30% de tus ingresos totales de: {ingresos_totales}.")

ahorro = float(input("¿Qué porcentaje de tu sueldo quieres destinar al ahorro? (ejemplo: 10 para 10%): "))
ahorro = round(ingresos_totales * (ahorro / 100), 2)
if ahorro > ingresos_totales * 0.1:
    print(f"Has decidido ahorrar {ahorro}  de tus ingresos totales.  ")

tiempo_ocio = int(input("¿Cuántas horas a la semana dedicas al ocio?  "))
if tiempo_ocio < 10:
    print("Es importante dedicar tiempo al ocio para mantener un equilibrio en tu vida.  ")
else:
    tiempo_ocio >= 15
    print("¡¡No seas tan bagoneta!!!!.")
    
    gastos_totales = (gastos_fijos + gastos_no_fijos + valor_alquiler + ahorro)
print("\n Vamos a revisar tus gastos totales y ver si son adecuados para tu situación financiera.\n")
if gastos_totales > ingresos_totales:
    print("Tus gastos totales superan tus ingresos, debes ajustar tu presupuesto.")
else:
    print(f"Tus gastos totales son adecuados, pagas {gastos_totales} que no supera tus ingresos totales de: {ingresos_totales}.")

print(f"Has decidido ahorrar el {ahorro}% de tu sueldo y dedicas {tiempo_ocio} horas a la semana al ocio.")
print("**¡Felicidades!** Has completado el análisis de tu situación financiera y puedes independizarte si mantienes un buen control de tus gastos y ahorros.")
print("Fin del programa")