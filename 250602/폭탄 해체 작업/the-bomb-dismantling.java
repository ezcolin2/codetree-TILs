import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Bomb[] bombs = new Bomb[n];
        for (int i = 0; i < n; i++) {
            bombs[i] = new Bomb(sc.nextInt(), sc.nextInt());
        }
        Arrays.sort(bombs);
        int totalScore = 0;
        // 현재 시간
        int currentTime = 0;
        for (int i=0; i<n; i++){
            // 현재 시간보다 같거나 작으면 스킵
            if (bombs[i].time <= currentTime){
                continue;
            }
            totalScore += bombs[i].score;
            currentTime += 1;
            
        }
        System.out.println(totalScore);
    }
}
class Bomb implements Comparable<Bomb>{
    int score;
    int time;
    public Bomb(int score, int time){
        this.score = score;
        this.time = time;
    }
    @Override
    public int compareTo(Bomb bomb){
        // 시간이 같을 때는 점수 기준 내림차순
        if (this.time == bomb.time){
            return Integer.compare(bomb.score, this.score);
        }
        // 시간이 다를 때는 시간 기준 오름차순
        return Integer.compare(this.time, bomb.time);
    }
}