const gpio = require('onoff').Gpio;

class Pin{
	constructor(pinNumber, name){
		this.gpioInterface = new gpio(pinNumber, 'out');
		this.pinNumber = pinNumber;
		this.name = name;
		this.currentStatus = false;
	}

	updateState(state){
		this.currentState = state;
	}

	on(){
		this.gpioInterface.writeSync(1);
		this.updateState(1);
	}

	off(){
		this.gpioInterface.writeSync(0);
		this.updateState(0);
	}

	write(state){
		this.gpioInterface.writeSync(state);
		this.updateState(state);
	}

}


module.exports = Pin;

