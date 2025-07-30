import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.TreeSet;

public class Main {
    static int n,m,r;
    static TreeSet<Integer> flags = new TreeSet<>();
    static int[] points;

    private static String sol(){
        int result = 0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int bottom = points[j]-points[i];
                if(bottom>r) break;
                int target = r/bottom;
                Integer check = flags.floor(target);
                if(check!=null){
                    result = Math.max(result, bottom*check);
                }
            }
        }
        if(result==0) return String.valueOf(-1);
        StringBuilder sb = new StringBuilder(String.valueOf(result / 2));
        if(result%2==0) sb.append(".0");
        else sb.append(".5");
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" " );
        n = Integer.parseInt(temp[0]);
        m = Integer.parseInt(temp[1]);
        r = Integer.parseInt(temp[2]);
        r*=2;
        points = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();
        Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).forEach(flags::add);

        System.out.println(sol());

    }
}