import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        int n= Integer.parseInt(temp[0]), t=Integer.parseInt(temp[1]);

        int[] turn = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Set<Integer> occupied = new HashSet<>();

        User[] users = new User[n];
        for(int i=0;i<n;i++) users[i] = new User();

        Deque<Card> Deck = new ArrayDeque<>();
        for(int i=0;i<t;i++){
            temp = br.readLine().split(" ");
            if(temp.length==3){
                Deck.add(new Card(Integer.parseInt(temp[0]), temp[1], Integer.parseInt(temp[2])));
            }else{
                Deck.add(new Card(Integer.parseInt(temp[0]), temp[1]));
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i : turn) {
            User user = users[i-1];
            if(user.card==null) {
                Card cardNow= Deck.poll();
                user.card = cardNow;
            }
            sb.append(user.card.id+"\n");
            if(user.card.command.equals("next")){
                user.card=null;
            }else if(user.card.command.equals("acquire")){
                if(!occupied.contains(user.card.target)){
                    occupied.add(user.card.target);
                    user.card=null;
                }
            }else{
                occupied.remove(user.card.target);
                user.card=null;
            }
        }
        System.out.println(sb.toString());
    }
}

class Card{
    int id;
    String command;
    int target;

    public Card(int id, String command, int target) {
        this.id = id;
        this.command = command;
        this.target = target;
    }

    public Card(int id, String command) {
        this.id = id;
        this.command = command;
    }
}

class User{
    Card card;

}