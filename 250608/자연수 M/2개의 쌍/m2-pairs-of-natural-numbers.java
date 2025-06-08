import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 숫자 정보 배열
        Number[] numbers = new Number[n];
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            numbers[i] = new Number(x, y);
        }
        Arrays.sort(numbers);
        int res = 0;
        // 가장 작은 것과 가장 큰 것을 two pointer로 매칭하기
        int left = 0;
        int right = n-1;
        while (left<right){
            // 만약 둘이 같다면?
            if (numbers[left].count == numbers[right].count){
                numbers[left].count = 0;
                numbers[right].count = 0;
                res = Math.max(res, numbers[left].number+numbers[right].number);
                left += 1;
                right -= 1;
            }
            // 왼쪽이 더 크다면
            else if (numbers[left].count > numbers[right].count){
                numbers[left].count -= numbers[right].count;
                numbers[right].count = 0;
                res = Math.max(res, numbers[left].number+numbers[right].number);
                right -= 1;
            }
            // 오른쪽이 더 크다면
            else{
                numbers[right].count -= numbers[left].count;
                numbers[left].count = 0;
                res = Math.max(res, numbers[left].number+numbers[right].number);
                left+=1;
            }
        }
        // 만약 left와 right가 똑같아졌다면 딱 한 종류의 수만 남은 것
        if (numbers[left].count > 0){
            res = Math.max(res, 2*numbers[left].count);
        }
        System.out.println(res);
    }
}
class Number implements Comparable<Number>{
    int count;
    int number;
    public Number(int count, int number){
        this.count = count;
        this.number = number;
    }
    @Override
    public int compareTo(Number number){
        return Integer.compare(this.number, number.number);
    }
}

