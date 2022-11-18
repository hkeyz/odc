from exercice1 import Exo1 as exo1
from exercice2 import DataTrans as dataTrans

def choisir():
    try:
        choix = int(input("Choisissez 1 pour Exercice 1 ou 2 pour Exercice 2 ou 0 pour quitter : "))
    except:
        choisir()
    else:
        if choix==1:
            exo1.R()
        elif choix==2:
            dataTrans.saisi()
            optionf_exo2()
        elif choix==0:
            exit()
        else:
            choisir()
    choisir()


def optionf_exo2():
    try:
        choix2 = int(input("Choissisez 1 pour voir La liste D  ou 2 pour avoir le min et max ou 3 pour avoir D' ou 4 pour quitter l'exo2 : "))
    except:
        optionf_exo2()
    else:
        if choix2==1:
            dataTrans.D()
            optionf_exo2()
        elif choix2==2:
            dataTrans.maxEtMin()
            optionf_exo2()
        elif choix2 ==3:
            dataTrans.DPrim()
            optionf_exo2()
        elif choix2 ==4:
            choisir()
        else:
            optionf_exo2()

choisir()