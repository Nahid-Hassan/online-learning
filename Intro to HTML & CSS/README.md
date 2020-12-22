# Intro to HTML & CSS

- [Intro to HTML & CSS](#intro-to-html--css)
  - [Lesson 1](#lesson-1)
    - [Make your first element](#make-your-first-element)
    - [Text Editors](#text-editors)
    - [Browsers](#browsers)
    - [Trees](#trees)
    - [HTML and Trees](#html-and-trees)
    - [HTML Research](#html-research)
    - [HTML Structure Part 2](#html-structure-part-2)
    - [HTML Documents in Depth](#html-documents-in-depth)

## Lesson 1

### Make your first element

To recap the previous video, your goal is to make three elements:

- One paragraph
- Two spans
Make sure you put some text content in every element!

Here's an example element:

```text
<tag>content</tag>
```

Feel free to use the workspace below to create your elements!

**Solution**:

```html
<p>I'm Cameron!</p>
<span>I like teaching</span>
<span>and web dev :)</span>
```

**Preview**:

```text
I'm Cameron!
I like teaching and web dev :)
```

**Note**: Paragraph in it's own line(paragraph has it own line) but both span tag made one line(span are the parts of the line).

### Text Editors

- Visual Studio Code
- Atom Editor
- Emacs
- VI/VIM [Learn how to use vim](https://www.openvim.com/)

### Browsers

- Google Chrome
- Mozilla Firefox

### Trees

![images](images/1.png)

### HTML and Trees

![images](images/2.png)

| Code                                       | Bug or Not with Description                                                                                                                            |
| :----------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<p>a paragraph<p>`                        | Improperly formatted                                                                                                                                   |
| `<p><em>words, words, words.</em></p>`     | Looks Good                                                                                                                                             |
| `<span...middle of the sentence...</span>` | If you write this in a code editor, you'll notice different coloring on the tags. Syntax color is a clue that things are or aren't properly formatted! |
| `<p><em>words, words, words.</p></em>`     | The other element is the child of the `<p>` element, and as such, you have to close it inside the `<p>`, unlike what was done here.                    |

### HTML Research

Here is the [MDN HTML elements reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) page. Once you're there, click on HTML elements on the left-hand sidebar. Then, search for **bold** and **emphasis** (remember, you can search text on a page using keyboard shortcuts `⌘ + F` for Mac, or `Ctrl + F` for Windows!).

**Solution**:

```html
<strong>This text should be bold.</strong>
<em>And this text should have emphasis (italics).</em>
```

**Preview**:

```text
This text should be bold. And this text should have emphasis (italics).
```

### HTML Structure Part 2

Congratulations! You created your first HTML elements, set up your development environment, streamlined your workflow, and even organized elements on a page using a standard HTML tree structure.

Now, let's take a moment for a little trip down memory lane. Remember this clip from the beginning of the lesson?

![images](images/3.png)

Did it seem odd that it took 10 lines of HTML to create a webpage that only displayed four words? At this point, you know that `<h1>This is a heading.</h1>` is responsible for displaying the heading on the page, but what about the rest of the code?

![images](images/4.gif)

You can think of it as a template. And, following this template will help ensure that the page is displayed as the developer (you) intended. It not only says what should be displayed, but also includes relevant information that tells the browser how to display it.

This template can be broken down into 3 parts:

1. `DOCTYPE`: Describes the type of HTML. While there are technically different types, for 99.999% of the HTML you'll write, you’ll likely be fine with <!DOCTYPE html>.
1. `<head>`: Describes meta information about the site, such as the title, and provides links to scripts and stylesheets the site needs to render and behave correctly.
1. `<body>`: Describes the actual content of the site that users will see.
Omitting some of this information doesn't necessarily mean that the page won't be displayed. In fact, your browser will assume certain parts of the template exist even if you accidentally leave them out. Take this line of HTML for example:

```html
<h1>This is a heading</h1>
```

If you create an HTML file with only this line, open the file in any modern browser, and inspect the page with developer tools, you’ll see that certain parts of the basic HTML document format were assumed:

![images](images/5.png)

The view from the Elements panel in Developer Tools when you omit all but `<h1>...</h1>.` (Notice that an empty `<head>` has been created for you.)

That being said, this is not guaranteed behavior. Older browsers can be unpredictable, and you won’t know what browser your visitors will decide to use. It’s good practice to include all the basic parts of the template so that you aren’t relying on the guesswork of browsers to display your sites correctly.

### HTML Documents in Depth

An HTML document will usually start with a type declaration (which is not a tag, so it should not have a closing tag). The declaration helps the browser determine what type of HTML document it’s trying to parse and display.

If you’ve ever looked at an older website using dev tools, you might have noticed a doctype that looks like this:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

(Triggers Standards mode but specifies an older form of validation.)
```

Or maybe you didn’t see a doctype at all?

```html
<html>
    … 
</html>

(Triggers “Quirks” mode. This is bad.)
```

But newer websites (and your websites!) will have a declaration that looks like this:

```html
<!DOCTYPE html>

(Triggers Standards mode with all updated features.) 😊
```

Browsers look for this doctype declaration to determine which rendering mode to use to render the site. Generally, newer sites follow standard HTML specifications. The current standard HTML specification is called HTML5 (which is what you're learning!). On the other hand, older sites, created before HTML standards really existed, might use a different rendering mode that imitates the behavior of older browsers.

If you are interested in reading more about doctype declarations and different rendering modes, you can read about them here.

Once you’ve declared the doctype, the next part of your HTML document is the `<html>` tag, which tells the browser that everything enclosed inside the `<html> ... </html>` should be parsed as HTML. Then you have the two main sections of your HTML document: `<head>` and `<body>`

![images](images/6.png)

**`<head>` and `<body>`**:

The `<head>` will contain general information and metadata about the page, while the `<body>` will contain the content that will be displayed on the page. Here’s an example tree structure for a full HTML document:

![images](images/7.png)

All of the HTML syntax that you’ve learned in this lesson will help you create the content of the page, which is always contained inside the <body> tags. The <body> is always visible.

The <head>, on the other hand, is never visible, but the information in it describes the page and links to other files the browser needs to render the website correctly. For instance, the <head> is responsible for:

- the document’s title (the text that shows up in browser tabs): <title>About Me</title>.
- associated CSS files (for style): <link rel="stylesheet" type="text/css" href="style.css">.
- associated JavaScript files (multipurpose scripts to change rendering and behavior): <script src="animations.js"></script>.
- the charset being used (the text's encoding): <meta charset="utf-8">.
- keywords, authors, and descriptions (often useful for SEO): <meta name="description" content="This is what my website is all about!">.
- … and more!

At this point, just focus on these two tags:

```html
<title>About Me</title>
<meta charset="utf-8">
```

`<meta charset="utf-8">` is pretty standard, and will allow your website to display any Unicode character. (Read more on how UTF-8 works here.) `<title>` will define the title of the document and will be displayed in the tab of the browser window when a user visits the page.

![images](images/8.png)

**HTML Validators**:

This might seem like a lot to remember, but thankfully, there are tools out there to help you. Much like how the Udacity Feedback Extension tells you when you've met all the requirements for a particular project, [HTML validators](https://validator.w3.org/) analyze your website and verify that you're writing valid HTML.
