"""Implement a class called TreeDict that supports operators the same
way as a dict. 

TreeDict should be implemented using the binarysearchtree module I
have provided (you can download it from canvas in the same folder as
this file).

You need to make sure you support the following operations with the
same semantics as a normal Python dict:
* td[key]
* td[key] = value
* key in td
* td.get(key)
* td.get(key, default)
* td.update(iterable_of_pairs_or_dict_or_TreeDict)
* len(td)
* for key in td: pass
* for key, value in td.items(): pass
* A constructor: TreeDict(iterable_of_pairs_or_dict_or_TreeDict)

Iteration should be in key order, this should be pretty easy to do
just by traversing the tree using an in-order traversal. None of the
iterator methods should make a copy of any of the data in the
TreeDict. You should only implement in-order traversal once and use
that implementation for both kinds of traversal.

You should support a constructor which takes the same arguments as
update and creates a TreeDict with just those values. There is an easy
way to do this in just a couple of lines using your existing update
method.

For each operation, make sure it does the same thing as a dict and you
handle errors by throwing the same type of exception as would be
thrown by a dict. However you only need to handle the operations
listed above, not all operations supported by dict. Unlike dict your
implementation will not support None as a key and you should throw an
appropriate exception if None is used as a key. Look at the available
built in exceptions and pick the most appropriate one you find.

Most of these methods will be very short (just a couple of lines of
code), a couple will be a bit more complicated. However all the hard
work should already be handled by the binarysearchtree module. It
looks like a lot of operations, but it shouldn't actually take that
long. Many of the operations are quite similar as well.

Do not reimplement anything in the binarysearchtree module or copy
code from it. You should not need to.

For this assignment I expect you will have to use at least the
following things you have learned:
* Raising exceptions
* Catching exceptions
* Implementing magic methods
* Generators using yield (and you will need to look up "yield from" in the Python documentation)
* Type checks
* Default values/optional arguments

You will also need to read code which I think will help you learn to
think in and use Python.

To reiterate some of the things you should be aware of to avoid losing
points:
* None of the iterator methods should make a copy of any of the data
  in the TreeDict.
* You should only implement in-order traversal once and it should be
  recursive (it's so much easier that way).
* Do not reimplement anything in the binarysearchtree module or copy
  code from it.
* There are easy ways to implement all the required operations. If
  your implementation of a method is long you may want to think if
  there is a simpler way.

Links:
* https://docs.python.org/3.5/library/stdtypes.html#dict
* http://en.wikipedia.org/wiki/Binary_search_tree#Traversal
* https://docs.python.org/3.5/reference/expressions.html#yieldexpr

"""

import binarysearchtree

class TreeDict:
    
    def __init__(self, iterable = None):
        self.root = binarysearchtree.Node()
        self.keys = []
        if iterable is None:
            self.values = []
        elif isinstance(iterable, dict) or isinstance(iterable, TreeDict):
            for key, value in iterable.items():
                self.root.insert(key, value)
                self.keys.append(key)
        else:
            iterable = list(iterable)
            for item in iterable:
                self.root.insert(item[0], item[1])
                self.keys.append(item[0])
        
    
    def __getitem__(self, key):
        try:
            return self.root.lookup(key).value
        except ValueError as e:
            raise KeyError(str(key))
    
    def get(self, key, second = None):
        if key is None:
            raise ValueError()
            raise TypeError()
            raise KeyError()
        try:
            return self.root.lookup(key).value
        except ValueError as e:
            return second
    
    def __setitem__(self, key, value):
        if self.__contains__(key) == False:
            self.keys.append(key)
        self.root.insert(key, value)
        
    def update(self, iterable = None):
        if isinstance(iterable, dict) or isinstance(iterable, TreeDict):
            for key, value in iterable.items():
                if self.__contains__(key) == False:
                    self.keys.append(key)
                self.root.insert(key, value)
        else:
            iterable = list(iterable)
            if len(iterable[0]) < 2:
                raise Exception()
            for item in iterable:
                if self.__contains__(item[0]) == False:
                    self.keys.append(item[0])
                self.root.insert(item[0], item[1])
    
    def __contains__(self, key):
        try:
            self.root.lookup(key)
            return True
        except ValueError as e:
            return False
        
    def __len__(self):
        return len(self.keys)
    
    def inorder(self, tree):
        if tree == None or tree.key == None:
            return
        yield from self.inorder(tree.left)
        yield tree.key
        yield from self.inorder(tree.right)
    
    def __iter__(self):
        return self.inorder(self.root)
    
    def inorder2(self, tree):
        if tree == None or tree.key == None:
            return
        yield from self.inorder2(tree.left)
        yield (tree.key, tree.value)
        yield from self.inorder2(tree.right)
    
    def items(self):
        return self.inorder2(self.root)