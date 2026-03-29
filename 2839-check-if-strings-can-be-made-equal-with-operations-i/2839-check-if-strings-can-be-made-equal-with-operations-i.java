class Solution {
    public boolean canBeEqual(String s1, String s2) {
        char[] s1Even = {s1.charAt(0), s1.charAt(2)};
        char[] s1Odd = {s1.charAt(1), s1.charAt(3)};
        
        char[] s2Even = {s2.charAt(0), s2.charAt(2)};
        char[] s2Odd = {s2.charAt(1), s2.charAt(3)};
        
        java.util.Arrays.sort(s1Even);
        java.util.Arrays.sort(s1Odd);
        java.util.Arrays.sort(s2Even);
        java.util.Arrays.sort(s2Odd);
        
        return java.util.Arrays.equals(s1Even, s2Even) &&
               java.util.Arrays.equals(s1Odd, s2Odd);
    }
}