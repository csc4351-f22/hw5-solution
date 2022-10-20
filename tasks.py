
def task_1(s):
    count = 0  # I'm too lazy to make two variables so we're going to increment and decrement the same one for vowels/consonants.
    for char in s:
        if char in {'a', 'e', 'i', 'o', 'u'}: # <-- that's a set literal. Also y is not a vowel today.
            count += 1
        else:
            count -= 1  # this will count things like spaces and punctuation as consonants
                        # if we were REALLY worried, we could use ord() to get the actual ASCII
                        # value of each character and check if it's in a given range
    
    if count == 0:
        return None
    return count > 0  # note that this will evalute to True iff there are more vowels than consonants

def task_2(r):
    from math import pi  # yep, you can import anywhere in a file (although it would be better practice to do this at the top)
    return 4/3*pi*r**3

def task_3(list_of_words):
    return ",".join(list_of_words) # this is the opposite of split() -- it adds a comma between each pair of words, but doesn't add a trailing one

def task_4(list_of_lists_of_strings, filename):
    # not gonna use the CSV library, although that would probably be easier
    with open(filename, "w") as f:  # need to use "w" to indicate we're "w"riting to the file
        for list_of_strings in list_of_lists_of_strings:
            f.write(task_3(list_of_strings))
            f.write("\n") # need a newline at the end

def task_5(filename):
    res = []
    with open(filename) as f:
        for line in f:
            res.append(line.strip().split(","))  # strip() removes whitespace and other garbage, split creates a list out of 
                                                 # everything separated by commas
    return res

def task_6(arg1, arg2):
    try:
        return arg1 + arg2
    except TypeError:
        # type() will print out the variable type 
        # the "f" at the beginning of the string tells Python to evaluate expressions in the {} braces
        print(f"You oaf! You tried to add a {type(arg1)} and a {type(arg2)}")
        return 0  # probably best to keep the return types consistent

def task_7(nums):
    res = []

    # make a dictionary with the number of occurrences of each number
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1
    
    for num in nums:
        if count[num] > 1:
            res.append(num)
    
    return res