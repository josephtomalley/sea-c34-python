"""What is going on with the '0:100:x method of string slicing?"""


def stringslicer(x):
    string = range(100)
    print string[0:100:x]
stringslicer()

"""Answer: The 3rd part of the slicing method controls
how big a chunk of a string is sliced out"""

"""What happens when you use an negative index on a
string beyond the beginning range? Does it error in the same way?"""


def negativeindex(x):
    s = "This is a string"
    print s[x]
negativeindex(-20)

"""Answer: Yes, you get the same type of error."""

"""What happens when you try to tuple a list?"""


def listtupler(list):
    tuple(list)
    print list
    list2 = tuple(list)
    print list2
listtupler([45, 'cat', 5.0])

"""Answer: Calling tuple() on a list does not change the list,
but, declaring a new variable as a list that has been tupled
does create a tuple."""
