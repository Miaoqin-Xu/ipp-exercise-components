# Test 1: bool declare test
is_enabled = True
if (is_enabled):
    print("The boolean 'is_enabled' is", is_enabled)

#Test 2: bool compare test
is_running = True
if (is_running == is_enabled):
    print("The booleans `is_running` and `is_enabled` have the same value:", is_running)
else:
    print(f"The booleans `is_running = {is_running}` and `is_enabled = {is_enabled}` differ.")