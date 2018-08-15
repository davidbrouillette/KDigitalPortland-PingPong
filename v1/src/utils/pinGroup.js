class PinGroup{
	constructor(name){
		this.name = name;
		this.pins = {};
	}

	addPin(name, pin){
		this.pins[name] = pin;
	}

	removePin(name){
		if(this.pins[name]){
			delete this.pins[name];
		}
	}

	turnOn(name){
		this.pins[name].on();
	}

	turnOff(name){
		this.pins[name].off();
	}

}

modules.exports = PinGroup;
