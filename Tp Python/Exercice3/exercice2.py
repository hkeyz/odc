from random import randint





class DataTrans :

    def __init__(self):
        DataTrans.D()
    
    d = []
    n=0
    S=0

    def f(x):
        return ((x**3) + 3*(x**2) - 5)


    
    def N():
        global S
        n = []
        for i in range(S):
            n.append(randint(0,100))
        return n


    def detD():
        global d
        global S
        global n
        for i in range(n):
                DataTrans.d.append(DataTrans.N())

    def saisi():
        global n
        global S
        try:
            n= int(input("Nombre d'element de la liste : "))
            S=int(input("Veuillez entrer la taille de chaque element : "))
        except ValueError:
            print("Veuillez renseignr que des entier")
            DataTrans.saisi()
        else:
            DataTrans.detD()

    def D():
        global d
        global S
        global n
        for i in range(n):
            DataTrans.d.append(DataTrans.N())
        print(DataTrans.d)
        return DataTrans.d


    def mini(x):
        minn = x[0]
        for i in x:
            if i<minn:
                minn=i
        return minn


    def maxi(x):
        maxx = x[0]
        for i in x:
            if i>maxx:
                maxx=i
        return maxx


    def maxEtMin():
        k = []
        l=[]
        global d
        for i in DataTrans.d:
            k.append(DataTrans.mini(i))
            l.append(DataTrans.maxi(i))
        print(f"Min {k} Max {l} ||| Min Global : {DataTrans.mini(k)}, Max Global : {DataTrans.maxi(l)}")
        return (f"Min {k} Max {l} "), (f"Min Global : {DataTrans.mini(k)}, Max Global : {DataTrans.maxi(l)}")


    def calculFTableau(x):
        resultat = []
        for i in x:
            resultat.append(DataTrans.f(i))
        return resultat


    def DPrim():
        result = []
        global d
        for i in DataTrans.d:
            result.append(DataTrans.calculFTableau(i))
        print(f"Les D' pour element de D sont respectivement : {result}")
        return result


# DataTrans.D()
# DataTrans.maxEtMin()
# DataTrans.DPrim()