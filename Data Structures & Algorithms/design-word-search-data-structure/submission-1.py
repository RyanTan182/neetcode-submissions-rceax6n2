class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False 

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                new_node = TrieNode()
                curr.children[index] = new_node
            curr = curr.children[index]

        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children:
                        if child is not None and dfs(i + 1, child):
                            return True
                    return False
                else:
                    index = ord(c) - ord('a')
                    if curr.children[index] is None:
                        return False
                    curr = curr.children[index]
            return curr.isEndOfWord
        return dfs(0, self.root)

        
