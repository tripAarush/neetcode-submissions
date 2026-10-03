class PrefixTree:

    def __init__(self, char=''):
        self.char = char
        self.children = []
        self.end = False

    def insert(self, word: str) -> None:
        def dfs(node, idx):
            if idx>=len(word):
                node.end = True
                return

            for ch in node.children:
                if ch.char == word[idx]:
                    dfs(ch,idx+1)
                    return

            new_node = PrefixTree(word[idx])
            node.children.append(new_node)
            dfs(new_node,idx+1)
        
        dfs(self,0)
            
    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx>=len(word):
                return True if node.end else False
            
            for ch in node.children:
                if ch.char == word[idx]:
                    return dfs(ch, idx+1)
            
            return False
        
        return dfs(self,0)

    def startsWith(self, prefix: str) -> bool:
        def dfs(node, idx):
            if idx>=len(prefix):
                return True
            
            for ch in node.children:
                if ch.char == prefix[idx]:
                    return dfs(ch, idx+1)
            
            return False
        
        return dfs(self,0)
        