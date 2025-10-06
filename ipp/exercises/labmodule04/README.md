# Programming in Python - An Introduction: Lab Module 04

### Description

Briefly describe the objectives of the Lab Module:

1) worked with array, sets and dictionaries

2) 

3) 


### Exercise Activities

List the actions you took in implementing the Lab Module:

1) dig into the codes and write comments for it, finding it's possible problems

2) 

3) 


### Unit and/or Integration Tests Executed

List the tests you exercised in validating your functionality for the Lab Module:

1) createDictionaryFromKeyValuePairs

2) mergeDictionaries(*args)

3) addItemsToDictionary and removeItemsFromDictionary


What's happening with this code? Why are the float values so... odd?
The code array('f', values) are stored as 32 bit floats, and most decimals cannot be represented exacly in binary, so when printing array python converts those 32 bit value back to 64 bit causing a rounding error.

What's happening with this code? Why are the double values represented the way they are?
This function creates an array using double precision (64-bit) floats, which matches Python's default float precision. The values are represented accurately without the precision loss seen in single-precision floats.
    
What's happening with this code?
It converts the input list of names to a set, which removes duplicates and does not preserve order.

What's happening with this code? Specifically, what does *args do?
*arg means give me as many you'd like, and will collect variable number of positioinal arguments into a tuple
What's happening with this code? What would happen if you added one or more items of the same name?
The function iterates through *args and adds each item to nameSet. It would overwrite.

What's happening with this code? What would happen if you removed an item that doesn't exist in the set?
It iterates through the items and safely removes each one using set.discard(arg). Discard deletes the element if it exists, if it doesn’t exist, it does nothing.

What's happening with this code? What are the potential issues with this code? How would you resolve these potential issues?
The code pairs up names and locations, if the keys are the same it will be overwrite by the last one. change key names to different names and could use defaultdict(list)to collect all values

What's happening with this code? Specifically, what does *args do?
it takes in as many dict and merge them in order, the last same key will overwrite the previous one.

What's happening with this code? What would happen if you added one or more items of the same name?
**kwargs made numerous key=value into dict, if key already exist, the new value will overwrite old value. Length will only increase if the key is different.

What's happening with this code? What would happen if you removed an item that doesn't exist in the dictionary?
use pop to safely remove, if key doesn't exist it wil not come up with error.


EOF.
