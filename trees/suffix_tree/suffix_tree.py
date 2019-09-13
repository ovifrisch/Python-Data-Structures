"""Suffix Tree Implementation"""


class TreeNode:

    def __init__(self, substr, children=None):
        self.substr = substr
        if not children:
            self.children = []
        else:
            self.children = children


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
        self.root = TreeNode("")
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

        for string in strings:
            for c in string:
                if (c in self.termination_symbols):
                    raise Exception("Illegal Character")

        suffixes = self.get_suffixes(strings)
        for suffix in suffixes:
            self.__add_string(suffix)


    def get_suffixes(self, strings):
        res = []
        for string in strings:
            sym = self.termination_symbols[len(self.strings)]
            res += [string[i:] + sym for i in range(len(string) + 1)]
            self.strings.append(string)
        return sorted(res, key=lambda x: len(x))

    def get_strings(self):
        """Get all the strings in the suffix tree

        Returns:
            A list of strings
        """
        return self.strings

    def __longest_common_prefix(self, str1, str2):
        idx = 0
        while (idx < len(str1) and idx < len(str2) and str1[idx] == str2[idx]):
            idx += 1
        return idx



    def __add_string(self, string):
        """Add the string to the tree

        Args:
            string: the string to add
        """

        def helper(node, str_):

            if (not str_):
                return

            """find the index of the head char"""
            start_chars = [x[0] for x in [y.substr for y in node.children]]

            # if not exists, create a new child and return
            if str_[0] not in start_chars:
                node.children.append(TreeNode(str_))
                return

            # the child's index
            child_idx = start_chars.index(str_[0])


            # if the child's substr is a prefix of this string, then recurse

            child_substr = node.children[child_idx].substr
            child_len = len(child_substr)
            if (child_len < len(str_) and str_[:child_len] == child_substr):
                helper(node.children[child_idx], str_[child_len:])
                return

            # find the prefix to preserve
            new_substr_len = self.__longest_common_prefix(str_, node.children[child_idx].substr)
            node.children[child_idx].substr = node.children[child_idx].substr[new_substr_len:]
            new_node = TreeNode(str_[:new_substr_len], [node.children[child_idx]])
            node.children.pop(child_idx)
            node.children.append(new_node)
            helper(node.children[-1], str_[new_substr_len:])

        helper(self.root, string)

    def get_suffixes_from_tree(self):

        result = []
        def helper(node, curr_str):
            if (node.substr and node.substr[-1] in self.termination_symbols):
                result.append(curr_str + node.substr)

            for child in node.children:
                helper(child, curr_str + node.substr)

        helper(self.root, "")
        return result


    def longest_common_substring(self, strings=None):
        """Computes the LCS of all the strings in this suffix tree

        Args:
            strings (optional): The strings to consider in the LCS

        Returns:
            A string denoting the LCS of all the strings in the tree

        Raises:
            String Not Found: If strings is provided but at least one of them does not exist
        """

        if (not strings):
            strings = self.strings

        if (len(list(filter(lambda x: x not in self.strings, strings))) > 0):
            raise Exception("String Not Found")

        if (len(strings) < 2):
            raise Exception("Not Enough Strings")

        symbs = set()
        for string in strings:
            # find the associated symbol in termination symbols
            for idx, symb in enumerate(self.strings):
                if (self.strings[idx] == string and self.termination_symbols[idx] not in symbs):
                    symbs.add(self.termination_symbols[idx])

        max_str = ""

        def helper(node, curr_str):
            nonlocal max_str
            curr_str += node.substr
            found = set()
            if (node.substr and node.substr[-1] in symbs):
                found.add(node.substr[-1])

            for child in node.children:
                for symb in helper(child, curr_str):
                    found.add(symb)

            if (set(found) == set(symbs)):
                if (len(max_str) < len(curr_str)):
                    max_str = curr_str
            return found


        helper(self.root, "")
        return max_str




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
        strings = self.strings
        if (str_):
            if (str_ not in strings):
                raise Exception("String Not Found")
            strings = [str_]


        def single_string(string):
            symb = self.termination_symbols[self.strings.index(string)]
            """
            Observation: If a substring is repeated in string,
            then it is an internal node in the suffix tree.

            Observation 2: If a substribng is the longest
            repeated in a string, it is the "deepest" internal
            node in the string.

            When we find an internal node, we must only include it
            as a candidate if one of its children ends in the target
            termination symbol.
            """
            max_repeat = ""
            def helper(node, curr_str):
                nonlocal max_repeat

                if (node.substr and node.substr[-1] in self.termination_symbols):
                    if (node.substr[-1] == symb):
                        return True
                    return False

                curr_str += node.substr
                is_str = []
                for child in node.children:
                    is_str.append(helper(child, curr_str))
                if (sum(is_str) > 1):
                    if (len(curr_str) > len(max_repeat)):
                        max_repeat = curr_str

                return sum(is_str) > 1

            helper(self.root, "")
            return max_repeat


        res = []
        for string in strings:
            res.append(single_string(string))

        if (str_):
            return res[0]
        return res
                








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

if __name__ == "__main__":
    t = SuffixTree()
    strings = ["aaa"]
    t.add_strings(strings)
    # print(t.contains_null())



