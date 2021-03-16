# 1 list_jmen = ["Jakub", "Petr", "Kamil", "Kamil"]
# 2 Kolikrat je Kamil uvnitr listu.
# 3 spojit to co je v listu pomoci "-"
# 4 Vypsat tento list pozadu


list_jmen = ["Jakub", "Petr", "Kamil", "Kamil", "Petr", "Martina", "Lilly"]

def indexovani_jmena(input):
    Jmeno = input("Zadej jméno?:")
    print(Jmeno)
    index = list_jmen.index(Jmeno)
    print(index)

for name in list_jmen:
    print(name)

d = {x:list_jmen.count(x) for x in list_jmen}
print(d)



# 1
print(list_jmen.count("Kamil"))

# 2
list_jmen_spojen = "-".join(list_jmen)
print(list_jmen_spojen)

# 3
list_jmen.reverse()
print(list_jmen)


print(indexovani_jmena(input))






