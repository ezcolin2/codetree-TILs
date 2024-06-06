const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0].trim());
const arr = input[1].trim().split(' ').map(Number);

// 합을 구하면 모든 조합을 구한 다음 그 조합의 합을 여기서 빼면 됨
const sum = arr.reduce((acc, num) => acc+num);

// 조합
const combination = [];

// 최소값 저장할 변수
let res = Number.MAX_SAFE_INTEGER;
// currIdx는 arr의 현재 위치
// cnt는 몇 개 골랐는지
function makeCombination(currIdx, cnt){
    if (currIdx == 2*n){
        if (cnt ==n){
            // n/2개만큼 골랐다면 현재 고른 조합의 합 구함
            const currSum = combination.reduce((acc, num)=>acc+num);
            const abs = Math.abs((sum-currSum)-currSum);
            if (abs<res){
                res = abs;
            }
        }
        return;
    }
    // 해당 위치의 숫자 선택
    combination.push(arr[currIdx]);
    makeCombination(currIdx+1, cnt+1);
    combination.pop();

    // 해당 위치의 숫자 선택하지 않음
    makeCombination(currIdx+1, cnt);
}
makeCombination(0, 0);
console.log(res);