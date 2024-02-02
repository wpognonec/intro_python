obj = 42            #Assign
obj = 'ABcd'        #Reassign
obj.upper()         #Neither
obj = obj.lower()   #Reassign
print(len(obj))     #Neither
obj = list(obj)     #Reassign
obj.pop()           #Mutate
obj[2] = 'X'        #Mutate
obj.sort()          #Mutate
set(obj)            #Neither
obj = tuple(obj)    #Reassign