const fs = require('fs')

const input = fs.readFileSync(0).toString().trim().split('\n')
const n = Number(input[0])
const arr = input.slice(1, n+1).map((item)=>item.trim().split(' ').map(Number))
let [r, c, m1, m2, m3, m4, dir] = input[n+1].split(' ').map(Number)
newR = r-1
newC = c-1
// 방향 거꾸로
let stepCount = []
let dr = []
let dc = []
if (dir == 1){
    stepCount = [m1, m2, m3, m4]
    dr = [-1, -1, 1, 1]
    dc = [1, -1, -1, 1]
}
else {
    stepCount = [m4, m3, m2, m1]
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, 1, -1]
}

// 한 번 회전하는 함수
function rotate(){

    // 시작 데이터 저장
    const initial = arr[newR][newC]
    for (let i = 0;i<4;i++){
        for (let j = 0;j<stepCount[i];j++){
            const nr = newR + dr[i]
            const nc = newC + dc[i]
            // 한 칸 땡김
            arr[newR][newC] = arr[nr][nc] 
            if (nr == r-1 && nc == c-1){
                arr[newR][newC] = initial
            }
            newR= nr
            newC=nc
        }
    }
}

rotate()

arr.map((temp)=>{
    console.log(temp.join(' '))
})