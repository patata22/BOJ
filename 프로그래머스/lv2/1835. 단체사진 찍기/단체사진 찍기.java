import java.util.HashMap;
import java.util.Map;

class Solution {

    static boolean[] used = new boolean[8];
    static Character[] member = new Character[]{'A','C','F','J','M','N','R','T'};
    static Map<Character, Integer> location = new HashMap();
    static int answer;

    public int solution(int n, String[] data) {
        answer=0;
        choice(0,data);
        return answer;
    }

    public void choice(int count, String[] data){
        if(count==8){
            answer+=judge(data);
            return;
        }
        for(int i=0;i<8;i++){
            if(!used[i]){
                used[i]=true;
                location.put(member[i], count);
                choice(count+1, data);
                location.remove(member[i]);
                used[i]=false;
            }
        }
    }

    public int judge(String[] data){
        for (String d : data) {
            char[] temp = d.toCharArray();
            char memberA = temp[0];
            char memberB = temp[2];
            int locationA = location.get(memberA);
            int locationB = location.get(memberB);
            char condition = temp[3];
            int realDistance = Math.abs(locationA - locationB);
            int conditionDistance = Integer.parseInt(String.valueOf(temp[4]))+1;
            if(condition=='='){
                if(realDistance!=conditionDistance){
                    return 0;
                }
            }else if(condition=='>'){
                if(!(realDistance>conditionDistance)){
                    return 0;
                }
            }else if(condition=='<'){
                if(!(realDistance<conditionDistance)){
                    return 0;
                }
            }
        }
        return 1;
    }
}