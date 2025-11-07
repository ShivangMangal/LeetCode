class Solution {
    public boolean isPowerOfTwo(int n) {
        // A number less than or equal to 0 cannot be a power of two
        if (n <= 0) return false;
        
        // A power of two has exactly one bit set in its binary representation
        // Example: 1 (0001), 2 (0010), 4 (0100), 8 (1000)
        return (n & (n - 1)) == 0;
    }
}
