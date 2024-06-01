const fs = require('fs')
const [n, m, r, c] = fs.readFileSync(0).toString().trim().split(' ').map(Number)
const arr = Array(n).fill(0).map((item)=>Array(n).fill(0))
arr[r][c] = 1
// 동서남북
const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]

function canGo(x, y){
    return 0<=x && x<n && 0<=y && y<n
}
// time초에 [x][y]에서 폭탄이 터졌을 때
function explode(x, y, time){
    // 이동할 횟수
    const distance = 2**(n-1)
    for (let i =0;i<4;i++){
        const [nx, ny] = [x+dx[i]*time, y+dy[i]*time]
        if (canGo(nx, ny)){
            arr[nx][ny] = 1 // 기존에 폭탄이 있어도 덮어 씌우기
        }
    }
}
// 1초가 지날 때마다 실행
for (let i = 1;i<=m;i++){
    // 모든 격자를 탐색하면서 폭탄 조사
    for (let j=0;j<n;j++){
        for (let k=0;k<n;k++){
            // 폭탄이 있으면 터뜨림
            if (arr[j][k]){
                explode(j, k, i)
            }
        }
    }
}

// 개수 확인
let count = 0
for (let j=0;j<n;j++){
    for (let k=0;k<n;k++){
        // 폭탄이 있으면 증가
        if (arr[j][k]){
            count++
                }
    }
}
console.log(count)