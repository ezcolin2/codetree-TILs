import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] BCards = new int[n];
        for (int i = 0; i < n; i++) {
            BCards[i] = sc.nextInt();
            set.add(BCards[i]);
        }

        // A가 가지고 있는 모든 카드 번호를 구한다.
        int[] ACards = new int[n];
        int idx = 0;
        for (int i=1; i<=2*n; i++){
            if (set.contains(i)){
                continue;
            }
            ACards[idx++] = i;
        }


        // 정렬 
        Arrays.sort(ACards);
        Arrays.sort(BCards);
        int score = 0;
        int AIdx = 0;

        // 매칭 시작
        for (int BIdx = 0; BIdx < n; BIdx++){
            // BCards[BIdx]보다 큰 게 나올 때까지
            while (AIdx < n && ACards[AIdx] <= BCards[BIdx]){
                AIdx++;
            }

            // 만약 범위 넘었다면 스킵
            if (AIdx >= n){
                continue;
            }

            //  큰 게 나왔다면?
            score+=1;
        }
        System.out.println(score);



    }

}
