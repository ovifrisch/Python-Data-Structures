"""Suffix Tree Implementation"""


class SuffixTree:
    """Suffix Tree class

    Attributes:
        root: the root of the tree
    """

    def __init__(self):
        """Init"""
        self.root = None


    def add_strings(self, strings):
        """Add the strings to the suffix tree
        
        Args:
            strings: A list of strings
        """
        pass

    def get_strings(self):
        """Get all the strings in the suffix tree

        Returns:
            A list of strings
        """
        pass

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



