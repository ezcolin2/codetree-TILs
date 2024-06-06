const fs = require('fs');
const n = Number(fs.readFileSync(0).toString().trim())

// 연속 동일 부분 수열이 없으면 true 반환 
function isPossible(arr){
    // 비교할 부분 수열의 길이
    for (let i=1;i<=parseInt(arr.length/2);i++){
        // 해당 길이의 부분 수열 중 연속된 동일 부분 수열이 있는지 체크
        // j는 비교 시작 인덱스
        for (let j=0;j<=arr.length-i*2;j++){
            // 부분 수열의 길이만큼 비교
            let cnt = 0;
            for (let k=0;k<i;k++){
                if (arr[j+k] == arr[j+i+k]){
                    cnt++;
                }
            }
            // 연속된 동일 부분 수열 존재
            if (cnt == i){
                return false;
            }
        }
    }
    return true;
}
// console.log(isPossible([4, 5, 5, 4]));

const combination = [];
// idx에 어떤 수를 넣을지
function makeCombination(idx){
    if (idx == n){
        console.log(combination.join(''));
        process.exit(0);
    }
    for (let i=4;i<=6;i++){
        combination.push(i);
        if (isPossible(combination)){
            makeCombination(idx+1);
        }
        combination.pop();
    }
}
makeCombination(0);