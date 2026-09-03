class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Count characters in s1
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        # Sliding window over s2
        window = {}
        for r in range(len(s2)):
            # Add right character
            char = s2[r]
            window[char] = window.get(char, 0) + 1
            
            # Remove left character when window is too large
            if r >= len(s1):
                left_char = s2[r - len(s1)]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
            
            # Check if current window matches s1
            if window == s1_count:
                return True
        
        return False