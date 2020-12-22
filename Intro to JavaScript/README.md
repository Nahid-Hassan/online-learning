# Introduction to JavaScript

Learn the fundamentals of JavaScript syntax. Explore JavaScript fundamentals by learning how to define variables and use data types to represent data in your code.

- [Introduction to JavaScript](#introduction-to-javascript)
  - [LESSON 1 (What is JavaScript?)](#lesson-1-what-is-javascript)
    - [History of JavaScript](#history-of-javascript)
    - [The JavaScript Console](#the-javascript-console)
    - [console.log](#consolelog)
    - [JavaScript Demo](#javascript-demo)

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
