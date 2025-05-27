import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
public class Main {
    public static int[][] grid;
    public static boolean[][] visited;
    public static int current_x;
    public static int current_y;
    public static int[] dx = {0, 0, 1, -1};
    public static int[] dy = {1, -1, 0, 0};
    public static Queue<int[]> queue;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        current_x = sc.nextInt()-1;
        current_y = sc.nextInt()-1;

        // k번 반복
        for (int i=0; i<k; i++){
            // 움직이지 못 한다면 스킵
            if (!is_possible()){
                continue;
            }
            move();
        }
        System.out.printf("%d %d", current_x+1, current_y+1);
    }
    // 현재 위치에서 시작이 가능한지
    public static boolean is_possible(){
        for(int i=0; i<4; i++){
            int nx = current_x+dx[i];
            int ny = current_y+dy[i];
            // 범위 벗어나면 스킵
            if (nx<0 || nx>=grid.length || ny<0 || ny>=grid[0].length){
                continue;
            }
            // 만약 이동 가능한 곳이 한 곳이라도 있으면 true 반환
            if (grid[nx][ny] < grid[current_x][current_y]){
                return true;
            }
        }
        return false;
    }

    // 이동
    public static void move(){
        int nx = -1;
        int ny = -1;
        int maxValue = -1;
        visited = new boolean[grid.length][grid[0].length];
        queue = new LinkedList();
        queue.add(new int[]{current_x, current_y});
        visited[current_x][current_y] = true;
        while (!queue.isEmpty()){
            int[] current = queue.remove();

            // 우선 현재까지 이동할 곳 갱신
            if (grid[current[0]][current[1]] > maxValue && grid[current[0]][current[1]] != grid[current_x][current_y]){
                nx = current[0];
                ny = current[1];
                maxValue = grid[current[0]][current[1]];
            }
            // 같다면?
            else if (grid[current[0]][current[1]] == maxValue){
                if (nx > current[0] || (nx == current[0] && ny > current[1])){
                    nx = current[0];
                    ny = current[1];
                    maxValue = grid[current[0]][current[1]];
                }

            }            
            for (int i=0; i<4; i++){
                int next_x = current[0]+dx[i];
                int next_y = current[1]+dy[i];
                // 범위 벗어나면 스킵
                if (next_x<0 || next_x>=grid.length || next_y<0 || next_y>=grid[0].length){
                    continue;
                }
                // 값이 같거나 크면 스킵
                if (grid[next_x][next_y] >= grid[current_x][current_y]){
                    continue;
                }
                // 방문했으면 스킵
                if (visited[next_x][next_y]){
                    continue;
                }
                queue.add(new int[]{next_x, next_y});
                visited[next_x][next_y] = true;
            }
        }
        
        // 만약 이동하지 못 한다면 그대로
        if (nx == -1 && ny == -1){
            return;
        }
        current_x = nx;
        current_y = ny;

    }
}