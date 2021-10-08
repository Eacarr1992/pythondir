name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kg_weight = weight / 2.205
cm_height = height * 2.54

print(f"Let's talk about {name}.")
print(f"He's {round(cm_height)} cm tall.")
print(f"He's {round(kg_weight)} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {round(cm_height)}, and {round(kg_weight)} I get {total}.")
