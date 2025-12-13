import java.util.*;
class Solution {
    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        int n = code.length;
        Map<String, Integer> order = new HashMap<>();
        order.put("electronics", 0);
        order.put("grocery", 1);
        order.put("pharmacy", 2);
        order.put("restaurant", 3);
        List<String[]> valid = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!isActive[i]) continue;

            if (!order.containsKey(businessLine[i])) continue;

            if (code[i] == null || code[i].isEmpty()) continue;
            if (!code[i].matches("[A-Za-z0-9_]+")) continue;

            valid.add(new String[]{businessLine[i], code[i]});
        }

        Collections.sort(valid, (a, b) -> {
            int lineCompare = order.get(a[0]) - order.get(b[0]);
            if (lineCompare != 0) return lineCompare;
            return a[1].compareTo(b[1]);
        });

        List<String> result = new ArrayList<>();
        for (String[] arr : valid) {
            result.add(arr[1]);
        }

        return result;
    }
}