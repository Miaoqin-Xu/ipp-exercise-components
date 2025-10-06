import sys

# You can use any name, and as many as you'd like, but make sure each list (or tuple) is the same length
fruitNames = ("apples", "peaches", "pineapples", "apples", "blueberries", "oranges", "kiwi")
fruitLocations = ("Massachusetts", "Georgia", "Hawaii", "Washington", "Maine", "Florida", "California")

def createDictionaryFromKeyValuePairs(names, locations):
    """"Create a dictionary by pairing names with locations.

    Keyword arguments:
    names     -- iterable of keys (e.g., list of names)
    locations -- iterable of values; must align with names in length
    """
    itemDict = None

    if names is not None and locations is not None:
        if len(names) == len(locations):
            itemDict = {}

            print(f"Length of item names and item locations are the same. Creating dictionary of size {len(names)}")

            index = 0
            for n in names:
                itemDict[n] = locations[index]
                index = index + 1
        else:
            print(f"Can't create dictionary of names and locations. Lengths of lists are different.")

    return itemDict
def mergeDictionaries(*args):
    """Merge two or more dictionaries into one; later ones overwrite earlier keys.

    Keyword arguments:
    *args -- variable number of dict objects to merge
    """
    mergedDict = dict()
    #mergedDict = {}

    if (args and len(args) > 0):
        for arg in args:
            if (arg is not None):
                print(f"Merging dictionary into main dictionary with {len(arg)} items.")
                mergedDict = mergedDict | arg
                print(f"Newly merged dictionary: {mergedDict}")

        return mergedDict
    else:
        print("No dictionaries included in arguments to function. Ignoring.")

    return mergedDict
def addItemsToDictionary(itemDict, **kwargs):
    """Add one or more key/value items to the dictionary.

    Keyword arguments:
    itemDict -- target dictionary to update
    **kwargs -- items as key=value; existing keys will be overwritten
    """
    # NOTE: we have to be explicit about checking if itemDict
    # is not None, as the boolean eval (if itemDict:) will
    # return false if the set is empty
    if itemDict is not None:
        if (kwargs and len(kwargs) > 0):
            for k, v in kwargs.items():
                if (k is not None and v is not None):
                    print(f"Adding key {k} and value {v} to dictionary of length {len(itemDict)} items.")
                    itemDict[k] = v
                    print(f"New dictionary length: {len(itemDict)}")
    
    return itemDict
def removeItemsFromDictionary(itemDict, *args):
    """Safely remove one or more keys from the dictionary.

    Keyword arguments:
    itemDict -- target dictionary
    *args    -- keys to remove; missing keys are ignored
    """
    # NOTE: we have to be explicit about checking if itemDict
    # is not None, as the boolean eval (if itemDict:) will
    # return false if the set is empty
    if itemDict is not None:
        if (args and len(args) > 0):
            for arg in args:
                if (arg is not None):
                    print(f"Removing key {arg} from dictionary of length {len(itemDict)} items.")
                    
                    # NOTE: there are other ways, but this avoids raising an exception
                    # if 'arg' is not a key in the dictionary
                    itemDict.pop(arg, None)
                    print(f"New dictionary length: {len(itemDict)}")

    return itemDict

def main():
 
    fruitNames   = ["apples", "peaches", "pineapples", "apples"]
    fruitLocs    = ["MA", "GA", "HI", "WA"]

    d1 = createDictionaryFromKeyValuePairs(fruitNames, fruitLocs)
    print("d1:", d1)

    d2 = {"apples": "NY", "oranges": "FL"}
    merged = mergeDictionaries(d1, d2)
    print("merged:", merged)

    addItemsToDictionary(merged, bananas="CA", apples="TX") 
    print("after add:", merged)

    removeItemsFromDictionary(merged, "oranges", "no-such-key") 
    print("after remove:", merged)
    return 0

if __name__ == "__main__":
    sys.exit(main())