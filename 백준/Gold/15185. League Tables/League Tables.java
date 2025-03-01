import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static HashMap<String, Team> teams = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n= Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            String name = br.readLine();
            int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            Team team = new Team(name, temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6]);
            teams.put(name,team);
        }

        int m=Integer.parseInt(br.readLine());
        for(int i=0;i<m;i++){
            Team teamA = teams.get(br.readLine());
            int scoreA = Integer.parseInt(br.readLine());
            Team teamB = teams.get(br.readLine());
            int scoreB = Integer.parseInt(br.readLine());

            teamA.Match(scoreA, scoreB);
            teamB.Match(scoreB, scoreA);
        }

        ArrayList<Team> result = new ArrayList<>();
        for (String s : teams.keySet()) {
            result.add(teams.get(s));
        }

        result.sort((o1, o2) -> {
            if(o1.point!=o2.point){
                return -Integer.compare(o1.point, o2.point);
            }
            if(o1.earned-o1.against!=o2.earned-o2.against){
                return -Integer.compare(o1.earned-o1.against,o2.earned-o2.against);
            }
            if(o1.earned!=o2.earned){
                return -Integer.compare(o1.earned,o2.earned);
            }
            return o1.name.compareToIgnoreCase(o2.name);
        });

        for (Team team : result) {
            System.out.println(team);
        }
    }
}


class Team{
    String name;
    int game;
    int win;
    int draw;
    int lose;
    int earned;
    int against;
    int point;

    public Team(String name, int game, int win, int draw, int lose, int earned, int against, int point) {
        this.game = game;
        this.name = name;
        this.win = win;
        this.draw = draw;
        this.lose = lose;
        this.earned = earned;
        this.against = against;
        this.point = point;
    }

    public void Match(int earn, int lost){
        this.game++;
        if(earn>lost){
            Win(earn,lost);
        }else if(earn<lost){
            Lose(earn,lost);
        }else{
            Draw(earn);
        }
    }

    public void Win(int earn, int lost){
        this.point+=3;
        this.win++;
        this.earned+=earn;
        this.against+=lost;
    }

    public void Lose(int earn, int lost){
        this.lose++;
        this.earned+=earn;
        this.against+=lost;
    }

    public void Draw(int earn){
        this.point++;
        this.draw++;
        this.earned+=earn;
        this.against+=earn;
    }

    @Override
    public String toString() {
        return this.name+' '+game+" "+win+" "+draw+" "+lose+" "+earned+" "+against+" "+point;
    }
}