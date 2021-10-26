(function(){
	var levelData = ["  wwwww ","www   w ","w b w ww","w w  p w","w    w w","wwbwp  w"," wy  www"," wwwww  "], level = [[], [] ,[] ,[] ,[] ,[] ,[] ,[]];
	
	var board=document.getElementById('board');
	
	for(var n=0;n<levelData.length;n++)
		for(var m=0;m<levelData[n].length;m++){
			var div=document.createElement('div');
			level[n].push(div);
			div.className=levelData[n][m] == ' '?'s':levelData[n][m];
			
			board.appendChild(div);
			if(levelData[n][m]=='y') x = m, y = n;
		}
		
	
	
	window.addEventListener('keydown', function(e){
		
		if(e.keyCode==37)dx=-1, dy=0;
		else if(e.keyCode==38)dx= 0, dy=-1;
		else if(e.keyCode==39)dx=1, dy=0;
		else if(e.keyCode==40)dx=0, dy=1;
		else return;
		
		var newPos = level[y+dy][x+dx];
		if(newPos.className=='w')return;
		
		 
		if(newPos.className=='b'|| newPos.className=='a'){
			var newBallPos=level[y+dy+dy][x+dx+dx];
			
			if(newBallPos.className=='w'||newBallPos.className=='b')return;
			newBallPos.className=newBallPos.className=='p'?'a':'b';
			newPos.className=newPos.className=='a'?'p':'s';
		}
		
		
		var thisPos = level[y][x];
		thisPos.className = thisPos.className == 'Y' ? 'p' : 's';
    	newPos.className = newPos.className == 'p' ? 'Y' : 'y';
		
		x += dx, y += dy;
		
		for(var n=0;n<levelData.length;n++)
			for(var m=0;m<levelData[n].length;m++)
				if(level[n][m].className=='b')return;
		
		alert('You win!');
	});
	
})()