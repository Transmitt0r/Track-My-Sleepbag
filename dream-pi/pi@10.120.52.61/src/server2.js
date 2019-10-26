var Bleacon = require('bleacon');

var uuid = process.env.UUID || 'c8899e80062b41fb87f98238b6633054';
var major = process.env.MAJOR || 0; // 0 - 65535
var minor = process.env.MINOR || 0; // 0 - 65535
var measuredPower = process.env.MEASURED_POWER || -59; // -128 - 127 (measured RSSI at 1 meter)

Bleacon.startAdvertising(uuid, major, minor, measuredPower);

Bleacon.startScanning();
Bleacon.on('discover', function (bleacon) {
    // just use this so our app won't end after starting the beacon has started
});


let signals = {
    'SIGHUP': 1,
    'SIGINT': 2,
    'SIGTERM': 15
};
// Do any necessary shutdown logic for our application here
const shutdown = (signal, value) => {
    Bleacon.stopAdvertising();
    Bleacon.stopScanning();
    console.log(`server stopped by ${signal} with value ${value}`);
    process.exit(128 + value);
};
// Create a listener for each of the signals that we want to handle
Object.keys(signals).forEach((signal) => {
    process.on(signal, () => {
        console.log(`process received a ${signal} signal`);
        shutdown(signal, signals[signal]);
    });
});