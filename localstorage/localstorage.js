'use strict';

function isLocalStorageAvailable() {
    try {
        return 'localStorage' in window && window['localStorage'] !== null;
    } catch (e) {
        return false;
    }
}

var dictionary = {
    get: function() {
    },
    alrt: function() {
	alert('hi');
    }
};

(function() {
    console.log("localStorage avialability: " + isLocalStorageAvailable());

//    document.getElementById("store_button").setAttribute ('onclick',dictionary.alrt());
//    ^^^ This is wrong it executes stuff immediately
//
    document.getElementById("store_button").addEventListener('click', dictionary.alrt, false);

    localStorage.setItem('key', 'value');
    localStorage.setItem('foo', 'bar');
}());
