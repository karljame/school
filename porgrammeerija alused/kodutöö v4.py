n=int(input("Sisend:  "))
listv3 = [k * k for k in range(0, n)]
print("Väljund: ", ", ".join( repr(e) for e in listv3 ) )
