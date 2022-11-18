from math import atan
class Exo1:
   
   
    def f(x):
        # x=int(input("Calcul de la fonction f(x) = x/(x^2+1), Veuillez rentrer la valeur de X : "))
        return (x/(x**2 +1))

    def g(x):
        #x=int(input("Calcul de la fonction g(x) = arctan(x), Veuillez rentrer la valeur de X : "))
        return atan(x)

    L = []
    def R():
        try:
            N = int(input("Donner la valeur de l’entier N : \n"))
        except ValueError:
            print("Veuillez renseigner un entier")
            Exo1.R()
        else :
            global L
            L = list(range(-N,N+1))
            print(f"la liste L est : {L}")
            s = 0
            seq =[]
            for e in L:
                s = (Exo1.f(e)-Exo1.g(e))**2
                seq.append(s)
            print(f" La valeur de R est : {sum(seq)}")
            return sum(seq)