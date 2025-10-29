import sys

# You can use any name, and as many as you'd like,
# as long as you have at least 3 that are duplicates
fruitNamesA = ["apples", "peaches", "bananas", "apples", "blueberries", "bananas", "oranges", "oranges"]
fruitNamesB = ["apples", "oranges", "kiwi", "pineapple", "apples", "cherries", "cherries", "watermelon"]

def createSetFromNames(names):
    """Create a set from a list of names and display unique contents.

    Keyword arguments:
    names -- list (or iterable) of names; duplicates will be removed
    """
    nameSet = None

    if names is not None:
        nameSet = set(names)

    return nameSet

def mergeSetNames(*args):
    """Merge two or more name sets into a single set (union).

    Keyword arguments:
    *args -- variable number of set objects to merge

    """
    mergedSet = set()

    if (args and len(args) > 0):
        for arg in args:
            if (arg is not None):
                print(f"Merging set into main set with {len(arg)} items.")
                mergedSet = mergedSet | arg
                print(f"Newly merged set: {mergedSet}")

        return mergedSet
    else:
        print("No sets included in arguments to function. Ignoring.")

    return mergedSet

def addItemsToSet(nameSet, *args):
    """Add one or more items to the given name set.

    Keyword arguments:
    nameSet -- target set to be updated
    *args   -- items to add; duplicates have no effect

    """
    # NOTE: we have to be explicit about checking if uniqueItems
    # is not None, as the boolean eval (if uniqueItems:) will
    # return false if the set is empty
    if nameSet is not None:
        if (args and len(args) > 0):
            for arg in args:
                if (arg is not None):
                    print(f"Adding item {arg} to set of length {len(nameSet)} items.")
                    nameSet.add(arg)
                    print(f"New set length: {len(nameSet)}")
    
    return nameSet

def removeItemsFromSet(nameSet, *args):
    """Safely remove one or more items from a given set.

    Keyword arguments:
    nameSet -- target set to be updated
    *args   -- items to remove; missing items are ignored 

    """
    # NOTE: we have to be explicit about checking if uniqueItems
    # is not None, as the boolean eval (if uniqueItems:) will
    # return false if the set is empty
    if nameSet is not None:
        if (args and len(args) > 0):
            for arg in args:
                if (arg is not None):
                    print(f"Removing item {arg} from set of length {len(nameSet)} items.")
                    
                    # NOTE: remove() works too, but will raise an exception if 'arg' isn't found
                    nameSet.discard(arg)
                    print(f"New set length: {len(nameSet)}")

    return nameSet

def main():
    fruitNamesA = ["apples", "peaches", "bananas", "apples", "blueberries", "bananas"]
    fruitNamesB = ["apples", "oranges", "kiwi", "pineapple", "apples", "cherries"]
    
    setA = createSetFromNames(fruitNamesA)
    setB = createSetFromNames(fruitNamesB)
    print("Set A:", setA)
    print("Set B:", setB)


    merged = mergeSetNames(setA, setB)
    print("Merged set:", merged)

   
    addItemsToSet(merged, "apples", "dragonfruit", "kiwi", "kiwi")
    print("After add:", merged)
    
    removeItemsFromSet(merged, "bananas", "papaya")
    print("After remove:", merged)

    return 0

if __name__ == "__main__":
    sys.exit(main())