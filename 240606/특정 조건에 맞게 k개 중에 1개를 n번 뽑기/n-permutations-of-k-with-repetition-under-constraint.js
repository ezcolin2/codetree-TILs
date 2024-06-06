const fs = require('fs');
const [k, n] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

// 뽑은 숫자들
const combination = [];

// cnt는 지금까지 선택한 숫자 개수
function makeCombination(cnt){
    // n 개를 선택했을 때
    if (cnt == n){
        console.log(combination.join(' '));
        return;
    }
    
    // 1이상 k이하 숫자를 선택
    for (let i=1;i<=k;i++){
        // 세 개 연속 같은 숫자는 건너뜀.
        if (i>=3 && combination[i-1] == combination[i-2] == combination[i-3]){
            continue;            
        }
        combination.push(i);
        makeCombination(cnt+1);
        combination.pop();
    }
}
makeCombination(0);