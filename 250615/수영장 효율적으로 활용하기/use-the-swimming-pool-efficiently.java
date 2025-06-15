import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int left = 0;
        int right = 144000000;
        int res = Integer.MAX_VALUE;
        while (left<=right){
            int mid = (left+right)/2;
            if (isPossible(n, m, arr, mid)){
                right = mid-1;
                res = Math.min(res, mid);
            }
            else{
                left = mid+1;
            }
        }
        System.out.println(res);
    }
    // 각 레인 별 수영장 이용 시간 총합이 totalTime 이하가 가능하면 true 아니면 false 반환
    public static boolean isPossible(int n, int m, int[] arr, int totalTime){
        int cnt = 1; // 레인 개수
        int currentTotalTime = 0;
        for (int i=0; i<n; i++){
            if (currentTotalTime+arr[i] <= totalTime){
                currentTotalTime += arr[i];
            } else{
                cnt += 1;
                currentTotalTime = arr[i];
            }
        }
        if (cnt <= m){
            return true;
        }
        return false;
    }
}