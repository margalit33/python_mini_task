# tools/col.py



"""
    A simple wrapper for the built-in zip function.
    
    Args:
    it1: The first iterable collection.
    it2: The second iterable collection.
    
    Returns:
    An iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
    """
def myzip(it1, it2):
    return zip(it1, it2)

