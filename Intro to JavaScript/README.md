# Introduction to JavaScript

Learn the fundamentals of JavaScript syntax. Explore JavaScript fundamentals by learning how to define variables and use data types to represent data in your code.

- [Introduction to JavaScript](#introduction-to-javascript)
  - [LESSON 1 (What is JavaScript?)](#lesson-1-what-is-javascript)
    - [History of JavaScript](#history-of-javascript)
    - [The JavaScript Console](#the-javascript-console)
    - [console.log](#consolelog)
    - [JavaScript Demo](#javascript-demo)
  - [Data Types and Variables](#data-types-and-variables)
    - [Numbers](#numbers)
    - [Comments](#comments)

## LESSON 1 (What is JavaScript?)

Learn the history of JavaScript and start writing your code immediately using the JavaScript console.

### History of JavaScript

[![Image Alt Text Here](https://img.youtube.com/vi/EbqS33gGrj0/0.jpg)](https://www.youtube.com/watch?v=EbqS33gGrj0)

> TIP: HTML and CSS are markup languages. Markup languages are used to describe and define elements within a document. JavaScript is a programming language. Programming languages are used to communicate instructions to a machine. Programming languages can be used to control the behavior of a machine and to express algorithms.

### The JavaScript Console

Press `CTRL` + `Shift` + `J` to open the JavaScript Console.

| Browser | Keyboard Shortcuts     |
| :------ | :--------------------- |
| Chrome  | `CTRL` + `Shift` + `J` |
| Mozilla | `CTRL` + `Shift` + `i` |

### console.log

`console.log` is used to `display` content to the `JavaScript` console. Run the following code in the console:

```js
console.log("hiya friend!");
// Prints: "hiya friend!"
```

For Chrome users, if you don't see the output, click `“Default levels”` in the console and make sure that "Info" is checked. Congratulations! You performed the `log` action on the debugging `console`.

The message you’ve logged is "hiya friend!". `hiya friend!` is a **string** (a sequence of characters).

**Optional demo example**:

Let’s use console.log to do something a little more interesting. Here’s a block of JavaScript code that loops through the numbers 0 through 9 and prints them out to the console:

```js
for (var i = 0; i < 10; i++) {
  console.log(i);
}

// Prints:
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
```

This is called a loop.

Based on this loop's settings, any code written inside the curly brackets `{...}` will be repeated 10 times. In this case, `console.log` is printing out the value of `i` each time the loop runs. Don't worry if you're not sure about what the syntax means at this point. You will learn more about how and when to use loops later in this course.

### JavaScript Demo

So you saw how to use console.log to print a message to the JavaScript console. Now, let’s see how you can use the console as a sandbox to test a new line of JavaScript in the browser.

Open the [following site](https://daringfireball.net/projects/markdown/) in a new tab and in that tab also open up developer tools. Then paste the following code:

```js
document.getElementsByTagName("h1")[0].style.color = "#ff0000";
```

**Question**: What happened when you ran that line of code in the JavaScript console?

**Answer**: Heading change to be `red`.

Styling elements on the page is great, but you could also do that by just modifying the CSS. What makes JavaScript so special in this case? Refresh the page, then paste this line of code in the JavaScript console.

```js
document.body.addEventListener('click', function () {
     var myParent = document.getElementsByTagName("h1")[0]; 
     var myImage = document.createElement("img");
     myImage.src = 'https://thecatapi.com/api/images/get?format=src&type=gif';
     myParent.appendChild(myImage);
     myImage.style.marginLeft = "160px";
});
```

If you’re confused because nothing happened. Don’t worry. Click somewhere on the page to see the effect. You can refresh the page to return the page its original state.

Add image on the page.

## Data Types and Variables

Learn to represent real-world data using JavaScript variables, and distinguish between the different data types in the language.

### Numbers

Defining a number in JavaScript is actually pretty simple. The Number data type includes any positive or negative integer, as well as decimals. Entering a number into the console will return it right back to you.

```js
3 
// Returns: 3
```

There, you did it.

**Arithmetic operations**:

You can also perform calculations with numbers pretty easily. Basically type out an expression the way you would type it in a calculator.

```js
3 + 2.1
// Returns: 5.1
```

**Comparing numbers**:

What about comparing numbers? Can you do that? Well of course you can!

Just like in mathematics, you can compare two numbers to see if one’s greater than, less than, or equal to the other.

```js
5 > 10
```

Returns: false

```js
5 < 10
```

Returns: true

```js
5 == 10
```

Returns: false

Comparisons between numbers will either evaluate to true or false. Here are some more examples, so you can try it out!

| Operator | Meaning                  |
| :------- | :----------------------- |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or Equal to    |
| >=       | Greater than or Equal to |
| ==       | Equal to                 |
| !=       | Not Equal to             |

```js
// number
console.log(3);

// arithmetic operators
console.log(3 + 2.51);
console.log(3 - 1.5);
console.log(2 + 10 - 19 + 4 - 90 + 1);
console.log(-20 + -19 - (-10) - (-1) + 24);
console.log((10/5) * 4 - 20);
console.log(4096 % 12);

// comparison operators
console.log(43 > 47);
console.log(3 != 0);
console.log(3 == 4);
console.log(3 <= 4);
```

**Output**:

```js
3
5.51
1.5
-92
-4
-12
4
false
true
false
true
```

### Comments

`// You're about to take your first programming quiz!`

Before you move onto the quiz, we want to talk about something you'll see quite often throughout this course: **comments**!

You can use **comments** to help explain your code and make things clearer. In JavaScript, comments are marked with a double forward-slash `//`. Anything written on the same line after the `//` will not be executed or displayed. To have the comment span multiple lines, mark the start of your comment with a forward-slash and star, and then enclose your comment inside a star and forward-slash `/* … */`.

```js
// this is a single-line comment

/*
this is
a multi-line
comment
*/
```

Some of the quizzes in this course might include comments that give you hints or instructions to complete the quiz. Comments are often used to clarify and document non-obvious code. It's good practice to include code comments to improve code readability.
