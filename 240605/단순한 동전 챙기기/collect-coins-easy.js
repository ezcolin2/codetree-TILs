const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0]);
const arr = input.slice(1).map((item)=>item.trim().split(''));

// 좌표에 존재하는 모든 동전의 숫자
const numList = [];
// 동전의 숫자를 입력하면 그 좌표를 알려주는 Map
const numMap = new Map();
for (let i=0;i<n;i++){
    for (let j=0;j<n;j++){
        if (arr[i][j] != '.'){
            // 좌표 저장
            
            // 시작점과 끝점은 numList에 들어가면 안 됨
            // 계산의 편의를 위해 numMap의 숫자 key들은 모두 숫자로 변경
            if (arr[i][j] != 'S' && arr[i][j] != 'E'){
                numList.push(Number(arr[i][j]));
                numMap.set(Number(arr[i][j]), [i, j]);
            }
            else{
                numMap.set(arr[i][j], [i, j]);
            }
        }
    }
}
numList.sort((a, b)=>a-b);
// 숫자가 a인 동전과 숫자가 b인 동전 사이의 거리
// 숫자가 아닌 'S'와 'E'가 들어갈 수도 있다.
function getDistance(a, b){
    const [ax, ay] = numMap.get(a);
    const [bx, by] = numMap.get(b);
    return Math.abs(ax-bx) + Math.abs(ay-by);
}

// 현재까지 선택한 동전의 숫자들 (nums)에서 각 순서로 이동할 때 이동 횟수
function getTotalDistance(){
    let distance = 0;
    nums.push('E');
    // 조합을 구성할 때 이미 정렬되어 있다.
    // 두 개를 비교할 것이기 때문에 인덱스 1부터 시작
    for (let i=1;i<nums.length;i++){
        distance += getDistance(nums[i], nums[i-1]);
    }
    nums.pop()
    return distance;
}

// 현재까지 선택한 동전의 숫자들
const nums = ['S']
// 최소 이동 횟수
let res = Number.MAX_SAFE_INTEGER;
// currIdx numList[currIdx]를 선택할지 말지
// cnt는 선택한 동전의 개수
function combination(currIdx, cnt){
    if (currIdx == numList.length){
        // 선택한 동전의 개수가 3개 이상이면
        if (cnt >= 3){
            const temp = getTotalDistance();
            res = (res > temp) ? temp : res;
        }
        return;
    }
    // currIdx에 해당하는 동전의 숫자를 선택
    nums.push(numList[currIdx]);
    combination(currIdx+1, cnt+1);
    nums.pop();

    // currIdx에 해당하는 동전의 숫자를 선택하지 않음
    combination(currIdx+1, cnt);
}
combination(0, 0);
console.log(res == Number.MAX_SAFE_INTEGER ? -1 : res);