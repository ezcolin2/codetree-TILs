const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0].trim());
const [r, c] = input[input.length-1].trim().split(' ').map(Number);
// 숫자
const number = input.slice(1, n+1).map((item)=>item.trim().split(' ').map(Number));
// 방향
const direction = input.slice(n+1, input.length-1).map((item)=>item.trim().split(' ').map(Number));
// 방향
// 계산의 편의를 위해 인덱스 0에는 의미 없는 숫자 넣기
const dx = [0, -1, -1, 0, 1, 1, 1, 0, -1];
const dy= [0, 0, 1, 1, 1, 0, -1, -1, -1];

function canGo(x, y){
    return 0<=x && x<n && 0<=y && y<n;
}
let res = 0;
function dfs(x, y, cnt){
    if (cnt > res){
        res = cnt;
    }
    const currNumber = number[x][y];
    const currDirection = direction[x][y];
    // 좌표를 벗어날 때까지 반복
    while(true){
        let [nx, ny] = [x+dx[currDirection], y+dy[currDirection]];
        // 갈 수 있다면
        if (canGo(nx, ny)){
            if (number[nx][ny] > number[x][y]){
                dfs(nx, ny, cnt+1);
            }
        } else{
            break;
        }

        [x, y] = [nx, ny];
    }
}
dfs(r-1, c-1, 0);
console.log(res);