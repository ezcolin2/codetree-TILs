import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        int cnt = 0;
        for (int i=0; i<N-1; i++){
            // 0이면 다음 것을 누른다.
            if (arr[i] == 0){
                arr[i] = 1;
                arr[i+1] = (arr[i+1]+1)%2;
                if (i+2<N){
                    arr[i+2] = (arr[i+2]+1)%2;
                }
                cnt++;
            }
        }
        // 모두 1인지 확인
        for (int i=0; i<N; i++){
            if (arr[i] == 0){
                System.out.println(-1);
                return;
            }
        }
        System.out.println(cnt);
    }
}