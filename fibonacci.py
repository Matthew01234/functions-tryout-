def Fibonacciformule(n):
   if n <= 1:
       return n
   else:
       return(Fibonacciformule(n-1) + Fibonacciformule(n-2))
cijfer = int(input("hoeveel keer wilt u een Fibonacci formule uitgevoerd zien? "))

if cijfer <= 0:
   print("type alstublieft een + nummer")
else:
   print("Fibonacci formule:")
   for i in range(cijfer):
       print(Fibonacciformule(i))