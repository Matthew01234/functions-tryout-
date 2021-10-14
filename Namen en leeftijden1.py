#Programma 3: Namen en leeftijden

def info():
   while True:
    naam = input ('Wat is je naam? ')
    if naam == ('stop'):
        break
    getal = input ('Hoe oud ben je? ')
    if getal == ('stop'):
          break
    
    print ('Hallo '+ naam +', je leeftijd is '+ getal+ ' jaar')
   
   
info()