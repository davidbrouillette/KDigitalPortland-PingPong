const Pin = require('./pin');
const Player = require('./player');

class Match{
	constructor(pointsInMatch=11, servesPerPlayer=5){
		this.pointsInMatch = pointsInMatch;
		this.servesPerPlayer = servesPerPlayer;
		this.player1 = new Player('player1');
		this.player2 = new Player('player2');
		this.score = {
			[this.player1.name]: 0,
			[this.player2.name]: 0
		}
		this.numberOfServes = 0;
		this.currentServer = this.player1.name;
		this.pin = new Pin(23);
	}

	scorePoint(name){
		this.score[name]++;
		this.numberOfServes++;
		this.checkScores(name);
		this.checkServes();
	}

	checkScores(name){
		if(this.score[name] === this.pointsInMatch){
			this.winScenerio(name);
		}
	}

	checkServes(){
		console.log(this.numberOfServes);
		if(this.numberOfServes > 0 && (this.numberOfServes % this.servesPerPlayer === 0)){
			if(this.currentServer === this.player1.name){
				this.currentServer = this.player2.name;
				this.pin.write(1);
			} else {
				this.currentServer = this.player1.name;
				this.pin.write(0);
			}

		}
	}

	winScenerio(name){
		console.log(`${name} Wins!`);
	}


}

module.exports = Match;

