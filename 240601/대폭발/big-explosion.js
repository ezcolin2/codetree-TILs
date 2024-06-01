const fs = require('fs')
const [n, m, r, c] = fs.readFileSync(0).toString().trim().split(' ').map(Number)
let arr = Array(n).fill(0).map((item)=>Array(n).fill(0))
arr[r-1][c-1] = 1
// 동서남북
const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]

function canGo(x, y){
    return 0<=x && x<n && 0<=y && y<n
}
// time초에 [x][y]에서 폭탄이 터졌을 때
function explode(time){
    // 2차원 배열 깊은 복사
    // 폭탄이 생성되자마자 바로 터지는 것을 방지
    const temp = arr.map((item)=>[...item])
    for (let x=0;x<n;x++){
        for (let y=0;y<n;y++){
            // 폭탄이 있으면 터뜨림
            if (arr[x][y]){
                // 이동할 횟수
                const distance = 2**(time-1)
                for (let i =0;i<4;i++){
                    const [nx, ny] = [x+dx[i]*distance, y+dy[i]*distance]
                    if (canGo(nx, ny)){
                        temp[nx][ny] = 1 // 기존에 폭탄이 있어도 덮어 씌우기
                    }
                }
            }
        }
    }
    // 원본에 적용 
    arr = temp.map((item)=>[...item])

}
// 1초가 지날 때마다 실행
for (let i = 1;i<=m;i++){
    // 모든 격자를 탐색하면서 폭탄 조사
    explode(i)
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