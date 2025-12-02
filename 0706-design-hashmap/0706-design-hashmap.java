class MyHashMap {

    private ListNode[] buckets;
    private static final int SIZE = 10000;

    private static class ListNode {
        int key, value;
        ListNode next;

        ListNode(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public MyHashMap() {
        buckets = new ListNode[SIZE];
    }

    private int hash(int key) {
        return key % SIZE;
    }

    public void put(int key, int value) {
        int index = hash(key);

        if (buckets[index] == null) {
            buckets[index] = new ListNode(-1, -1);  
        }

        ListNode prev = findNode(buckets[index], key);
        
        if (prev.next == null) {
            prev.next = new ListNode(key, value);  
        } else {
            prev.next.value = value;              
        }
    }

    public int get(int key) {
        int index = hash(key);

        if (buckets[index] == null) return -1;

        ListNode prev = findNode(buckets[index], key);

        if (prev.next == null) return -1;

        return prev.next.value;
    }

    public void remove(int key) {
        int index = hash(key);

        if (buckets[index] == null) return;

        ListNode prev = findNode(buckets[index], key);

        if (prev.next == null) return;

        prev.next = prev.next.next;
    }

    private ListNode findNode(ListNode head, int key) {
        ListNode prev = head;
        ListNode curr = head.next;

        while (curr != null && curr.key != key) {
            prev = curr;
            curr = curr.next;
        }
        return prev;
    }
}
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */