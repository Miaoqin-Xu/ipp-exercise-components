#Test 1: string iteration
name = "Connor"
for _ in name:
    print(_)

#Test 2: list iteration and manipulation
class_items = ["notebook", "pen", "power supply"]
for item in class_items:
    print(f"Item:{item}")
class_items.append("charger")
for item in class_items:
    print(f"Item:{item}")

#Test 3: tuple iteration
immutable_class_items = ("notebook","pen","power supply")
for item in immutable_class_items:
    print(f"Item:{item}")
try:
    immutable_class_items.append("charger")
except:
    print(f"Tuples are immutable! Can't append!")
for item in immutable_class_items:
    print(f"Item:{item}")

#Test 4:rangeiteration
print("This is simpele range:")
for i in range(10):
    print(i)
print("This is bounded range:")
for i in range(1,11):
    print(i)
print("This is stepwise range:")
for i in range (0,30,5):
    print(i)