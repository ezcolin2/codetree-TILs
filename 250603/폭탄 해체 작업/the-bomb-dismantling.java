// dp로 해결
// dp[i][j] : i번째 폭탄까지 고려했을 때, j개 폭탄을 해제했을 때 점수 최대 값
import java.util.Scanner;
import java.util.Queue;
import java.util.PriorityQueue;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Bomb[] bombs = new Bomb[n];
        Queue<Integer> pq = new PriorityQueue();
        for (int i = 0; i < n; i++) {
            bombs[i] = new Bomb(sc.nextInt(), sc.nextInt());
        }
        Arrays.sort(bombs);
        int res = 0;
        int bombIdx = n-1;
        // 뒤에서부터 차례대로
        for (int time=10001; time>0; time--){
            // 지금 시간에 해체할 수 있는 모든 폭탄을 pq에 넣는다.
            while (bombIdx >=0 && bombs[bombIdx].time >= time){
                pq.add(-bombs[bombIdx--].score);
            }
            if (pq.isEmpty()){
                continue;
            }
            // 뽑는다.
            int score = pq.remove();
            res += -score;
        }
        System.out.println(res);
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
        if (this.time == bomb.time){
            return Integer.compare(this.score, bomb.score);
        }
        return Integer.compare(this.time, bomb.time);
    }
}