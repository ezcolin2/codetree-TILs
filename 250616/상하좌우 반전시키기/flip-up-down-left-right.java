import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 동서남북 
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        for (int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int cnt = 0;
        for (int i=0; i<n-1; i++){
            for (int j=0; j<n; j++){
                // 0이면 (i+1, j)를 선택해야 한다.
                if (arr[i][j] == 0){
                    cnt++;
                    int x = i+1;
                    int y = j;
                    if (arr[x][y] == 1){
                        arr[x][y] = 0;
                    } else{
                        arr[x][y] = 1;
                    }
                    for (int k=0; k<4; k++){
                        int nx = x+dx[k];
                        int ny = y+dy[k];
                        if (nx<0 || nx>=n || ny<0 || ny>=n){
                            continue;
                        }
                        if (arr[nx][ny] == 1){
                            arr[nx][ny] = 0;
                        } else{
                            arr[nx][ny] = 1;
                        }
                    }
                }
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        for (int i=0; i<n; i++){
            if (arr[n-1][i] == 0){
                cnt = -1;
            }
        }
        bw.write(String.valueOf(cnt));
        bw.close();
    }
}