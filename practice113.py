#q1
cast = {'Friends': [('Joey', 'Matt'), ('Chandler', 'Matthew')],
         'BBT': [('Penny', 'Kaley'), ('Sheldon', 'Jim')],
         'Breaking Bad': [('Jesse', 'Aaron'), ('Walter', 'Bryan')]}
val_0=input("Enter the charecter's name: ")
for key_0 in cast.keys():
   for elm in cast[key_0]:
       if elm[1]==val_0:
           val_1=elm[0]
           val_2=key_0

print(f"{val_0} played the character {val_1} in {val_2}")