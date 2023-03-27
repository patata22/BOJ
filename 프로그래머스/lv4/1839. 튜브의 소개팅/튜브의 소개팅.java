import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(int n, int m, int s, int[][] time_map) {
        int[] answer = new int[2];
        int[] dx = new int[]{-1, 1, 0, 0};
        int[] dy = new int[]{0, 0, -1, 1};

        long[][][] distance = new long[n][m][n * m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                Arrays.fill(distance[i][j],Long.MAX_VALUE);
            }
        }
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> {
            int t1=o1.getT(), t2=o2.getT();
            if(t1!=t2){
                return Integer.compare(t1,t2);
            }
            return Long.compare(o1.getS(), o2.getS());
        });
        distance[0][0][0] = 0;
        pq.add(new Node(0, 0, 0, 0));
        while (!pq.isEmpty()) {
            int x = pq.peek().getX();
            int y = pq.peek().getY();
            int t = pq.peek().getT();
            long talkTime = pq.poll().getS();
            if (distance[x][y][t] != talkTime) {
                continue;
            }
            if (x == n - 1 && y == m - 1) {
                answer[0] = t;
                answer[1] = (int) talkTime;
                break;
            }
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && time_map[nx][ny] != -1 && t<n*m-1) {
                    long newTalkTime = talkTime + time_map[nx][ny];
                    if (newTalkTime <= s && distance[nx][ny][t + 1] > newTalkTime) {
                        distance[nx][ny][t + 1] = newTalkTime;
                        pq.add(new Node(nx, ny, t+1,newTalkTime));
                    }
                }
            }

        }
        return answer;
    }
}


class Node {
    int x;
    int y;
    int t;
    long s;

    public Node(int x, int y, int t, long s) {
        this.x = x;
        this.y = y;
        this.t = t;
        this.s = s;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getT() {
        return t;
    }

    public long getS() {
        return s;
    }
}
