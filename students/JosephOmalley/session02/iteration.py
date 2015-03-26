"""Can I use enumerate on lists?"""
list = ["cat", "dog", "bird"]
for i in enumerate(list):
    print i
"""Yes, you can enumerate lists."""

"""Does range() work on strings?"""
for i in range("string"):
    print i
"""Nope, it doesn't let you do that."""

"""What happens when you try to enumerate range?"""
for i in enumerate(range(10)):
    print i
"""Yes, that works too."""
