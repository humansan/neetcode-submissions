class TrieNode:
    def __init__(self, children = None, eow = False):
        self.children = children if children else {}
        self.eow = eow

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        found_words = []

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.eow = True
        
        def dfs(x, y, node, word):
            # if node is eow return true
            # check if char is in node's children, if so set that node as cur
            # pass cur node
            # explore adjacent squares if in bound and not visited
            # to mark as visited in current search store char, and set to #
            # return true if any dfs returns true
            # unmark # before exiting or returning
            

            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != "#" and board[x][y] in node.children:
                char = board[x][y]
                cur_node = node.children[char]
                word += char

                if cur_node.eow:
                    found_words.append(word)
                    cur_node.eow = False

                board[x][y] = "#"

                dfs(x - 1, y, cur_node, word) 
                dfs(x + 1, y, cur_node, word)
                dfs(x, y - 1, cur_node, word) 
                dfs(x, y + 1, cur_node, word)

                board[x][y] = char

                if not cur_node.eow and not cur_node.children:
                    node.children.pop(char, None)

                            
            # if node.eow:
            #     found_words.append(word)
            #     return True
            # if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != "#" and board[x][y] in node.children:
            #     word += char
            #     cur_node = node.children[char]
            #     board[x][y] = "#"
            #     res = dfs(x - 1, y, cur_node, word) or 
            #             dfs(x + 1, y, cur_node, word) or
            #             dfs(x, y - 1, cur_node, word) or 
            #             dfs(x, y + 1, cur_node, word)

            #     board[x][y] = char
            #     return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, "")

        return found_words



                    
        