# input 

c = float(input("Digite su capital inicial : "))

# prossecing 

n=0
d=2*c

while  (c <= d):
    
    n= n+1
    c= c+ 5*c/100

# output 

print("la capital acumulada es:", c)
print("el capital inicial se duplico en, ", n ,"meses")

# FIN 