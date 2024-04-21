import java.util.ArrayDeque;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};

    static int n,m,fuel,tx,ty;
    static int[][] board;
    static Customer[][] customers;

    static PriorityQueue<Customer> pq = new PriorityQueue<>((o1, o2) -> {
        if (o1.distance != o2.distance) {
            return Integer.compare(o1.distance, o2.distance);
        }
        if (o1.sx != o2.sx) {
            return Integer.compare(o1.sx, o2.sx);
        }
        return Integer.compare(o1.sy, o2.sy);
    });

    private static Customer findCustomer(){
        pq.clear();
        ArrayDeque<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][n];
        q.add(new int[]{tx,ty});
        visited[tx][ty]=true;
        if(customers[tx][ty]!=null){
            customers[tx][ty].distance=0;
            return customers[tx][ty];
        }
        int dist = 0;
        while(!q.isEmpty()){
            int L= q.size();
            for(int l=0;l<L;l++){
                int x = q.peek()[0];
                int y = q.poll()[1];
                if(customers[x][y]!=null){
                    customers[x][y].distance=dist;
                    pq.add(customers[x][y]);
                }
                for(int i=0;i<4;i++){
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(0<=nx&&nx<n&&0<=ny&&ny<n&&board[nx][ny]!=1&&!visited[nx][ny]){
                        visited[nx][ny]=true;
                        q.add(new int[]{nx,ny});

                    }
                }
            }
            dist+=1;
        }
        return pq.poll();

    }

    public static int getDistance(Customer c){
        ArrayDeque<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][n];
        q.add(new int[]{c.sx,c.sy});
        visited[c.sx][c.sy]=true;
        int ex = c.ex;
        int ey = c.ey;
        int dist = 0;
        while(!q.isEmpty()){
            int L= q.size();
            for(int l=0;l<L;l++){
                int x = q.peek()[0];
                int y = q.poll()[1];
                if(x==ex&&y==ey) return dist;
                for(int i=0;i<4;i++){
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(0<=nx&&nx<n&&0<=ny&&ny<n&&board[nx][ny]!=1&&!visited[nx][ny]){
                        visited[nx][ny]=true;
                        q.add(new int[]{nx,ny});
                    }
                }
            }
            dist+=1;
        }
        return -1;
    }

    public static int sol(){
        for(int i=0;i<m;i++){
            Customer customer = findCustomer();

            if(customer==null) return -1;
            int destination = getDistance(customer);
            if(destination==-1) return -1;
            if(customer.distance+destination>fuel)  return -1;
            fuel-=customer.distance;
            fuel+=destination;
            tx = customer.ex;
            ty = customer.ey;
            customers[customer.sx][customer.sy]=null;
        }
        return fuel;
    }

    private static void init(){
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        board= new int[n][n];
        customers= new Customer[n][n];
        fuel=sc.nextInt();
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                board[i][j]=sc.nextInt();
            }
        }
        tx=sc.nextInt()-1;
        ty=sc.nextInt()-1;
        for(int i=0;i<m;i++){
            Customer customer = new Customer(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt());
            customers[customer.sx][customer.sy]=customer;
        }

    }
    public static void main(String[] args) {
        init();
        System.out.println(sol());
    }

    static class Customer{
        int sx,sy,ex,ey,distance;

        public Customer(int sx, int sy, int ex, int ey) {
            this.sx = sx-1;
            this.sy = sy-1;
            this.ex = ex-1;
            this.ey = ey-1;
            this.distance=0;
        }

        @Override
        public String toString() {
            return "Customer{" +
                    "sx=" + sx +
                    ", sy=" + sy +
                    ", distance=" + distance +
                    ", tx = " + tx +
                    ", ty = " + ty +
                    ", fuel=" + fuel +
                    '}';
        }
    }

}
