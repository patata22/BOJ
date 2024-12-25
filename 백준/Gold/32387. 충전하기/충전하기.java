import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.TreeSet;

public class Main {

    static TreeSet<Integer> left;
    static int[] record;

    private static String push(int x, int order){
        Integer result = left.ceiling(x);
        if(result==null){
            return "-1\n";
        }
        left.remove(result);
        record[result]=order;
        return result +"\n";

    }

    private static String pull(int x){
        if(record[x]!=-1){
            left.add(x);
            int result = record[x];
            record[x]=-1;
            return result+"\n";
        }

        return -1+"\n";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int n = Integer.parseInt(temp[0]);
        int q = Integer.parseInt(temp[1]);
        left= new TreeSet<>();
        for(int i=1;i<=n;i++) {
            left.add(i);
        }
        record=new int[n+1];
        Arrays.fill(record, -1);
        StringBuilder sb = new StringBuilder();
        for(int i=1;i<=q;i++){
            temp = br.readLine().split(" ");
            int cmd = Integer.parseInt(temp[0]);
            int num = Integer.parseInt(temp[1]);
            if(cmd==1){
                sb.append(push(num, i));
            }else{
                sb.append(pull(num));
            }
        }

        System.out.println(sb);
    }
}
