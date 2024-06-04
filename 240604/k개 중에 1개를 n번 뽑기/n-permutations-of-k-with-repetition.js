const fs = require('fs');
		const [k, n] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
		const arr = [];
		function choose(curIdx){
			if (curIdx == n){
				console.log(arr.join(' '));
				return;
			}
			else{
				for (let i=1;i<=k;i++){
					arr.push(i);
					choose(curIdx+1);
					arr.pop()
				}
			}
		}
        choose(0);