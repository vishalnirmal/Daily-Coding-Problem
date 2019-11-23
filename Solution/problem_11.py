# # Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
suggestions = []

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add(self, remaining, word):
        exists = False
        for child in self.children:
            if remaining[0] == child.val:
                exists = True
                if len(remaining) > 1:
                    child.add(remaining[1:], word)
                else:
                    child.children.append(Node(word))
        
        if not exists:
            tnode = Node(remaining[0])
            self.children.append(tnode)
            if len(remaining) > 1:
                tnode.add(remaining[1:], word)
            else:
                tnode.children.append(Node(word))
    

    def findSuggestion(self):
        if self.children == []:
            suggestions.append(self.val)
        else:
            for child in self.children:
                child.findSuggestion()
    
    def find(self, query):
        if query == '':
            self.findSuggestion()
            return 
        for child in self.children:
            if query[0] == child.val:
                child.find(query[1:])
    
    def print(self):
        print(self.val, end='->')
        for child in self.children:
            print(child.val, end=' ')
        print()
        for child in self.children:
            print(child.val,':')
            child.print()

if __name__ == "__main__":
    strings = ['dog', 'deer', 'deal']
    query = 'd'
    root = Node('root')
    for word in strings:
        root.add(word, word)
    root.find(query)

    print(suggestions)