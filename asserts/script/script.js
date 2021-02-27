const canvas = document.getElementById("canvas");
const ctx = canvas.getContext('2d');

const sizeCell = 3;

const step = "black";
const wall = "#383a59";
const path = "#bd93f9";

canvas.width = h * sizeCell;
canvas.height = w * sizeCell;

for (let i = 0; i < h; i++){
	for (let j = 0; j < w; j++){
		if (maze[i][j] == "1" || maze[i][j] == "2")
			ctx.fillStyle = step;
		else
			ctx.fillStyle = wall;
		ctx.fillRect(sizeCell * i, sizeCell * j, sizeCell, sizeCell);
	}
}


let flag = true;
let change = button.querySelector("p");

button.addEventListener("click", () => {
	if (flag){
		change.innerHTML = "hide path";
		ctx.fillStyle = path;
		for (let i = 0; i < p-1; i++)
			ctx.fillRect(sizeCell * Path[i][0], sizeCell * Path[i][1], sizeCell, sizeCell);
	}
	else{
		change.innerHTML = "show path";
		ctx.fillStyle = step;
		for (let i = 0; i < p-1; i++)
			ctx.fillRect(sizeCell * Path[i][0], sizeCell * Path[i][1], sizeCell, sizeCell);
	}
	flag = !flag;
});