import sys
import SimpleTempConversion

def do_Work():
    f_val = 72.0
    
    c_val = SimpleTempConversion.convert_Temp_F_to_C(f_val)

    print(f"Converted temperature values: F = {f_val}, C = {c_val}")

def main():
    print("Hello, world!")
    do_Work()
    return 0

if __name__ == "__main__":
    sys.exit(main())
