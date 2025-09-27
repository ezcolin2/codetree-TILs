import java.util.*;

public class Main {
    private static int[] arr;
    private static int[] dp;
    private static ArrayList<Integer>[] graph;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        arr = new int[n+1];
        dp = new int[n+1];
        graph = new ArrayList[n+1];
        for (int i=0; i<=n; i++){
            graph[i] = new ArrayList();
        }
        for (int i = 2; i < n + 1; i++) {
            int t = sc.nextInt();
            int a = sc.nextInt();
            int p = sc.nextInt();

            arr[i] = (t==1) ? a : -a;
            graph[p].add(i);
        }
        System.out.println(dfs(1));
    }

    private static int dfs(int nodeNumber){
        // 값을 이미 구했다면 반환
        if (dp[nodeNumber] != 0){
            return dp[nodeNumber];
        }
        int res = arr[nodeNumber];
        // 자식이 없으면 자기 자신 반환
        if (graph[nodeNumber].size() == 0){
            dp[nodeNumber] = res;
            return dp[nodeNumber];
        }

        // 아니면 자식마다 dfs 수행
        for (int nextNodeNumber: graph[nodeNumber]){
            int dfsRes = dfs(nextNodeNumber);
            res += dfsRes > 0 ? dfsRes : 0;
        }
        dp[nodeNumber] = res;
        return dp[nodeNumber];
    }
}