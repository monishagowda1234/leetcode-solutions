class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:  # s[i] == ')'
                # Check if the next character is also ')'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Missing one ')'
                    insertions += 1
                    i += 1
                
                # Consume an open parenthesis if available
                if open_count > 0:
                    open_count -= 1
                else:
                    # Need to insert an '(' for this '))'
                    insertions += 1
                    
        # For every remaining open parenthesis, we need two ')'
        insertions += open_count * 2
        return insertions