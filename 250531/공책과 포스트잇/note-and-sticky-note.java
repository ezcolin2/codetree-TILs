/*
    h-index를 알아낼 때, c 값들을 정렬한 뒤, 인덱스와 값을 사용하면 알아낼 수 있다.
    h-index 값이 h를 만족할 수 있는지 확인하려면 총 L*K 만큼의 숫자를 h보다 작은 값들에게 적절히 분배해야 한다.
*/
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static int[] arr;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int l = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // 오름차순 정렬
        Arrays.sort(arr);

        // parametric search 시작
        int left = 0;
        int right = 100000;
        int res = -1;
        while (left <= right){
            int mid = (left+right)/2;
            // 가능하다면 갱신
            if (isPossible(mid, k, l)){
                res = Math.max(res, mid);
                left = mid+1;
            }
            else{
                right = mid-1;
            }
        }
        System.out.println(res);
    }
    /**
        k, l이 주어졌을 때, hIndex가 가능한지 여부 반환
    */
    public static boolean isPossible(int hIndex, int k, int l){
        // 일단 hIndex보다 크거나 같은 값이 처음으로 나오는 인덱스를 구한다.
        int firstIndex = bisectLeft(hIndex);

        // 총 번호를 적을 수 있는 횟수
        long totalCount = (long)k*l;

        // 필요한 공책의 개수를 구한다.
        int count = hIndex - (arr.length - firstIndex);
        
        // l*k 값을 사용해서 적절히 분배한 뒤, hIndex 값이 가능한지 구한다.
        while (count > 0){
            firstIndex -= 1;
            if (firstIndex<0){
                return false;
            }
            // 적어야 하는 개수
            int difference = hIndex - arr[firstIndex];

            // 만약 k보다 큰 값이 필요하거나 번호를 적을 수 있는 횟수가 불가능하면 불가능
            if (difference > k || difference > totalCount){
                return false;
            }

            // 공책에 적기
            totalCount -= difference;
            count -= 1;
        }
        return true;
    }
    /*
        hIndex 보다 크거나 같은 값이 처음으로 나오는 인덱스 반환
    */
    public static int bisectLeft(int hIndex){
        int left = 0;
        int right = arr.length-1;
        int index = arr.length;
        while (left<=right){
            int mid = (left+right)/2;
            // arr[mid] 값이 hIndex보다 같거나 크면 갱신
            if (arr[mid] >= hIndex){
                index = Math.min(index, mid);
                right = mid-1;
            }
            // 작다면 높은 범위로
            else{
                left = mid+1;
            }
        }
        return index;
    }
}