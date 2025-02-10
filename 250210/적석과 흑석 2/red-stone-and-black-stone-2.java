import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        // 빨간 돌 배열
        int[] redStones = new int[c];
        for (int i=0; i<c; i++){
            st = new StringTokenizer(br.readLine());
            redStones[i] = Integer.parseInt(st.nextToken());
        }
        // 오름차순 정렬
        Arrays.sort(redStones);

        // 검은 돌 배열
        int[][] blackStones = new int[n][2];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            blackStones[i][0] = a;
            blackStones[i][1] = b;
        }
        // 오름차순 정렬
        Arrays.sort(blackStones, new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b){
                if (a[0] == b[0]){
                    return Integer.compare(a[1], b[1]);
                }
                return Integer.compare(a[0], b[0]);
            }
        });

        // 최대 쌍 개수 구하기
        int maxPairs = getMaxPairs(redStones, blackStones);
        bw.write(String.valueOf(maxPairs));
        bw.close();
    }

    /**
        @param redStones : 정렬된 빨간 돌
        @param blackStones : 정렬된 검은 돌
        @return : 최대 쌍 개수
    */
    public static int getMaxPairs(int[] redStones, int[][] blackStones){
        /**
            그리디로 접근한다.
            가장 작은 빨간 돌은 가장 시작점이 작은 검은 돌과 매칭한다.
            이렇게 검은 돌이 매칭될 경우 혹시 이후에 이 검은 돌과 매칭할 수 있던 빨간 돌은 이 검은 돌과 매칭하지 못 한다.
            하지만 다음 검은 돌과 매칭될 가능성이 존재하게 되고 이는 이 선택의 최적의 해라는 것을 의미한다.
        */

        int c = redStones.length;
        int n = blackStones.length;
        int maxPairs = 0;
        
        // 매칭 시작
        int redIdx = 0;
        int blackIdx = 0;
        while (redIdx < c && blackIdx < n){
            // 만약 빨간 돌이 검은 돌의 시작 번호보다 작다면
            if (redStones[redIdx] < blackStones[blackIdx][0]){
                // 다음 빨간 돌로 간다.
                redIdx++;
                continue;
            }

            // 만약 빨간 돌이 검은 돌의 끝 번호보다 크다면
            if (redStones[redIdx] > blackStones[blackIdx][1]){
                // 다음 검은 돌로 간다.
                blackIdx++;
                continue;
            }

            // 빨간 돌이 검은 돌의 범위 안에 속한다면
            // 매칭 
            maxPairs++;
            redIdx++;
            blackIdx++;
        }
        return maxPairs;
    }
}