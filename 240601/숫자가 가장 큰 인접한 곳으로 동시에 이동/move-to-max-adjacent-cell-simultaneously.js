const fs = require('fs')

const input = fs.readFileSync(0).toString().trim().split('\n')
const [n, m, t] = input[0].trim().split(' ').map(Number)
// 격자판 정보
const arr = input.slice(1, n+1).map((item)=>item.trim().split(' ').map(Number))
// 구슬 위치 정보
const marbles = Array(arr.length).fill(0).map(() => Array(arr[0].length).fill(0))
// 구슬 정보 저장
input.slice(n+1, n+m+1).map((item)=> {
        const temp = item.trim().split(' ').map(Number)
        marbles[temp[0]-1][temp[1]-1] = 1
    })

// 상하좌우
const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

function canGo(x, y){
    return 0<=x && x<n && 0<=y && y<n
}
// 1초마다 실행되는 구슬을 이동시키는 함수
function move(){
    const tempMarvles = marbles.map((item)=>[...item])
    // 모든 격자판 조사하면서 구슬 여부 확인
    for (let i=0; i<n;i++){
        for (let j=0;j<n;j++){
            // 구슬이 있으면 이동시킴
            if (tempMarvles[i][j]){
                // [숫자, x좌표 y좌표] 저장 후 숫자가 가장 큰 좌표 찾아내기 위한 배열
                temp = [-1, -1, -1]
                for (let k=0;k<4;k++){
                    const [nx, ny] = [i+dx[k], j+dy[k]]
                    // 크다면 이동
                    if (canGo(nx ,ny) && arr[nx][ny] > temp[0]){
                        temp = [arr[nx][ny], nx, ny]
                    }
                }
                if (temp[0]!=-1){
                    marbles[temp[1]][temp[2]]+=1
                    marbles[i][j]=0
                }

            }
        }
    }
    // 동시에 구슬을 이동하기 때문에 한 바퀴 돈 다음 충돌 검사
    for (let i=0; i<n;i++){
        for (let j=0;j<n;j++){
            // 충돌 났다면 제거
            if(marbles[i][j]>1){
                marbles[i][j] = 0
            }
        }
    }
}

for (let i=0;i<t;i++){
    move()

}
let res = 0
for( let j =0; j<n;j++){
    for (let k =0;k<n;k++){
        if (marbles[j][k]==1{
            res++
        }
    }
}
console.log(res)