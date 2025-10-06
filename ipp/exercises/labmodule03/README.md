# Programming in Python - An Introduction: Lab Module 03

### Description

Briefly describe the objectives of the Lab Module:

1) Created a small temperature convert module, and imported it to another module to create a small app

2) Learned to use if __name__ == "__main__" to prevent test code being called in imported modules

3) 


### Exercise Activities

List the actions you took in implementing the Lab Module:

1)**To answer DEV-03-003" This code defines a function divideTwoNumbers() that calls another function from the SimpleDivision module named divideTwoNumbersWithExceptionHandling().
It passes two numbers (numerator and denominator) to perform division while handling errors such as division by zero.
The test calls divideTwoNumbers(5, 2) and divideTwoNumbers(3, 0) to verify that normal division works and exceptions are handled properly.
I probably did not get repository correctly, so I did not see a premade simpledivison module in my file, therefore, I had to create one myself for that code to work.
2) 

3) 


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) ran a test code to see if the converter returns the correct value
#Simple Test Cases 2
orig_f_val = 72.0                         
c_val = convert_Temp_F_to_C(orig_f_val)     
f_val = convert_Temp_C_to_F(c_val)            

print(f"Celsius = {c_val} and Fahrenheit = {f_val}. Original Fahrenheit is {orig_f_val}")

if (orig_f_val == f_val):
    print("The temp converter works!")
else:
    print("The temp converter failed!")
"""
Also did a test to see if the temperature input is in the desired range

2) tested if my simple division module works properly by using the dividetwonumbers function to see the outcomes.

3) 

EOF.
