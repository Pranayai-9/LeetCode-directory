class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
            
        # Dictionary to track visited nodes and their clones
        old_to_new = {}
        
        def dfs(current_node):
            # If already cloned, return the existing clone
            if current_node in old_to_new:
                return old_to_new[current_node]
                
            # Create a clone for the current node
            clone = Node(current_node.val)
            old_to_new[current_node] = clone
            
            # Recursively clone and add all neighbors
            for neighbor in current_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        return dfs(node)
