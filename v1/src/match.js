class Match{
    constructor(firstServer, pointsInMatch, servesPerPlayer){
        this.pointsInMatch = pointsInMatch
        this.servesPerPlayer = servesPerPlayer
        this.player1 = {'name':'player1'}
        this.player2 = {'name':'player2'}
        this.score = {'player1':0, 'player2':0}
        this.numberOfServes = 0
        this.currentServer = firstServer
    }

    setServer(name){
        this.currentServer = name
    }

    scorePoint(name){
        this.score[name] = this.score[name] + 1
        this.numberOfServes = this.numberOfServes + 1
        this.checkScores(name)
        this.checkServes()
        
    }

    checkScores(name){
        if(this.score[name] == this.pointsInMatch){
            this.winScenerio(name)
        }
    }

    winScenerio(name){
        console.log(name + ' wins!')
    }

    checkServes(){
        if((this.numberOfServes > 0) && (this.numberOfServes % this.servesPerPlayer == 0)){
            if(this.currentServer == 'player1'){
                this.currentServer = 'player2'
            } else{
                this.currentServer = 'player1'
            }
        }
            console.log('CurrentServer = ' + this.currentServer)
    }
}