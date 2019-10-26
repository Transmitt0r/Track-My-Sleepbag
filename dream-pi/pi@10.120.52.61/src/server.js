let eddy;
const PI = process.env.PI === "true";
if (PI) eddy = require("eddystone-beacon");

let options = {
    name: 'Dreambag1',    // set device name when advertising (Linux only)
    txPowerLevel: -21, // override TX Power Level, default value is -21,
    tlmCount: 2,       // 2 TLM frames
    tlmPeriod: 1      // every 10 advertisements
};

let updateAd = () => {
    let t = new Date().getTime();
    t /= 1000;
    t = t % 100;
    t = parseInt(t);
    console.log(green);
    eddy.advertiseUrl("http://bag.com", options);
    eddy.setTemperature(t);
    // eddy.setBatteryVoltage(500);
};

if (PI) setInterval(updateAd, 500);