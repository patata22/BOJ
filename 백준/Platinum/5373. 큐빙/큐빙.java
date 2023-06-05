import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t=0;t<T;t++){
            Cube cube = new Cube();
            int n= Integer.parseInt(br.readLine());
            String [] command = br.readLine().split(" ");
            for (String cmd : command) {
                char[] temp = cmd.toCharArray();
                boolean clock = temp[1]=='+';
                if(temp[0]=='U'){
                    cube.rotateU(clock);
                }else if(temp[0]=='B'){
                    cube.rotateB(!clock);
                }else if(temp[0]=='R'){
                    cube.rotateR(clock);
                }else if(temp[0]=='L'){
                    cube.rotateL(clock);
                }else if(temp[0]=='D'){
                    cube.rotateD(!clock);
                }else if(temp[0]=='F'){
                    cube.rotateF(clock);
                }
            }
            cube.printAnswer();
        }
    }
}

class Cube {
    Part[] parts = new Part[27];
    int[] U = new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8};
    int[] L = new int[]{0, 3, 6, 9, 12, 15, 18, 21, 24};
    int[] R = new int[]{2, 5, 8, 11, 14, 17, 20, 23, 26};
    int[] D = new int[]{18, 19, 20, 21, 22, 23, 24, 25, 26};
    int[] F = new int[]{6, 7, 8, 15, 16, 17, 24, 25, 26};
    int[] B = new int[]{0, 1, 2, 9, 10, 11, 18, 19, 20};


    public void rotateU(boolean clock) {
        if (!clock) {
            for (int i = 0; i < 3; i++) {
                rotateU(true);
            }
            return;
        }
        Part temp = parts[1];
        parts[1] = parts[3];
        parts[3] = parts[7];
        parts[7] = parts[5];
        parts[5] = temp;
        temp = parts[0];
        parts[0] = parts[6];
        parts[6] = parts[8];
        parts[8] = parts[2];
        parts[2] = temp;
        for (int i : U) {
            parts[i].rotateU();
        }
    }


    public void rotateR(boolean clock) {
        if (!clock) {
            for (int i = 0; i < 3; i++) {
                rotateR(true);
            }
            return;
        }
        Part temp = parts[2];
        parts[2] = parts[8];
        parts[8] = parts[26];
        parts[26] = parts[20];
        parts[20] = temp;
        temp = parts[5];
        parts[5] = parts[17];
        parts[17] = parts[23];
        parts[23] = parts[11];
        parts[11] = temp;
        for (int i : R) {
            parts[i].rotateR();
        }
    }

    public void rotateL(boolean clock) {
        if (!clock) {
            for (int i = 0; i < 3; i++) {
                rotateL(true);
            }
            return;
        }
        Part temp = parts[0];
        parts[0] = parts[18];
        parts[18] = parts[24];
        parts[24] = parts[6];
        parts[6] = temp;
        temp = parts[3];
        parts[3] = parts[9];
        parts[9] = parts[21];
        parts[21] = parts[15];
        parts[15] = temp;
        for (int i : L) {
            parts[i].rotateL();
        }
    }

    public void rotateD(boolean clock) {
        if (!clock) {
            for (int i = 0; i < 3; i++) {
                rotateD(true);
            }
            return;
        }
        Part temp = parts[18];
        parts[18] = parts[24];
        parts[24] = parts[26];
        parts[26] = parts[20];
        parts[20] = temp;
        temp = parts[19];
        parts[19] = parts[21];
        parts[21] = parts[25];
        parts[25] = parts[23];
        parts[23] = temp;
        for (int i : D) {
            parts[i].rotateD();
        }
    }

    public void rotateF(boolean clock) {
        if (!clock) {
            for (int i = 0; i < 3; i++) {
                rotateF(true);
            }
            return;
        }
        Part temp = parts[6];
        parts[6] = parts[24];
        parts[24] = parts[26];
        parts[26] = parts[8];
        parts[8] = temp;
        temp = parts[7];
        parts[7] = parts[15];
        parts[15] = parts[25];
        parts[25] = parts[17];
        parts[17] = temp;
        for (int i : F) {
            parts[i].rotateF();
        }
    }

    public void rotateB(boolean clock) {
        if (!clock) {
            for (int i = 0; i < 3; i++) {
                rotateB(true);
            }
            return;
        }
        Part temp = parts[0];
        parts[0] = parts[18];
        parts[18] = parts[20];
        parts[20] = parts[2];
        parts[2] = temp;
        temp = parts[1];
        parts[1] = parts[9];
        parts[9] = parts[19];
        parts[19] = parts[11];
        parts[11] = temp;
        for (int i : B) {
            parts[i].rotateB();
        }
    }

    public Cube() {
        for (int i = 0; i < 27; i++) {
            parts[i] = new Part();
        }
        for (int i : U) {
            parts[i].u = 'w';
        }
        for (int i : D) {
            parts[i].d = 'y';
        }
        for (int i : L) {
            parts[i].l = 'g';
        }
        for (int i : B) {
            parts[i].b = 'o';
        }
        for (int i : R) {
            parts[i].r = 'b';
        }
        for (int i : F) {
            parts[i].f = 'r';
        }
    }

    public void printAnswer() {
        for(int i=0;i<9;i++){
            System.out.print(parts[i].u);
            if(i%3==2) System.out.println();
        }

    }
}

class Part {
    public char u, d, f, b, l, r;

    public void rotateU() {
        char temp = b;
        b = l;
        l = f;
        f = r;
        r = temp;
    }
    public void rotateR() {
        char temp = u;
        u = f;
        f = d;
        d = b;
        b = temp;
    }
    public void rotateF() {
        char temp = u;
        u = l;
        l = d;
        d = r;
        r = temp;
    }
    public void rotateD() {
        char temp = b;
        b = l;
        l = f;
        f = r;
        r = temp;
    }
    public void rotateL() {
        char temp = u;
        u = b;
        b = d;
        d = f;
        f = temp;
    }
    public void rotateB() {
        char temp = u;
        u = l;
        l = d;
        d = r;
        r = temp;
    }
}