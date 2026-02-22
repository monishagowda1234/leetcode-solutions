class Solution {
    public int binaryGap(int n) {
        int maxDist = 0;
        int lastPos = -1;
        int currentPos = 0;

        while (n > 0) {
            // Check if the current rightmost bit is 1
            if ((n & 1) == 1) {
                if (lastPos != -1) {
                    // Update maxDist if the new gap is larger
                    maxDist = Math.max(maxDist, currentPos - lastPos);
                }
                // Update the position of the most recent 1
                lastPos = currentPos;
            }

            // Shift bits to the right by 1
            n >>= 1;
            currentPos++;
        }

        return maxDist;
    }
}