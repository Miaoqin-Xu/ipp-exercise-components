from random import randint
#Test 1: simple in calcs
picked_apples = randint(20,50)
bagged_apples = randint(5,10)
available_apples = picked_apples + bagged_apples
consumed_apples = randint(1,10)
remaining_apples = available_apples - consumed_apples
print(f"Apples collected. Picked: {picked_apples}; Bagged: {bagged_apples}; Available: {available_apples}")
print(f"After eating some apples. Consumed: {consumed_apples}; Remaining: {remaining_apples}")

#Test 2: simple product calcs
shopping_trips = randint(2,4)
apples_per_trip = randint(1,5)
purchased_apples = shopping_trips * apples_per_trip
total_apples = remaining_apples + purchased_apples
print(f"After shopping. Trips: {shopping_trips}; Apples per trip: {apples_per_trip}; Purchased: {purchased_apples}; Total: {total_apples}")

#Test 3: remainders
days_per_week = 7
daily_apples_for_week = total_apples / days_per_week
left_over_apples_mod = total_apples % days_per_week
left_over_apples_sub = total_apples - (daily_apples_for_week * days_per_week)
print(f"Distributing apples over a week. Total: {total_apples}; Daily: {daily_apples_for_week}")
print(f"Leftover apples (mod): {left_over_apples_mod}; Leftover apples (sub): {left_over_apples_sub}")