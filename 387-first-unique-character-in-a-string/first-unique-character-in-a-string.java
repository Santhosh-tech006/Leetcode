import java.util.HashMap;

class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> ch = new HashMap<>();

        // Step 1: Count each character
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (ch.containsKey(c)) {
                ch.put(c, ch.get(c) + 1);
            } else {
                ch.put(c, 1);
            }
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (ch.get(c) == 1) {
                return i;
            }
        }
        return -1;
    }
}