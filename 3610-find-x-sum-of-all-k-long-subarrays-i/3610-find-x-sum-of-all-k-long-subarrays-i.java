import java.util.*;
class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        for (int i = 0; i <= n - k; i++) {
            int[] sub = Arrays.copyOfRange(nums, i, i + k);
            Map<Integer, Integer> freq = new HashMap<>();
            for (int num : sub) {
                freq.put(num, freq.getOrDefault(num, 0) + 1);
            }
            List<Integer> elements = new ArrayList<>(freq.keySet());
            elements.sort((a, b) -> {
                if (!freq.get(a).equals(freq.get(b))) 
                    return freq.get(b) - freq.get(a);
                else 
                    return b - a;
            });
            Set<Integer> keep = new HashSet<>();
            for (int j = 0; j < Math.min(x, elements.size()); j++) {
                keep.add(elements.get(j));
            }
            int sum = 0;
            for (int num : sub) {
                if (keep.contains(num)) sum += num;
            }
            ans[i] = sum;
        }
        return ans;
    }
}
