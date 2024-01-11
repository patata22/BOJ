import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {

    static int p,m;

    static ArrayList<Room> rooms = new ArrayList<>();

    static void findRoom(User user){
        for (Room room : rooms) {
            if(room.addUser(user)) return;
        }
        rooms.add(new Room(user, m));
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        p = Integer.parseInt(temp[0]);
        m = Integer.parseInt(temp[1]);
        for(int i=0;i<p;i++){
            temp=br.readLine().split(" ");
            int level = Integer.parseInt(temp[0]);
            String name = temp[1];
            findRoom(new User(level, name));
        }
        for (Room room : rooms) {
            System.out.print(room);
        }

    }

}

class Room{
    private int lowerBound;
    private int upperBound;
    private int maxSize;
    private List<User> users;

    public Room(User user, int maxSize) {
        this.lowerBound = user.getLevel()-10;
        this.upperBound = user.getLevel()+10;
        this.maxSize = maxSize;
        this.users = new ArrayList<>();
        users.add(user);
    }

    public boolean addUser(User user){
        if(users.size()==maxSize) return false;
        if(user.getLevel()<=this.upperBound&&this.lowerBound<=user.getLevel()){
            users.add(user);
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        Collections.sort(users, Comparator.comparing(User::getName));
        StringBuilder sb = new StringBuilder();
        if(users.size()==maxSize) sb.append("Started!\n");
        else sb.append("Waiting!\n");
        for (User user : users) {
            sb.append(user.toString());
        }
        return sb.toString();
    }
}

class User{
    private String name;
    private int level;

    public User(int level, String name) {
        this.name = name;
        this.level = level;
    }

    public String getName() {
        return name;
    }

    public int getLevel() {
        return level;
    }

    @Override
    public String toString() {
        return this.level+" "+this.name+"\n";
    }
}
