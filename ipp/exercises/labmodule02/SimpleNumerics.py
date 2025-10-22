from random import randint
#Test 1:int
age = randint(20,100)
count = -5
large_numer = 1000000
alt_age_number = 1_000_000
print(f"Age:{age}, count:{count}, large_numer:{large_numer}, alt_age_number:{alt_age_number}")

#Test 2: float
price = 19.99
termperature = 72.4
sci_value = 1.23e-4
print(f"Price:{price}, termperature:{termperature}, sci_value:{sci_value}")

#Test 3: abs() and conversion
price = 15.99
price_no_cents = int(price)
price_with_cents = float(price_no_cents)
print(f"Price:{price}, price_no_cents:{price_no_cents}, price_with_cents:{price_with_cents}")
