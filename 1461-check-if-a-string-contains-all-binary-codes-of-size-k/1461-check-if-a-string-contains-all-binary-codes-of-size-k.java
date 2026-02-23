import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean hasAllCodes(String s, int k) {
        // Total unique binary codes needed is 2^k
        int requiredCount = 1 << k; 
        
        // Quick optimization: if the string isn't long enough to hold all codes
        if (s.length() - k + 1 < requiredCount) {
            return false;
        }

        Set<String> seenCodes = new HashSet<>();

        // Iterate through s and extract substrings of length k
        for (int i = 0; i <= s.length() - k; i++) {
            String sub = s.substring(i, i + k);
            seenCodes.add(sub);
            
            // If we've already found everything, we can stop early
            if (seenCodes.size() == requiredCount) {
                return true;
            }
        }

        return seenCodes.size() == requiredCount;
    }
}