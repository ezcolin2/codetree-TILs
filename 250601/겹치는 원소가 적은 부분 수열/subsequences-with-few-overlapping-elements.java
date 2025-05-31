import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // 원소의 개수를 저장하는 CounterHashMap
        CounterHashMap map = new CounterHashMap();
        int left = 0;
        int right = 0;
        int res = 0;
        map.add(arr[right]);
        while (right < arr.length){

            // 만약 개수가 k개를 넘었다면
            if (map.get(arr[right]) >= k){
                left += 1;
                map.remove(arr[left]);
            }

            // 넘지 않았다면?
            else{
                res = Math.max(res, right-left+1);
                // 넣기
                map.add(arr[right]);
                right += 1;

            }
        }
        System.out.println(res);
    }
}
class CounterHashMap{
    Map<Integer, Integer> map;
    public CounterHashMap(){
        map = new HashMap();
    }
    public void add(int key){
        // 가지고 있다면 값 증가
        if (this.map.containsKey(key)){
            this.map.put(key, this.map.get(key)+1);
        }
        // 가지고 있지 않다면 1로 초기화
        else{
            this.map.put(key, 1);
        }
    }
    public void remove(int key){
        // 딱 하나 있었다면 제거
        if (this.map.get(key) == 1){
            this.map.remove(key);
        }
        // 더 있었다면 값 감소
        else{
            this.map.put(key, this.map.get(key)-1);
        }
    }
    public int get(int key){
        // 없으면 0 반환
        if (!this.map.containsKey(key)){
            return 0;
        }
        // 있으면 반환
        else{
            return this.map.get(key);
        }
    }
}