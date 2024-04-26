cosas = {"comida": 15, "energia": 100, "enemigo": 3}

# print(cosas.get("comida"))
print("items")
print(cosas.items())

# print(cosas.keys())

# eliminar cosas del diccionario

# print(cosas.popitem())
# print(cosas)

print(cosas.setdefault("comida"))
print(cosas)

new_items = {"piedra": 4, "flechas": 18}

cosas.update(new_items)

print(cosas)

cosas.update(comida=56, galletas=14)
print(cosas)
