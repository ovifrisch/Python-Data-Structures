"""Suffix Tree Implementation"""


class SuffixTree:
    """Suffix Tree class

    Attributes:
        root: the root of the tree
        termination_symbols: List of special symbols used to terminate strings. These
           cannot be part of any input string to the tree
        strings: A list of strings currently in the tree (must not exceed length of
           termination symbols)
    """

    def __init__(self):
        """Init"""
        self.root = None
        self.termination_symbols = ['$', '@', '%', '&', '*', '~', '!', '+', '#', '^']
        self.strings = []


    def add_strings(self, strings):
        """Add the strings to the suffix tree

        If the addition of strings to the tree causes it to go over
        capacity, none of the strings are added and an Exception is
        thrown. Similarly, if any of the strings contains a termination
        symbol, none of the strings are added and an Exception is
        thrown
        
        Args:
            strings: A list of strings

        Raises:
            Tree at Capacity: tree is at capacity so no more strings can be added
            Illegal Character: one of the strings contains an illegal character
        """
        if len(strings) + len(self.strings) > len(self.termination_symbols):
            raise Exception("Tree at Capacity")

        if (sum(map(lambda x: sum(map(lambda y: y in self.termination_symbols, x)) != 0, strings)) > 0):
            raise Exception("Illegal Character")

        self.strings += strings
        for string in strings:
            self.__add_string(string)
            self.strings += [string]

    def get_strings(self):
        """Get all the strings in the suffix tree

        Returns:
            A list of strings
        """
        return self.strings

    def longest_common_substring(self, strings=None):
        """Computes the LCS of all the strings in this suffix tree

        Args:
            strings (optional): The strings to consider in the LCS

        Returns:
            A string denoting the LCS of all the strings in the tree

        Raises:
            String Not Found: If strings is provided but at least one of them does not exist
        """
        pass

    def __add_string(self, string):
        """Add the string to the tree

        Args:
            string: the string to add
        """
        term_symb = self.termination_symbols[len(self.strings)]

    def longest_repeated_substring(self, str_=None):
        """Computers the LRS of each string in the tree

        Args:
            str_ (optional): the string to find the LRS for
    
        Returns:
            If str_ is not provided, a list containing the LRS of each string in the tree
            If str_ is provided, a string denoting the LRS of str_

        Raises:
            String Not Found: If str_ is provided but does not exist in the tree
        """
        pass

    def longest_palindrome(self, str_=None):
        """Computers the longest palindrome of each string in the tree

        Args:
            str_ (optional): the string to find the longest palindrome for
    
        Returns:
            If str_ is not provided, a list containing the longest palindromes of each string in the tree
            If str_ is provided, a string denoting the longest palindrome of str_

        Raises:
            String Not Found: If str_ is provided but does not exist in the tree
        """
        pass



