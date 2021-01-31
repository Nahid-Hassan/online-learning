// Being able to store a function in a variable makes it really simple
// to pass the function into another function. A function that is passed
// into another function is called a callback.

// function expression catSays
var catSays = function(max) {
  var catMessage = "";
  for (var i = 0; i < max; i++) {
    catMessage += "meow ";
  }
  return catMessage;
};

// function declaration helloCat accepting a callback
function helloCat(callbackFunc) {
  return "Hello " + callbackFunc(30);
}

// pass in catSays as a callback function
console.log(helloCat(catSays));
