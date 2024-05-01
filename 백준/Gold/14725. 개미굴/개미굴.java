import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Node root = new Node("root", -1);
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        for(int i=0;i<n;i++){
            int m= sc.nextInt();
            Node now = root;
            for(int j=0;j<m;j++){
                String name = sc.next();
                if(now.childMap.containsKey(name)){
                    now=now.childMap.get(name);
                }else{
                    now=now.newChild(name);
                }
            }
        }

        root.child.sort((o1,o2) -> String.CASE_INSENSITIVE_ORDER.compare(o1.name, o2.name));
        for (Node node : root.child) {
            node.print();
        }
    }


    static class Node{
        String name;
        int depth;
        HashMap<String, Node> childMap = new HashMap<>();
        ArrayList<Node> child = new ArrayList<>();

        public Node(String name, int depth) {
            this.name = name;
            this.depth = depth;
        }

        public Node newChild(String name){
            Node child = new Node(name, this.depth + 1);
            childMap.put(name, child);
            this.child.add(child);
            return child;
        }

        public void print(){
            StringBuilder sb = new StringBuilder();
            for(int i=0;i<depth;i++){
                sb.append("--");
            }
            sb.append(this.name);
            System.out.println(sb);
            child.sort((o1,o2) -> String.CASE_INSENSITIVE_ORDER.compare(o1.name, o2.name));
            for (Node node : child) {
                node.print();
            }
        }
    }
}
