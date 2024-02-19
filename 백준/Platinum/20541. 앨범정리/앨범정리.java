import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {

    static Album root;
    static Album now;
    public static void moveNamedAlbum(String name){
        if(now.albums.containsKey(name)){
            now = now.albums.get(name);
        }
        System.out.println(now.name);
    }

    public static void movePreAlbum(){
        if(now.root!=null){
            now=now.root;
        }
        System.out.println(now.name);
    }

    public static void moveRoot(){
        now=root;
        System.out.println(now.name);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        root = new Album("album", null);
        now=root;
        int n= Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            String[] temp = br.readLine().split(" ");
            String cmd=temp[0];
            if(cmd.equals("mkalb")){
                now.addAlbum(temp[1]);
            }else if(cmd.equals("rmalb")){
                if(temp[1].equals("-1")){
                    int[] counts = now.removeFirstAlbum();
                    System.out.println(counts[0]+" "+counts[1]);
                }else if(temp[1].equals("0")){
                    int[] counts = now.removeAllAlbum(true);

                    System.out.println(counts[0]+" "+counts[1]);
                }else if(temp[1].equals("1")){
                    int[] counts = now.removeLastAlbum();
                    System.out.println(counts[0]+" "+counts[1]);
                }else{
                    int[] counts = now.removeNamedAlbum(temp[1]);
                    System.out.println(counts[0]+" "+counts[1]);
                }
            }else if(cmd.equals("insert")){
                now.insertPhoto(temp[1]);
            }else if(cmd.equals("delete")){
                if(temp[1].equals("-1")){
                    System.out.println(now.deleteFirstPhoto());
                }else if(temp[1].equals("0")){
                    System.out.println(now.deleteAllPhoto());
                }else if(temp[1].equals("1")){
                    System.out.println(now.deleteLastPhoto());
                }else{
                    System.out.println(now.deleteNamedPhoto(temp[1]));
                }
            }else if(cmd.equals("ca")){
                if(temp[1].equals("/")){
                    moveRoot();
                }else if(temp[1].equals("..")){
                    movePreAlbum();
                }else{
                    moveNamedAlbum(temp[1]);
                }
            }
        }
    }
}

class Album{
    Album root;
    String name;
    TreeMap<String, Album> albums;
    TreeSet<String> photos;
    public Album(String name, Album root) {
        this.root = root;
        this.name = name;
        albums = new TreeMap<>();
        photos = new TreeSet<>();
    }
    public void addAlbum(String name){
        if(albums.containsKey(name)){
            System.out.println("duplicated album name");
        }else{
            albums.put(name,new Album(name,this));
        }
    }

    public int[] removeAllAlbum(boolean isRoot){
        int[] counts = new int[]{0,0};
        for (Album album : albums.values()) {
            int[] node = album.removeAllAlbum(false);
            counts[0]+=node[0];
            counts[1]+=node[1];
        }
        counts[0]+=this.albums.size();
        if(!isRoot)counts[1]+=this.photos.size();
        this.albums.clear();
        if(!isRoot)this.photos.clear();
        return counts;
    }
    public int[] removeFirstAlbum(){
        if(albums.isEmpty()){
            return new int[]{0,0};
        }
        String firstName = albums.firstKey();
        Album firstAlbum = albums.get(firstName);
        int[] counts = firstAlbum.removeAllAlbum(false);
        albums.remove(firstName);
        counts[0]+=1;
        return counts;
    }

    public int[] removeLastAlbum(){
        if(albums.isEmpty()){
            return new int[]{0,0};
        }
        String lastName = albums.lastKey();
        Album lastAlbum = albums.get(lastName);
        int[] counts = lastAlbum.removeAllAlbum(false);
        albums.remove(lastName);
        counts[0]+=1;
        return counts;
    }
    public int[] removeNamedAlbum(String name){
        if(!albums.containsKey(name)){
            return new int[]{0,0};
        }
        Album album = albums.get(name);
        int[] counts = album.removeAllAlbum(false);
        albums.remove(name);
        counts[0]+=1;
        return counts;
    }

    public void insertPhoto(String name){
        if(photos.contains(name)){
            System.out.println("duplicated photo name");
            return;
        }
        photos.add(name);
    }

    public int deleteNamedPhoto(String name){
        if(photos.contains(name)){
            photos.remove(name);
            return 1;
        }
        return 0;
    }

    public int deleteFirstPhoto(){
        if(photos.isEmpty()) return 0;
        photos.remove(photos.first());
        return 1;
    }

    public int deleteLastPhoto(){
        if(photos.isEmpty()) return 0;
        photos.remove(photos.last());
        return 1;
    }

    public int deleteAllPhoto(){
        int count = photos.size();
        photos.clear();
        return count;
    }
}