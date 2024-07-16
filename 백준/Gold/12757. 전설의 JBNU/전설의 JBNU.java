import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Optional;
import java.util.TreeMap;

public class Main {

    static int k;
    private static TreeMap<Integer, Integer> db = new TreeMap<>();
    private static void renewValue(int key, int value){
        if(db.containsKey(key)){
            db.put(key, value);
            return;
        }
        Optional<Integer> lowerKey = findLowerKey(key);
        Optional<Integer> higherKey = findHigherKey(key);

        int lowerGap=lowerKey.isPresent()?(key-lowerKey.get()):Integer.MAX_VALUE;
        int higherGap=higherKey.isPresent()?(higherKey.get()-key):Integer.MAX_VALUE;

        if(lowerGap==higherGap) return;
        else if(lowerGap<higherGap){
            db.put(lowerKey.get(), value);
        }else{
            db.put(higherKey.get(), value);
        }
    }

    private static String getValue(int key) {
        if(db.containsKey(key)){
            return db.get(key).toString();
        }

        Optional<Integer> lowerKey = findLowerKey(key);
        Optional<Integer> higherKey = findHigherKey(key);

        int lowerGap=lowerKey.isPresent()?(key-lowerKey.get()):Integer.MAX_VALUE;
        int higherGap=higherKey.isPresent()?(higherKey.get()-key):Integer.MAX_VALUE;

        if(lowerGap==Integer.MAX_VALUE&&higherGap==Integer.MAX_VALUE) {
            return String.valueOf(-1);
        }else if(lowerGap==higherGap){
            return "?";
        }else{
            if(lowerGap<higherGap){
                return String.valueOf(db.get(lowerKey.get()));
            }else{
                return String.valueOf(db.get(higherKey.get()));
            }
        }
    }

    private static Optional<Integer> findLowerKey(int key) {
        Integer result = db.lowerKey(key);
        if(result!=null&&key-result<=k){
            return Optional.of(result);
        }
        return Optional.empty();
    }

    private static Optional<Integer> findHigherKey(int key){
        Integer result = db.higherKey(key);
        if(result!=null&&result-key<=k){
            return Optional.of(result);
        }
        return Optional.empty();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int n= Integer.parseInt(temp[0]);
        int m= Integer.parseInt(temp[1]);
        k=Integer.parseInt(temp[2]);

        for(int i=0;i<n;i++){
            temp=br.readLine().split(" ");
            db.put(Integer.parseInt(temp[0]), Integer.parseInt(temp[1]));
        }

        for(int i=0;i<m;i++){
            temp=br.readLine().split(" ");
            int cmd = Integer.parseInt(temp[0]);
            if(cmd==1){
                db.put(Integer.parseInt(temp[1]), Integer.parseInt(temp[2]));
            }else if(cmd==2){
                renewValue(Integer.parseInt(temp[1]),Integer.parseInt(temp[2]));
            }else{
                System.out.println(getValue(Integer.parseInt(temp[1])));
            }
        }
    }
}
