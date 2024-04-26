frutas = ["manzana", "naranja", "peras", "frutilla", "uva"]
years = [3, "1998", 2.5, 987, "1994"]

print(frutas, years)

frutas.append("durazno")
print(frutas)

frutas.extend(years)
print(frutas)

frutas.remove("naranja")
print(frutas)

frutas.pop(0)
print(frutas)

frutas.pop(-1)
print(frutas)

numeros = [5, 1928, 4, 17, 68]
print(numeros)
numeros.sort()
print(numeros)

# check membership

print("manzana" in frutas)  # false, porque no esta
print("frutilla" in frutas)

print(frutas.index("uva"))
