from microbit import *
while True :
    valeur=pin2.read_analog()
    tension=valeur*300/1023
    pression=tension/2.3
    print("P=",pression,"hPa")
    print((pression))
    sleep(2000)