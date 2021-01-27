// ex-1
var studentName = "John";
var haveEnrolledInCourse = true;
var haveCompletedTheCourse = false;

if (haveEnrolledInCourse){
    console.log("Welcome "+studentName+" to Udacity!"); // Will run only if haveEnrolledInCourse is true
}

// ex-2
var a = 10;
var b = 20;
// a comparison - we will study this in detail in upcoming lesson
if (a>b) // The outcome of a>b will be a boolean
    console.log("Variable `a` has higher value"); // if a>b is true
else
    console.log("Variable `b` has higher value"); // if a>b is false

// ex-3
if(1){
    console.log("This statement will always execute because conditional is set to 1 i.e., true");
}

if(0){
        console.log("This statement will NEVER execute because conditional is set to 0 i.e., false");
}
