nomes = ("antony","artorias","kratos")

print("antony" in nomes)
print(nomes[1:2])
print(nomes[1:-1])
print(nomes[:2])
print(nomes)
print(len(nomes))
print(type(nomes))
print(dir(nomes))
x = ("aaa",)
print(type(x))
x = ("aaa")
print(type(x))
#x[0] = 1 vai dar erro pois é imutavel
print(x[0])
x = ("aaa","blue","red")
print(nomes[0])
print(nomes[-1])
print(nomes[1:])
print(x.index("blue"))
print(x.count("blue"))