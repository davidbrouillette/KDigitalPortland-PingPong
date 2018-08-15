
class Stats {
    constructor(data){
        this.wins = data.wins ? data.wins : 0,
        this.loses = data.loses ? data.loses : 0,
        this.games = data.game ? [data.game] : []
    }
}


module.exports = Stats;