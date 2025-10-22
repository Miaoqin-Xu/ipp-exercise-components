#Test 1: String append test
salutation = "Hello, world!"
new_salutation = salutation + " Good to meet you."
print(f"New Salutation: {new_salutation}")
print(len(new_salutation))

#Test 2: String multiplication test
lots_of_apples = "apples " * 2
print(f"Lots of apples: {lots_of_apples}")

#Test 3: String formatting test
selling_apples = "{0} {1} {2}".format("i'm selling", lots_of_apples, "!")
print(selling_apples)
print(selling_apples.capitalize())

#Test 4: String formatting with arguments test
school_info = "Location: {school}, {city}".format(school = "Northeastern", city = "Boston")
print(school_info)
school_info = school_info + ", MA"
print(school_info)