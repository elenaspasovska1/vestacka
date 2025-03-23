dict={'Elena':'29-03-2004', 'Ivona':'03-11-2003', 'Sanja':'17-05-2004'}
print("Dobredojdovte vo recnikot za rodendeni, nie gi znaeme rodendenite na: ")
for ime in dict.keys():
    print(ime)
find=input("Koj rodenden e potrebno da se prebara?")
print(dict[find])