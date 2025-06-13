// 최단 거리에 속하는 간선들 하나씩 모두 제거해가면서 경우의 수를 구한다.
import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.PriorityQueue;

import java.util.ArrayList;
import java.lang.Comparable;

public class Main {
    public static ArrayList<Edge>[] graph;
    public static int n;
    public static int m;
    public static int[] parentNodeArr; // 부모 노드
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parentNodeArr = new int[n+1];

        // graph[i] : i번 정점에 연결된 엣지 정보들
        graph = new ArrayList[n+1];
        for (int i=1; i<=n; i++){
            graph[i] = new ArrayList();
        }

        // graph 채우기
        for (int i=1; i<=m; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int length = Integer.parseInt(st.nextToken());
            
            // 양방향이기 때문에 두 개 추가
            graph[start].add(new Edge(end, length));
            graph[end].add(new Edge(start, length));
        }

        // 우선 최단 거리와 최단 경로 구하기
        int shortestDistance = djikstra(1, n, -1, -1);
        ArrayList<Integer> shortestPath = getShortestPath(parentNodeArr, 1, n);

        // 이제 shortestPath 바탕으로 간선을 하나씩 제거해나가면서 최단 거리를 다시 구한다.
        int cnt = 0;
        for(int i=1; i<shortestPath.size(); i++){
            int start = shortestPath.get(i-1);
            int end = shortestPath.get(i);
            int distance = djikstra(1, n, start, end);
            if (distance != shortestDistance){
                cnt += 1;
            }
        }
        System.out.println(cnt);
        
    }
    public static int djikstra(int start, int end, int removeStart, int removeEnd){
        int MAX_VALUE = Integer.MAX_VALUE;
        // 최단 거리 배열
        int[] distances = new int[n+1];
        for (int i=0; i<=n; i++){
            distances[i] = MAX_VALUE;
        }

        // 시작 점은 0으로 초기화
        distances[start] = 0;

        // pq 생성
        Queue<VertexInfo> pq = new PriorityQueue();

        // pq에 시작 점 넣기
        pq.add(new VertexInfo(start, distances[start]));

        // pq에 값이 없어질 때까지 반복
        while(!pq.isEmpty()){
            // 최단 거리 꺼내기
            VertexInfo v = pq.remove();
            int currentDistance = distances[v.number];

            // 만약 최단 거리가 저장된 값과 다르다면? 스킵
            if (currentDistance != v.distance){
                continue;
            }

            // 같다면? 연결된 모든 정점 최단 거리 갱신
            for (Edge edge : graph[v.number]){
                // 제거한 간선은 스킵
                if ((removeStart == v.number && removeEnd == edge.end) || (removeStart == edge.end && removeEnd == v.number)){
                    continue;
                }

                // 만약 현재까지 저장된 최단 거리보다 짧다면
                if (currentDistance + edge.length < distances[edge.end]){
                    // 갱신
                    distances[edge.end] = currentDistance + edge.length;

                    // 연결된 부모도 갱신
                    parentNodeArr[edge.end] = v.number;

                    pq.add(new VertexInfo(edge.end, distances[edge.end]));
                }
            }
        }
        return distances[end];
    }

    public static ArrayList<Integer> getShortestPath(int[] parentNodeArr, int start, int end){
        ArrayList<Integer> shortestPath = new ArrayList();
        int currentNode = end;
        shortestPath.add(currentNode);
        while (currentNode != start){
            currentNode = parentNodeArr[currentNode];
            shortestPath.add(currentNode);
        }
        return shortestPath;
    }
}
class Edge{
    public int end;
    public int length;
    public Edge(int end, int length){
        this.end = end;
        this.length = length;
    }
}

// 정점 정보, 해당 정점까지의 거리
class VertexInfo implements Comparable<VertexInfo>{
    public int number;
    public int distance;
    public VertexInfo(int number, int distance){
        this.number = number;
        this.distance = distance;
    }

    @Override
    public int compareTo(VertexInfo v){
        // 짧은 거리 순서
        return Integer.compare(this.distance, v.distance);
    }
}