const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

// 변수 선언 및 입력
const n = Number(input[0]);
const segments = input.slice(1, 1 + n).map(line => line.split(' ').map(Number));

let ans = 0;
const selectedSegs = [];

function overlapped(seg1, seg2) {
    const [ax1, ax2] = seg1;
    const [bx1, bx2] = seg2;

    // 두 선분이 겹치는지 여부는
    // 한 점이 다른 선분에 포함되는 경우로 판단 가능합니다.
    return (ax1 <= bx1 && bx1 <= ax2) || (ax1 <= bx2 && bx2 <= ax2) ||
           (bx1 <= ax1 && ax1 <= bx2) || (bx1 <= ax2 && ax2 <= bx2);
}

function possible() {
    // 단 한쌍이라도 선분끼리 겹치면 안됩니다
    for (let i = 0; i < selectedSegs.length; i++) {
        for (let j = i + 1; j < selectedSegs.length; j++) {
            if (overlapped(selectedSegs[i], selectedSegs[j])) {
                return false;
            }
        }
    }

    return true;
}

function findMaxSegments(cnt) {
    if (cnt === n) {
        if (possible()) {
            ans = Math.max(ans, selectedSegs.length);
        }
        return;
    }

    selectedSegs.push(segments[cnt]);
    findMaxSegments(cnt + 1);
    selectedSegs.pop();

}

findMaxSegments(0);
console.log(ans);