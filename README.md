# DIY-Python-Projects (being populated with increasing order of difficulty)
This repository contains pet DIY problems sourced from the web/books. 100% original codes (clarity helps, never hurts)

A brief description of the functions are given below:

**collatz()**: 
It is conjectured but not yet proven that no matter which positive integer we start with; we always end up with 1.
More details here https://www.geeksforgeeks.org/collatz-sequence/

**comma_code()**: 
Say you have a list value like this: spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and 
a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 
'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

**displayInventory**():

The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item 
in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary 
value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means theplayer has 1 rope, 6 torches, 42 gold coins,
and so on. Write a function named displayInventory() that would take any possible “inventory” and display it.

**addToInventory**():

Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the 
player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory()
function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples 
of the same item.

**printTable**():

Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],

['Alice', 'Bob', 'Carol', 'David'],

['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

apples Alice dogs

oranges Bob cats

cherries Carol moose

banana David goose
