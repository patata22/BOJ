
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int n, m;
    static int[] snack1 = new int[3001];
    static int[] snack2 = new int[101];

    static int[][][][] dp = new int[3][101][101][2];

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            snack1[i] = sc.nextInt();
        }
        m = sc.nextInt();
        for (int i = 1; i <= m; i++) {
            snack2[i] = -sc.nextInt();
        }
        Arrays.sort(snack2, 1, m + 1);
        for (int i = 1; i <= m; i++) snack2[i] *= -1;
        for (int i = 0; i <= 2; i++) {
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= m; k++) {
                    Arrays.fill(dp[i][j][k], Integer.MIN_VALUE);
                }
            }
        }
        dp[0][0][0][0] = 0;
        for (int j = 0; j <= m; j++) {
            for (int k = 0; k <= m - j; k++) {
                if (k > 0) {
                    dp[0][j][k][0] = Math.max(dp[0][j][k][0], dp[0][j][k - 1][1]);
                }
                if (j > 0) {
                    dp[0][j][k][1] = Math.max(dp[0][j][k][1], dp[0][j - 1][k][0]);
                }
                dp[0][j][k][1] = Math.max(dp[0][j][k][1], dp[0][j][k][0]);
            }
        }

        for (int j = 0; j <= m; j++) {
            for (int k = 0; k <= m - j; k++) {
                if (k > 0) {
                    dp[1][j][k][0] = Math.max(dp[1][j][k][0], dp[1][j][k - 1][1]);
                }
                if (j > 0) {
                    dp[1][j][k][1] = Math.max(dp[1][j][k][1], dp[1][j - 1][k][0]);
                }
                dp[1][j][k][0] = Math.max(dp[1][j][k][0], dp[0][j][k][1]);
                dp[1][j][k][1] = Math.max(dp[1][j][k][1], dp[0][j][k][0] + snack1[1]);

                dp[1][j][k][1] = Math.max(dp[1][j][k][1], dp[1][j][k][0]);
            }
        }
        int idx = 0;
        for (int i = 2; i <= n; i++) {
            idx = i % 2 == 0 ? 2 : 1;
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= m - j; k++) {
                    if (k > 0) {
                        dp[idx][j][k][0] = Math.max(dp[idx][j][k][0], dp[idx][j][k - 1][1]);
                    }
                    if (j > 0) {
                        dp[idx][j][k][1] = Math.max(dp[idx][j][k][1], dp[idx][j - 1][k][0]);
                    }

                    dp[idx][j][k][0] = Math.max(dp[idx][j][k][0], dp[3 - idx][j][k][1]);
                    dp[idx][j][k][1] = Math.max(dp[idx][j][k][1], dp[3 - idx][j][k][0] + snack1[i]);

                    dp[idx][j][k][1] = Math.max(dp[idx][j][k][1], dp[idx][j][k][0]);
                }
            }
        }

        int total = 0;
        int answer = 0;
        for (int j = 0; j <= m; j++) {
            total += snack2[j];
            answer = Math.max(answer, dp[idx][j][m - j][1] + total);
        }
        System.out.println(answer);
    }
}
