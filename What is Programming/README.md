# What is Programming

- [What is Programming](#what-is-programming)
  - [Web Development Language](#web-development-language)
    - [Lesson 1: Introduction](#lesson-1-introduction)
    - [Front End vs Back End](#front-end-vs-back-end)
    - [Front End Languages](#front-end-languages)
    - [Back-End Languages](#back-end-languages)

## Web Development Language

### Lesson 1: Introduction

Hello and welcome to this course on learning "What is Programming"! In this course, we're going to be looking at words, terms, and concepts in the worlds of web technology and programming. This course isn't going to dive into the nitty gritty details of how a web request is converted to bits and sent across the wire as electrical pulses...and that level of detail of explanation is already significantly more complicated and low-level than we'll be diving!

In this course, we'll be looking at five main sections:

- Web Languages
- Programming
- Standards
- Version Control
- Disparate Web Terms

**Web Languages**:

The web is a wide and varied place. Many people spend their entire careers in the world of web development. So in this section, we'll be looking at:

- front end vs back end
- Front-end languages
- Back-end languages

**Programming**:

The notion of "programming" can be a little cryptic if you haven't ever done it before. What exactly does a programmer _do_? How does one become a programmer? In this section, we'll look at:

- Syntax
- Text Editors
- Programming
- Estimating how long it takes to "program"

**Standards**:

Where do programming languages come from? How are they developed? What in the world is a "spec"? We'll look at these questions and others in the following topics:

- How HTML and CSS are developed
- How JavaScript is developed
- How Python is developed

**Version Control**:

Version Control is incredibly powerful and is used by any programmer that's worth their weight. In the following sections, we'll look at what Version control is, how it works, and other parts of the version control ecosystem. The topics in this section are:

- Why Version Control is needed
- How Version Control works
- Where GitHub fits
- What a PR is
  
**Disparate Web Terms**:

The web is a huge place, and not everything fits neatly into the "front end" or the "back end". There are terms that span both or terms that are tangentially related. In this section on "Disparate Web Terms", we'll be looking at terms and concepts that are in the world of web development but don't fit cleanly in "front end", "back end", or "version control". The topics in this section are:

- Web Requests
- Debugging
- Databases and APIs
- Markdown vs Markup
- Libraries and Frameworks
- CMS
- Command Line

### Front End vs Back End

[![Image Alt Text Here](https://img.youtube.com/vi/BiSNb2queic/0.jpg)](https://www.youtube.com/watch?v=BiSNb2queic)

We just looked at a number if important terms in this video, so let's go over them a bit more. We looked at:

- the client
- a server
- the front end
- the back end
- and full stack

When a developer uses the word "client", they could mean the person that's making a request but, more commonly, "client" is used to refer to the user's browser. Now, in contrast to the "client", there's the "server". A server is just a computer that's waiting to provide information. There's nothing really special about a server. It's just a computer with specific software installed on it. With the right software, you could turn your computer into a server.

Front end, front-end languages, and front-end development...all of this takes place on the client/browser. The front-end languages are:

- HTML
- CSS
- JavaScript

So a front-end developer is someone that's working with HTML, CSS, and JavaScript files to build what users see on the client (in their browser).

Back end, back-end languages, and back-end development...all of these take place on the server. There are actually many back-end languages, so we'll look at them more in the Back-end Languages section.

Now, if a developer is working on the front end and the backend, then they are what's known as a full-stack developer.

### Front End Languages

[![Image Alt Text Here](https://img.youtube.com/vi/y3Susu1gDD4/0.jpg)](https://www.youtube.com/watch?v=y3Susu1gDD4)

**Programming**:

There are many definitions of what "programming" is. Some are helpful, while others end up being pretty cryptic. Let's define "programming" as:

> a tool (written instructions) you use to tell the computer what to do

There are a number of requirements that make up programming language, but we'll limit them to just a few. A programming language needs to have:

- data
- data structures
- flow control

For a programming language to work, it must keep track of data (information). Think of any website you've ever interacted with, it stores information and presents it to you in some way. A programming language is (or more likely multiple programming languages are) responsible for presenting this data to you.

A programming language must have its own means of storing that data internally. The different ways it can store/represent this data internally are called data structures. Data structure is a abstract-y sounding word, but you're probably familiar with many of types of data structures that make up a programming language:

- string - just plain characters of text wrapped in quotes (e.g. `"Richard"`, `'Udacity'`, `"Supercalifragilisticexpialidocious"`)
- number - literally just numbers (e.g `1`, `0`, `117`)
- array or list - a list of items (e.g. an array of numbers: `[1, 3, 9]`, a list of strings: `['Richard', 'Udacity', 'one', 'apple', 'ice cream']`)
- object or dictionary - a key/value pair (e.g. `{firstName: 'Richard'}`)
 
A programming language must be able to perform actions based off of some information or event. For example, here are some flow control structures that most programming languages have:

- `if` - perform some action _if_ something else is true
  - if the jar is not full, add one piece of candy to the jar
- `if / else` - perform some action _if something is true, otherwise (else) perform a different action
  - if the jar is full, empty it out
  - otherwise (else!), add another piece of candy to the jar
- while - keep doing an action while
  - while the jar is not full, add one new piece of candy to the jar every second

Now that we've looked at what makes up a programming language, let's look at the front-end languages.

**Front-end Languages**:

We already saw that the front-end languages are HTML, CSS, and JavaScript. I like to think of these being the three main sections that make up a website:

- HTML = the structure of the website
- CSS = how the website looks
- JavaScript = how the website functions

**HTML**:

HTML stands for "HyperText Markup Language". HTML is not a programming language. Instead, it's a markup language. Markup is just text that's been marked up with special characters. In HTML, some of the marked up pieces of text are called **tags**.

![images](images/1.png)

**CSS**:

CSS stands for "Cascading Style Sheet". CSS is also not a programming language. CSS is a set of rules that specify how the HTML tags should be displayed.

Here is a CSS rule:

```cs
h1 {
    text-align: center;
}
```

The CSS here is telling the `h1` HTML tag that it should display its text aligned to the center (as opposed to being left aligned or right aligned).

**JavaScript**:

JavaScript is what controls the functionality of a website. Since it _is_ a programming language, it can do so many things! For example, if a popup window appears, that's JavaScript. If you fill out a form but enter something incorrectly and the form changes color and displays an error message...that's JavaScript!

> Capital S
> One thing to note, the capital S in "JavaScript" isn't a mistake!

I said it before, but JavaScript _is_ a programming language. Because it is, that means that JavaScript has all of the things we looked at earlier in the section on what makes up a programming language.

JavaScript:

- controls data
- has different data structures
  - number
  - string
  - array
  - object
- flow control
  - if
  - while

**Udacity Content**:

If you're interested in learning more about front-end languages and front-end development, check out:

the [Front End Nanodegree Program][1]
the [Intro to HTML and CSS course][2]
the [Intro to JavaScript course][3]

**Further Research**:

To dig into front-end technology a bit more, some other good resources would be the Mozilla Developer Network (commonly abbreviated to just "MDN"):

- the [HTML guide][4] on MDN
- the [CSS guide][5] on MDN
- the [JavaScript guide][6] on MDN

### Back-End Languages

Many Back-end Languages
There are only three front-end languages (HTML, CSS, and JavaScript), but there are maaaaany back-end languages!

- Python
- PHP
- Ruby
- JavaScript
- Go
- Java
- C++
- C#
...and the list keeps going!

> Udacity Teaches Python
> The [Full Stack Nanodegree Program][7] covers python. So if you're interested in learning it, check out that link!

**Purpose of a back-end language**:

A back-end language can do many, many things, but some of the main responsibilities are:

- to process data
- determine what files/content to send to the front end
- build up the HTML, CSS, and JavaScript files

Both front-end programming languages and back-end programming languages can do data processing. When a front-end programming language does data processing it's using the client's (or more clearly, the user's) computer to do the processing. While when a back-end programming language does data processing, the server is doing it. Typically, a server is going to be much more powerful, and therefore faster than the average person's personal computer.

Once all of the data has been processed, the back-end language will build up the HTML, CSS, and JavaScript files with the content they need. And then it will send these files to the client to be displayed.

**All Together Now**:

So we looked at front-end languages, and now we've just looked at back-end languages. These are the pieces we have so far, so let's put them together:

- a user types in a website in their browser
- the client (the browser) sends out a request for the website
- the server receives that request
- the back-end language (e.g. Python) determines what data and files to send back
- the server sends a response to the client with the data and all of the website files
- the client constructs the website by looking at the structure of the HTML file, styling from the CSS file(s), and functionality provided by the JavaScript file(s)

**Udacity Content**:

If you're interested in learning more about back-end languages and back-end development, check out:

- the [Full Stack Nanodegree] Program
- the [Programming Foundations with Python] course

**Further Research**:

To dig into back-end technology a bit more, check out the following resources:

- <https://www.python.org/>
- <https://www.ruby-lang.org/en/>
- <http://www.php.net/>
- <https://nodejs.org/en/>
- <https://golang.org/>

<!-- urls/paths -->
[1]: https://www.udacity.com/course/front-end-web-developer-nanodegree--nd0011
[2]: https://www.udacity.com/course/intro-to-html-and-css--ud001 
[3]: https://www.udacity.com/course/intro-to-javascript--ud803
[4]: https://developer.mozilla.org/en-US/docs/Web/HTML
[5]: https://developer.mozilla.org/en-US/docs/Web/CSS
[6]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[7]: https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044
[8]: https://www.udacity.com/course/introduction-to-python--ud1110
