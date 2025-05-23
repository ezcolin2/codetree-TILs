/**
    DP로 해결한다.
    dp[i][j] : i번째까지 고려했을 때, 그 합이 j가 될 수 있는 경우의 수
    배열의 인덱스로 표현하기 위해 문제의 조건을 0이상 40이하로 바꾼다.
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }
        long[][] dp = new long[N][41];
        // 초기 값 세팅
        dp[0][20 + numbers[0]] += 1;
        dp[0][20 - numbers[0]] += 1;
        
        // 순회 시작
        for (int i=1; i<N; i++){
            // 한 칸 나아갈 때마다 이전의 40개 값들을 모두 확인한다.
            for (int j=0; j<41; j++){
                // 만약 이전 값이 1이었다면 이 값에서 현재 숫자를 더하고 뺀다.
                if (dp[i-1][j] > 0){
                    // 물론 인덱스 범위를 넘어서는 안 된다.
                    if (j-numbers[i] >=0){
                        dp[i][j-numbers[i]] += dp[i-1][j];
                    }
                    if (j+numbers[i] <= 40){
                        dp[i][j+numbers[i]] += dp[i-1][j];
                    }
                }
            }
        }

        // 1인 개수 세기
        System.out.println(dp[N-1][20+M]);
    }
}