const noble = require('noble');

const JOYCON_L_UUID = "7C:BB:8A:EB:EE:0E";

noble.on('stateChange', (state)=>{
	if(state === 'poweredOn'){
		noble.startScanning([], true);
	} else {
		noble.stopScanning();
	}
});

noble.on('discover', (peripheral) => {
//	if(peripheral){
//		peripheral.discoverSomeServicesAndCharacteristics([], (err, servicesw, chrs)=>{
//			console.log("services= " + JSON.stringify(services));
//			console.log("characteristics= " + JSON.stringify(chrs));
//		});

	if(peripheral && peripheral.advertisement && peripheral.advertisement.localName){



//		console.log(`{PERIPHERAL: uuid=${peripheral.uuid} || localName=${peripheral.advertisement.localName} || advertisement=${JSON.stringify(peripheral.advertisement)}`);

		var output = Object.keys(peripheral).map((x)=>{
			if(x === 'advertisement'){
				return `{${x}.localName: ${x.localName} }`;
			} else if(typeof(peripheral[x]) === 'object'){
				return `{${x}: OBJECT}`;
			} else {
				return `{${x}:${peripheral[x]}}`;
			}
		});
		console.log(`PERIPHERAL(${peripheral.uuid}) = ${output}`);


	}
});

setTimeout(()=>{
	console.log('shutting program down');
	process.exit(0);
},20000);
