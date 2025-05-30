/*
    1. 최대 높이 최소 높이 차이가 주어질 때, 이게 가능한지 반환
    최대 높이와 최소 높이 차이가 주어지면 가능한 모든 경우의 수를 BFS로 탐색한다.
    정해진 최소 높이와 최대 높이 사이의 칸만 탐색하여 도착점에 도달 할 수 있는지 판단
    시간 복잡도 : O(H x 4 x M x N)

    2. 최대 높이 최소 높이 차이의 경우 이진 탐색으로 진행하여 1번을 실행한다.
    시간 복잡도 : O(log H) x O(HMN)

    최악의 경우 log(500) x 4 x 500 x 100 x 100 대략 1억 8천만
    시간 제한이 5초이기 때문에 넉넉히 통과할 수 있다.
*/
import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
public class Main {
    public static int[][] board;
    public static int[] dx = {0, 0, 1, -1};
    public static int[] dy = {1, -1, 0, 0};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        board = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                board[i][j] = sc.nextInt();
        
        // 이진 탐색 시작
        int left = 0;
        int right = 500;
        int res = 501;
        while (left <= right){
            int mid = (left+right)/2;
            if (isPossibleDifference(mid)){
                res = Math.min(res, mid);
                // 가능하면 범위를 좁혀보기
                right = mid-1;
            }
            // 불가능하면 범위를 넓혀보기
            else{
                left = mid+1;
            }
        }
        System.out.println(res);
    }
    // 해당 차이를 유지하면서 목표 지점까지 도달 가능 여부
    public static boolean isPossibleDifference(int difference){
        for (int minHeight=1; minHeight<=500-difference; minHeight++){
            // 한 번이라도 도달하면 가능
            if (BFS(minHeight, minHeight+difference)){
                return true;
            }
        }
        // 한 번도 도달하지 못 했다면 불가능
        return false;
    }
    
    // 최소 높이, 최대 높이를 유지하면서 탐색 가능한지
    public static boolean BFS(int minHeight, int maxHeight){
        // 만약 출발점부터 안 되면 false 반환
        if (board[0][0] < minHeight || board[0][0] > maxHeight){
            return false;
        }
        boolean[][] visited = new boolean[board.length][board[0].length];
        
        // 첫 번째 점부터 큐에 넣기
        Queue<Pair> queue = new LinkedList();
        queue.add(new Pair(0, 0));
        visited[0][0] = true;

        // 큐가 빌 때까지 반복
        while(!queue.isEmpty()){
            Pair pair = queue.remove();
            int cx = pair.x;
            int cy = pair.y;
            for (int i=0; i<4; i++){
                int nx = cx+dx[i];
                int ny = cy+dy[i];
                
                // 범위 벗어나먼 스킵
                if (nx<0 || nx>=board.length || ny<0 || ny>=board[0].length){
                    continue;
                }

                // 방문했으면 스킵
                if (visited[nx][ny]){
                    continue;
                }

                // 높이 범위 벗어나면 스킵
                if (board[nx][ny] < minHeight || board[nx][ny] > maxHeight){
                    continue;
                }

                // 만약 도달했으면 true 반환
                if (nx == board.length-1 && ny == board[0].length-1){
                    return true;
                }
                // 큐에 넣기
                queue.add(new Pair(nx, ny));
                visited[nx][ny] = true;
            }
        }
        // 큐가 빌 때까지 도달 못 했으면 false 반환
        return false;
    }
}
class Pair{
    public int x;
    public int y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}