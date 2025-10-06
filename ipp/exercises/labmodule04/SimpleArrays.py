import sys
import struct

from array import array

# You can use any float value (2 decimal places), and as many as you'd like,
# as long as you have at least 3 entries
values = [2.99, 5.99, 3.99, 7.99, 1.99]

def displaySizingInfo(val):
    """Display size and representation details of a floating-point value.

    Keyword arguments:
    val -- floating-point value to analyze
"""
    sampleBits = sys.getsizeof(val)
    sampleHex = val.hex()
    sampleBin = struct.unpack('!I', struct.pack('!f', val))[0]        

    print(" -> Sizing info: value =", val, ", bits =", sampleBits, ", hex =", sampleHex, ", binary =", f"{sampleBin:032b}")

def createItemPriceArrayUsingFloats():
    """
    Create an array of float prices and display the representation

    Keyword arguments:
    None

    Returns:
    itemPrices -- array('d') of double-precision floats
"""
    itemPrices = array('f', values)

    print(itemPrices)
    print(itemPrices.tolist())

    for i, val in enumerate(itemPrices):
        displaySizingInfo(val)

    return itemPrices

def createItemPriceArrayUsingDoubles():
    """Create an array of double prices and display their representations.

    Returns:
    itemPrices -- array('d') of double-precision floats
    """
    itemPrices = array('d', values)

    print(itemPrices)
    print(itemPrices.tolist())

    for i, val in enumerate(itemPrices):
        displaySizingInfo(val)

    return itemPrices

def main():
	createItemPriceArrayUsingFloats()
    createItemPriceArrayUsingDoubles()
	
    return 0

if __name__ == '__main__':
	sys.exit(main())