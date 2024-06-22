const fs = require('fs');

const [n, m] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

// 선택한 숫자 조합
const combination = [];
function dfs(currNum, cnt){

    if (currNum == n+1){
        if (cnt == m){
            console.log(combination.join(' '));
        }
        
        return
    }
    // currNum에 해당하는 것을 넣음
    combination.push(currNum);
    dfs(currNum+1, cnt+1);
    combination.pop();

    // 넣지 않음
    dfs(currNum+1, cnt);

}
dfs(1, 0)