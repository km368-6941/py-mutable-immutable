lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

mutable_types = (list, dict, set, bytearray)
immutable_types = (int, float, complex, bool, str, tuple, frozenset, bytes)

sorted_variables = {
    "mutable": [],
    "immutable": []
}

for name, value in list(globals().items()):
    if name in ["mutable_types", "immutable_types", "sorted_variables"]:
        continue

    if isinstance(value, mutable_types):
        sorted_variables["mutable"].append(value)
    elif isinstance(value, immutable_types):
        sorted_variables["immutable"].append(value)
