class Solution {
    public int maxRepeating(String sequence, String word) {
        int k = 0;
        String repeat = word;
        while (sequence.contains(repeat)) {
            k++;
            repeat += word;
        }
        return k;
    }
}
