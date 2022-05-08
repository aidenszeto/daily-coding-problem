'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

def autocomplete(s, queries):
    length = len(s)
    output = []
    for query in queries:
        if query[:length] == s:
            output.append(query)
    return output

query_strings = ["dog", "deer", "deal"]
print(autocomplete("de", query_strings))