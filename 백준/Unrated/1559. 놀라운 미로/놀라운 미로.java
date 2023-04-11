import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static int n, m, k, success;
    static int[][] board, treasure;
    static int[] dx = new int[]{-1, 0, 1, 0};
    static int[] dy = new int[]{0, 1, 0, -1};
    static Map<Character, Integer> D = new HashMap<>();

    public static int sol() {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        boolean[][][][] visited = new boolean[n][m][4][success + 1];
        q.add(new int[]{0, 0, 0});
        visited[0][0][0][0] = true;
        int t = 0;
        while (!q.isEmpty()) {
            int l = q.size();
            for (int i = 0; i < l; i++) {
                int x = q.peek()[0], y = q.peek()[1], key = q.poll()[2];
                if (x == n - 1 && y == m - 1 && key == success) return t;
                int d = (t + board[x][y]) % 4;
                int T = (t + 1) % 4;
                int nx = x + dx[d], ny = y + dy[d];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (treasure[nx][ny] != 0) {
                        int keyTemp = key | (1 << (treasure[nx][ny] - 1));
                        if (!visited[nx][ny][T][keyTemp]) {
                            visited[nx][ny][T][keyTemp] = true;
                            q.add(new int[]{nx, ny, keyTemp});
                        }
                    } else {
                        if (!visited[nx][ny][T][key]) {
                            visited[nx][ny][T][key] = true;
                            q.add(new int[]{nx, ny, key});
                        }
                    }
                }
                if (!visited[x][y][T][key]) {
                    visited[x][y][T][key] = true;
                    q.add(new int[]{x, y, key});
                }
            }
            t += 1;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        D.put('N', 0);
        D.put('E', 1);
        D.put('S', 2);
        D.put('W', 3);

        while (true) {
            String[] temp = br.readLine().split(" ");
            n = Integer.parseInt(temp[0]);
            m = Integer.parseInt(temp[1]);
            if (n == 0) {
                break;
            }
            board = new int[n][m];
            for (int i = 0; i < n; i++) {
                char[] chars = br.readLine().toCharArray();
                for (int j = 0; j < m; j++) {
                    board[i][j] = D.get(chars[j]);
                }
            }
            treasure = new int[n][m];
            k = Integer.parseInt(br.readLine());
            success = (int) (Math.pow(2, k) - 1);
            for (int i = 1; i <= k; i++) {
                temp = br.readLine().split(" ");
                int a = Integer.parseInt(temp[0]) - 1;
                int b = Integer.parseInt(temp[1]) - 1;
                treasure[a][b] = i;
            }
            System.out.println(sol());
        }
    }
}