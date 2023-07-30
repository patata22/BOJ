
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Trie root = new Trie();
        for (int i = 0; i < n; i++) {
            root.insert(br.readLine().toCharArray());
        }
        ArrayDeque<Trie> q = new ArrayDeque<>();
        root.fail = root;
        q.add(root);
        while (!q.isEmpty()) {
            Trie now = q.poll();
            for (int i = 0; i < 26; i++) {
                Trie next = now.go[i];
                if (next == null) continue;
                if (now == root) next.fail = root;
                else {
                    Trie dest = now.fail;
                    while (dest != root && dest.go[i] == null) {
                        dest = dest.fail;
                    }
                    if (dest.go[i] != null) dest = dest.go[i];
                    next.fail = dest;
                }
                if (next.fail.output) next.output = true;
                q.add(next);
            }
        }
        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            char[] chars = br.readLine().toCharArray();
            Trie now = root;
            boolean result = false;
            for (int c = 0; c < chars.length; c++) {
                int next = chars[c] - 'a';
                while (now != root && now.go[next] == null) {
                    now = now.fail;
                }
                if (now.go[next] != null) {
                    now = now.go[next];
                }
                if (now.output) {
                    result = true;
                    break;
                }
            }
            if (result) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}

class Trie {
    Trie[] go;
    Trie fail;
    boolean output;

    public Trie() {
        go = new Trie[26];
        output = false;
    }

    public void insert(char[] key) {
        Trie now = this;
        for (int i = 0; i < key.length; i++) {
            int next = key[i] - 'a';
            if (now.go[next] == null) {
                now.go[next] = new Trie();
            }
            now = now.go[next];
            if (i == key.length - 1) {
                now.output = true;
            }
        }
    }
}