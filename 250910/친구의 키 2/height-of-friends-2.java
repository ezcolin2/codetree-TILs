import java.util.Scanner;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    private static ArrayList<Integer>[] graph;
    private static boolean[] visited;
    private static ArrayList<Integer> order;
    private static int[] degrees;
    private static Queue<Integer> queue;

    public static void main(String[] args) {
        order = new ArrayList();
        queue = new LinkedList();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        graph = new ArrayList[n+1];
        visited = new boolean[n+1];
        degrees = new int[n+1];
        for (int i=0; i<=n; i++){
            graph[i] = new ArrayList();
        }
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a].add(b);
            degrees[b]++;
        }
        for (int i=1; i<=n; i++){
            if (degrees[i] == 0){
                queue.add(i);
            }
        }
        while (!queue.isEmpty()){
            int node = queue.remove();
            order.add(node);
            for (Integer nextNode: graph[node]){
                degrees[nextNode]--;
                if (degrees[nextNode] == 0){
                    queue.add(nextNode);
                }
            }
        }

        System.out.println(order.size() == n ? "Consistent" : "Inconsistent");
    }
}