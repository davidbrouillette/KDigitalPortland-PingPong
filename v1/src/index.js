//const Pin = require('./utils/pin.js');

//const led = new Pin(23);
//var on = 0;

//var blinker = setInterval(()=>{
//	led.write(on);
//	on = (on + 1) % 2;
//	console.log('ON = ' + on);
//}, 1000);

//setTimeout(()=>{
//	clearInterval(blinker);
//}, 12000);
/**
function sleep(ms){
	return new Promise(resolve => setTimeout(resolve, ms));
}

const Match = require('./utils/match.js');

async function main(){
const match = new Match();
match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player2.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);
await sleep(1000);

match.scorePoint(match.player1.name);
console.log(match.currentServer);

}

main();
**/

require('./utils/bluetooth.js');
