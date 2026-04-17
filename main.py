prices = [12500, 45000, 3200, 89000, 6750]
formatted = list(map(lambda p: f"{p:,} so‘m", prices))
print(formatted)

words = ["python", "map", "function", "exercise", "example"]
capitalized = list(map(str.capitalize, words))
print(capitalized)
