import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int n= Integer.parseInt(temp[0]), m= Integer.parseInt(temp[1]);
        int DIV = 1000000009;
        int[][] dp = new int[n+1][m+1];
        for(int i=0;i<n;i++) Arrays.fill(dp[i], 1);
        for(int i=0;i<n;i++){
            char[] c = br.readLine().toCharArray();
            for(int j=0;j<m;j++){
                int x= dp[i][j]%=DIV;
                if(c[j]=='B'){
                    dp[i][j+1]+=x;
                    dp[i+1][j]+=x;
                }else if(c[j]=='S'){
                    dp[i+1][j]+=x;
                }else{
                    dp[i][j+1]+=x;
                }
            }
        }
        System.out.println(dp[n-1][m-1]);
    }
}