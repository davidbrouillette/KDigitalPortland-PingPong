

class Game {
    constructor(data){
        console.log(JSON.stringify(data));
        this.player1 = data.player1;
        this.player2 = data.player2;
        this.winner = data.winner;
        this.score = {
            player1: data.score.player1,
            player2: data.score.player2
        }
    }
}

module.exports = Game;