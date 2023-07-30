import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;

public class Main {

    static int id=1;
    static int hs,ws,hb,wb;
    static int[] smallId;
    static char[][] small;
    static char[][] big;
    static int[][] result;
    static HashMap<String, Integer> stringToId = new HashMap<>();

    static BufferedReader br;


    static void makeId(String string){
        if(!stringToId.containsKey(string)){
            stringToId.put(string, id++);
        }
    }

    static int[] getFailure(){
        int[] fail = new int[hs];
        int j=0;
        for(int i=1;i<hs;i++){
            while(j>0&&smallId[i]!=smallId[j]) j= fail[j-1];
            if(smallId[i]==smallId[j]){
                fail[i] = ++j;
            }
        }
        return fail;
    }

    static int KMP(){
        int answer=0;
        int[] fail = getFailure();
        for(int w=0;w<wb;w++){
            int j=0;
            for(int i=0;i<hb;i++){
                while(j>0&&result[i][w]!=smallId[j]) j= fail[j-1];
                if(result[i][w]==smallId[j]){
                    if(j==hs-1){
                        answer++;
                        j=fail[j];
                    }else{
                        j++;
                    }
                }
            }
        }
        return answer;
    }

    static void Aho_Corasick() throws IOException {

        Trie root = new Trie();
        for (String s : stringToId.keySet()) {
            root.insert(s.toCharArray(), stringToId.get(s));
        }
        ArrayDeque<Trie> q = new ArrayDeque<>();
        root.fail = root;
        q.add(root);

        while(!q.isEmpty()){
            Trie now = q.poll();
            for(int i=0;i<2;i++){
                Trie next = now.go[i];
                if(next==null) continue;
                if(now==root) next.fail = root;
                else{
                    Trie dest = now.fail;
                    while(dest!=root&&dest.go[i]==null){
                        dest = dest.fail;
                    }
                    if(dest.go[i]!=null) dest = dest.go[i];
                    next.fail = dest;
                }
                if(next.fail.output!=0) next.output = next.fail.output;
                q.add(next);
            }
        }

        for(int i=0;i<hb;i++){
            Trie now = root;
            char[] big = br.readLine().toCharArray();
            for(int j=0;j<wb;j++){
                int next = big[j]=='x'?1:0;
                while(now!=root&&now.go[next]==null) now=now.fail;
                if(now.go[next]!=null) now = now.go[next];
                if(now.output!=0) result[i][j] = now.output;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        hs = Integer.parseInt(temp[0]);
        ws = Integer.parseInt(temp[1]);
        hb = Integer.parseInt(temp[2]);
        wb = Integer.parseInt(temp[3]);
        smallId = new int[hs];
        small = new char[hs][ws];
        big = new char[hb][wb];
        result = new int[hb][wb];
        for(int i=0;i<hs;i++){
            String s = br.readLine();
            makeId(s);
            smallId[i] = stringToId.get(s);
            small[i] = s.toCharArray();
        }
        Aho_Corasick();
        System.out.println(KMP());
    }
}

class Trie{
    Trie[] go;
    Trie fail;
    int output;

    public Trie() {
        go = new Trie[2];
        output = 0;
    }

    public void insert(char[] key, int id){
        Trie now = this;
        for(int i=0;i<key.length;i++){
            int next = key[i]=='x'?1:0;
            if(now.go[next]==null){
                now.go[next]= new Trie();
            }
            now = now.go[next];
            if(i==key.length-1){
                now.output = id;
            }
        }
    }
}