import java.util.Scanner;
import java.util.Queue;
import java.util.PriorityQueue;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        int n = sc.nextInt();
        int[] redStones = new int[c];
        for (int i = 0; i < c; i++) {
            redStones[i] = sc.nextInt();
        }
        int[][] blackStones = new int[n][2];
        for (int i = 0; i < n; i++) {
            blackStones[i][0] = sc.nextInt();
            blackStones[i][1] = sc.nextInt();
        }

        // 검정 돌 정렬 기준 1 - A 오름차순 : 배열 정렬에 사용
        Comparator<int[]> sortComp = new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b){
                if (a[0] == b[0]){
                    return Integer.compare(a[1], b[1]);
                }
                return Integer.compare(a[0], b[0]);
            }
        };

        // 검정 돌 정렬 기준 2 - B 오름차순 : priority queue에 사용
        Comparator<int[]> pqComp = new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b){
                if (a[1] == b[1]){
                    return Integer.compare(a[0], b[0]);
                }
                return Integer.compare(a[1], b[1]);
            }
        };

        // 빨간 돌과 검정 돌 정렬
        Arrays.sort(redStones);
        Arrays.sort(blackStones, sortComp);

        int res = 0;

        // priority queue
        // 빨간 돌을 순회하면서 매칭 가능한 모든 검은 돌들을 넣는다.
        Queue<int[]> pq = new PriorityQueue(pqComp);

        // 빨간 돌을 오름차순으로 탐색하면서 매칭 할 검정 돌 고르기
        int blackIdx = 0;
        for (int redStone : redStones){
            // 가능한 모든 검은 돌을 넣는다.
            while(blackIdx < n && blackStones[blackIdx][0] <= redStone && redStone <= blackStones[blackIdx][1]){
                // pq에 넣는다.
                pq.add(blackStones[blackIdx]);
                blackIdx += 1;
            }

            // 만약 가능한 검은 돌이 없으면 스킵
            if (pq.isEmpty()){
                continue;
            }

            // 다 넣었으면 여기서 가장 끝 구간이 작은 검은 돌을 뽑는다.
            int[] blackStone = pq.remove();

            // 그런데 여기서 이전 빨간 돌에 해당하는 검은 돌들이 현재 빨간 돌에 맞지 않을 수 있으니 범위 체크
            while (!pq.isEmpty() && blackStone[0] > redStone || blackStone[1] < redStone){
                blackStone = pq.remove();
            }

            // 만약 다 뽑았는데도 맞지 않다면 스킵
            if (blackStone[0] > redStone || blackStone[1] < redStone){
                continue;
            }

            // 매칭 완료
            res += 1;
        }

        System.out.println(res);
    }
}