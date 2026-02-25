import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] sortByBits(int[] arr) {
        // We convert to Integer[] to use a custom Comparator
        Integer[] boxedArray = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) {
            boxedArray[i] = arr[i];
        }

        Arrays.sort(boxedArray, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int bitCountA = Integer.bitCount(a);
                int bitCountB = Integer.bitCount(b);
                
                // If bit counts are different, sort by bit count
                if (bitCountA != bitCountB) {
                    return bitCountA - bitCountB;
                }
                // If bit counts are the same, sort by the value itself
                return a - b;
            }
        });

        // Convert back to primitive int[]
        for (int i = 0; i < arr.length; i++) {
            arr[i] = boxedArray[i];
        }
        
        return arr;
    }
}