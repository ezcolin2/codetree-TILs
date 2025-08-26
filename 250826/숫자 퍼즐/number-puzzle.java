import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        // dp[i][j][k] : i개의 마법석을 j개의 합이되도록 마지막 값이 k일 때 경우의 수
        int[][][] dp = new int[n+1][m+1][m+1];

        // 마법석이 1개면 무조건 경우의 수 1
        for (int j=1; j<=m; j++){
            dp[1][j][j] = 1;
        }
        
        for(int i=1; i<n; i++){
            for(int j=1; j<=m; j++){
                for(int q=1; q<=m; q++){
                    // 만약 경우의 수가 없으면 스킵
                    if (dp[i][j][q] == 0){
                        continue;
                    }
                    // 마지막 값보다 큰 값
                    for (int p=q; p<=m; p++){
                        // p 값을 추가했을 때
                        int totalSum = j+p;
                        if (totalSum>m){
                            break;
                        }
                        dp[i+1][totalSum][p] += dp[i][j][q];
                    }
                }
            }
        }

        int currentN = n;
        int currentM = m;
        int[] res = new int[n+1];
        int currentK = m;
        while (currentK > 0){
            if (dp[currentN][currentM][currentK] < k){
                k -= dp[currentN][currentM][currentK];
                currentK--;
            }
            // 만약 k보다 크다면? 확정 짓고 이전 단계로
            else{
                res[currentN] = currentK;
                currentN--;
                currentM-=currentK;
            }
        }
        for (int i=1; i<=n; i++){
            System.out.print(res[i]+" ");
        }
    }
}

