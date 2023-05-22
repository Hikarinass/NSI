from microbit import *
while True :
    valeur=pin2.read_analog()
    tension=valeur*300/1023
    pression=tension/2.3
    pression=pression*100
    distance=(pression-10000)/(997*9.81)
    distance=distance*1000
    print("Distance que parcourt le capteur=",distance,"Cm")
    #print((cm))
    sleep(1000)

from microbit import *

while True:
    valeur = pin2.read_analog()
    tension = valeur * 300 / 1023
    pression = tension / 2.3
    pression = pression * 100
    distance = (pression - 10000) / (997 * 9.81)
    distance = distance * 1000
    
    # Conversion en chaîne de caractères
    distance_str = "{:.2f}".format(distance)
    
    display.scroll("Distance : " + distance_str + " cm")
    
    sleep(1000)
