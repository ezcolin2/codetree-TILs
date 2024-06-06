const fs = require('fs');
const [k, n] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

// 뽑은 숫자들
const combination = [];

// cnt 자리에 숫자를 선택하는 하뭇
function makeCombination(cnt){

    // n 개를 선택했을 때
    if (cnt == n){
        console.log(combination.join(' '));
        return;
    }
    
    // 1이상 k이하 숫자를 선택
    for (let i=1;i<=k;i++){
        if (cnt>=2 && i == combination[cnt-1] == combination[cnt-2]){
            return;
        }
        combination.push(i);
        makeCombination(cnt+1);
        combination.pop();
    }
}
makeCombination(0);