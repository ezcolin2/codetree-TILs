const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0].trim());
const arr = input.slice(1).map((item)=>item.trim().split(' ').map(Number));
arr.sort((a, b)=> a[0]-a[b] || a[1]-b[1])
// 각 선분 방문 여부
const isVisited = Array(n).fill(false);
// 모든 경우에 대한 선문 수
const res = [];
// 현재 개수
let currentCnt = 0;
// 현재까지 방문한 좌표 
const currentCoordinates = []
// 겹치는지
function isOverrapped(idx){
    for (let i=0;i<currentCoordinates.length;i++){
        if (i==idx){
            continue;
        }
        if (idx<i && arr[idx][1] >= arr[i][0]){
             return true;
        }
        if (idx>i && arr[i][1] >= arr[idx][0]){
            return true;
        }
    }

    return false;
}
function backTracking(idx){
    if (idx==n){
        res.push(currentCnt);
        return;
    }
    // // 방문했거나 겹치면 다음 
    // if (isVisited[idx] || isOverrapped(idx)){
    //     backTracking(idx+1);
    //     return;
    // }
    // 경우의 수
    for (let i=0;i<n;i++){
        // 방문하지 않았고 겹치지 않는다면
        if (!isVisited[i] && !isOverrapped(i)){
            isVisited[i] = true;
            currentCoordinates.push([arr[i]]); // 방문한 좌표 정보 넣음
            currentCnt++;
            backTracking(idx+1);
            isVisited[i] = false;
            currentCoordinates.pop();
            currentCnt--;
        }
    }
    res.push(currentCnt);

}
backTracking(0);
res.sort((a, b)=>b-a);
console.log(res[0]);