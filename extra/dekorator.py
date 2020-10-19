#Primjer dekoracije s argumentima
def dekoriraj(s):
    def fff(f):
        def ff(*arg,**kvarg):
            v=f(*arg,**kvarg)
            l=len(v)
            print(s*4+s * l)
            print(s, v, s)
            print(s*4+s * l)
        return ff
    return fff
@dekoriraj("u")
def pozdravi(ime):
    return "Lijep pozdrav "+ime+"!!!"

pozdravi("Danijela")

#Primjer argumenata i KVargumenata
def fun(x=0,y=" ",z=True):
    print(x,y,z)

n={
    "z":False,
    "x":"7",
    "y":55,
}
fun(**n)



