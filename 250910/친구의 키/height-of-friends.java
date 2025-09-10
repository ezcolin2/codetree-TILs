import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    private static boolean[] visited;
    private static ArrayList<Integer>[] graph;
    private static ArrayList<Integer> order;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        graph = new ArrayList[n+1];
        visited = new boolean[n+1];
        order = new ArrayList();
        for (int i=0; i<=n; i++){
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a].add(b);
        }

        for (int i=1; i<=n; i++){
            if (visited[i]){
                continue;
            }
            visited[i] = true;
            dfs(i);
        }
        for (int i=order.size()-1; i>=0; i--){
            System.out.print(order.get(i));
            System.out.print(" ");
        }
    }

    private static void dfs(int node){
        // 연결된 모든 노드를 조사한다.
        for (Integer nextNode: graph[node]){
            // 방문한 것 패스
            if (visited[nextNode]){
                continue;
            }
            visited[nextNode]=true;
            dfs(nextNode);
        }
        order.add(node);
    }
}