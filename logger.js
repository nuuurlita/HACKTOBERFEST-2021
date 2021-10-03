const {performance} = require('perf_hooks');

function _log(func, ...args){
    const t1 = performance.now();
    const result = func.call(this, ...args);
    const t2 = performance.now();
    console.log(result, `(${(t2 - t1).toFixed(3)}ms)`);
}

module.exports = _log;
