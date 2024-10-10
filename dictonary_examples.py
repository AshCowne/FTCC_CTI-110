# Ash Cowne
# 10/10/2024
# Learning about dictonarys.

# Creating a dictonary.
rose_bush = {"rose_color":"purple", "price":32.98444, "max_height":"60", "is_perennial":True}

# Get a value given the key.
print(rose_bush);
print(rose_bush["rose_color"]);
print(rose_bush["price"]);
print(rose_bush["max_height"]);
print(rose_bush["is_perennial"]);
print(f"${rose_bush['price']:.2f}")
print (f"Is the rose bush a pereniall? {rose_bush['is_perennial']}");
print(rose_bush['rose_color']);

# Adding a new key.
rose_bush['water_needed'] = "4 ounce per day"

# Print the intire diconary
print(rose_bush)
print("")

# Adding a new key
rose_bush.update({"leaf_color":"green", "sun_needed":6})
print(rose_bush)
print("")

# Remove from dictonary
del rose_bush['max_height']

print(rose_bush)
print("")

# Printing just the keys
print(rose_bush.keys());

# ask the user to give one of the keys.
answer = input("Enter a key from the dictonary: ");
print("")

# Give a value ascosated to the Users answer.
print(f"The value for {answer} is {rose_bush[answer]}")











