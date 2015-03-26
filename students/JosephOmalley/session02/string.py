"""What does a string look like when sorted by ASCII code?"""


def asciiname(x):
    name = []
    sortedname = []
    for i in x:
        name.append(ord(i))
    name.sort()
    for i in name:
        sortedname.append(chr(i))
    print sortedname
asciiname("Joseph Thomas O'Malley")

"""Answer: This code produces: [' ', ' ', "'", 'J', 'M', 'O', 'T', 
'a', 'a', 'e', 'e', 'h', 'h', 'l', 'l', 'm', 'o', 'o', 'p', 's', 's', 'y']"""

"""What happens when you split a string using a letter?"""


def stringsplitter(x):
    string = "wqelukhnveksurhvnierufaekufgniveurhnvezdcn"
    print string.split('x')
stringsplitter('e')
 
"""Answer: ['wq', 'lukhnv', 'ksurhvni', 'rufa', 'kufgniv', 'urhnv', 'zdcn']
It splits the string where the letter is but also removes it."""

"""Can you perform operations on string placeholders?"""


def meowamount(x):
    statement = "the cat said: %s" % ("meow" * x)
    print statement
meowamount(10)

"""Answer: the cat said: meowmeowmeowmeowmeowmeowmeowmeowmeowmeow.
Yes you can"""



    