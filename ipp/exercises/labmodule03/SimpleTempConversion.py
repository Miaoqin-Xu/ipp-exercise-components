"""
This module contains temperature conversion functions.

"""
min_indoor_temp_F = 65.0
max_indoor_temp_F = 85.0

def is_Desired_Indoor_Temp_Range(temp, is_celsius):
    """
    Check whether a given temperature is within the desired indoor range.

    Parameters:
    temp -- the input temperature value (float)
    is_celsius -- True if temperature is in Celsius, False if in Fahrenheit

    Returns:
    True if the temperature is within the range (65°F–85°F), otherwise False.
    """
    if temp >= min_indoor_temp_F and temp <= max_indoor_temp_F:
        print(f"Input temperature (F) is within desired indoor range: {temp}")
        return True
    
    print(f"Input temperature (F) is outside desired indoor range: {temp}")
    return False

#Simple Test Cases
#is_Desired_Indoor_Temp_Range(70.0, False)
#is_Desired_Indoor_Temp_Range(50.0, False)
def convert_Temp_F_to_C(temp_F = 0.0):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
    temp_F -- temperature in Fahrenheit (float)

    Returns:
    Temperature in Celsius (float)
    """
    temp_C = (temp_F - 32) * 5.0 / 9.0
    print(f"Converted {round(temp_F, 1)}°F to {round(temp_C, 1)}°C")
    return temp_C
def convert_Temp_C_to_F(temp_C = 0.0):
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
    temp_C -- temperature in Celsius (float)

    Returns:
    Temperature in Fahrenheit (float)
    """
    temp_F = (temp_C * 9.0 / 5.0) + 32
    print(f"Converted {round(temp_C, 1)}°C to {round(temp_F, 1)}°F")
    return temp_F

orig_f_val = 72.0                         # 原始华氏温度
c_val = convert_Temp_F_to_C(orig_f_val)       # 转成摄氏
f_val = convert_Temp_C_to_F(c_val)            # 再转回华氏

print(f"Celsius = {c_val} and Fahrenheit = {f_val}. Original Fahrenheit is {orig_f_val}")

if (orig_f_val == f_val):
    print("The temp converter works!")
else:
    print("The temp converter failed!")