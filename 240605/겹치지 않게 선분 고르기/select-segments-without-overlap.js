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
    const [start, end] = arr[idx];
    for (let i=0;i<currentCoordinates.length;i++){
        const [tempStart, tempEnd] = currentCoordinates[i];
        if (start==tempStart){
            return true;
        }
        if (start<tempStart && end>=tempStart){
            return true;
        }
        if (start>tempStart && tempEnd>=start){
            return true;
        }
    }

    return false;
}
function backTracking(){

    // // 방문했거나 겹치면 다음 
    // if (isVisited[idx] || isOverrapped(idx)){
    //     backTracking(idx+1);
    //     return;
    // }
    // 경우의 수
    for (let i=0;i<n;i++){
        // 겹치지 않는다면
        if (!isOverrapped(i)){
            currentCoordinates.push(arr[i]); // 방문한 좌표 정보 넣음
            currentCnt++;
            backTracking();
            currentCoordinates.pop();
            currentCnt--;
        }
    }
    res.push(currentCnt);

}
backTracking();
res.sort((a, b)=>b-a);
console.log(res[0]);