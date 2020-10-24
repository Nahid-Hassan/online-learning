# Responsive Web Design Fundamentals

[Course Intro][intro]

## Lesson 1: Why Responsive

> Responsive Web Design(RWD) is a Art not a Science.

[Want to test with different browsers in the cloud? Try [BrowserStack][bs].

### Accessing Chrome's Developer Tools

To access Chrome's Developer Tools, using the following shortcuts (depending on which operating system you are using):

#### Mac

`⌘` + `⌥` + `J`

#### Windows

`Ctrl` + `Shift` + `J`

(Google has replaced the shortcut from in the video with the shortcut above)

For a comprehensive guide of Chrome's shortcuts, check out this [link](https://support.google.com/chrome/answer/157179?hl=en).

#### Toggling the Device Toolbar (Emulator)

Once you have Dev Tools opened in Chrome, look at the top left-hand corner of the new window that opens. Go ahead and click on the icon that looks like a phone and tablet (as seen below, directly above the word "Toggle"):
![image](https://video.udacity-data.com/topher/2018/October/5bbd3f27_screen-shot-2018-10-09-at-4.39.33-pm/screen-shot-2018-10-09-at-4.39.33-pm.png)

Alternatively, you can use the shortcut `⌘` + `⇧` + `M` (or `Ctrl` + `Shift` + `M` on Windows) to toggle the Device Toolbar as well. Note that this shortcut only works when Dev Tools is already open.

After toggling the Device Toolbar, your screen should look something like this:
![image](https://video.udacity-data.com/topher/2018/October/5bbd3f85_screen-shot-2018-10-09-at-4.48.56-pm/screen-shot-2018-10-09-at-4.48.56-pm.png)

Feel free to use the dropdown menu to emulate a device of your choice!
![image](https://video.udacity-data.com/topher/2018/October/5bbd3fc3_screen-shot-2018-10-09-at-4.54.00-pm/screen-shot-2018-10-09-at-4.54.00-pm.png)

For additional options, such as setting the device pixel ratio (DPR), you can always click on the "more options" button (i.e., the three dots/ellipsis icon) on the top right-hand corner of the page view:
![image](https://video.udacity-data.com/topher/2018/October/5bbd9e7d_screen-shot-2018-10-09-at-11.35.42-pm/screen-shot-2018-10-09-at-11.35.42-pm.png)

### Remote Debugging: Setup for Mobile Device

[Download Chrome Canary](https://www.google.com/chrome/canary/) (it won't affect your existing Chrome installation)

[Remote debugging Android devices with Chrome](https://developers.google.com/web/tools/chrome-devtools/debug/remote-debugging/remote-debugging?hl=en)

#### What is Chrome Canary and why should I use it

Chrome Canary is the developer version of Chrome. It looks and acts like the regular Chrome browser, but it includes new and experimental features that haven't been released yet. We recommend analyzing websites with Canary to take advantage of the latest tech. However, be warned that Canary isn't guaranteed to be stable, so expect crashes and occasional bugs.

#### Do I have to test on mobile

For the purposes of this course, no. But testing your websites on mobile is a best practice, and if you have the means to do so we highly recommend it.

#### Mobile Tools for iOS

[iOS WebKit Debug Proxy](https://github.com/google/ios-webkit-debug-proxy)

Please note that in the community, there is a discussion continuing about ios-webkit-debug-proxy. Depending on your version of canary, if you're using it, it might take a lot of time and some students suggest trying Safari Dev Tools and point to links like this:

Visit: https://www.smashingmagazine.com/2014/09/testing-mobile-emulators-simulators-remote-debugging/

Remember you can run in simulator mode in Chrome Dev Tools.

## Lesson 2: Starting Small

### Defining the viewport

HTML5 introduced a method to let web designers take control over the viewport, through the `<meta>` tag.

You should include the following `<meta>` viewport element in all your web pages:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

This gives the browser instructions on how to control the page's dimensions and scaling.

The `width=device-width` part sets the width of the page to follow the screen-width of the device (which will vary depending on the device).

The `initial-scale=1.0` part sets the initial zoom level when the page is first loaded by the browser.

#### HTML <meta> tag

```html
<head>
  <meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML, CSS, JavaScript">
  <meta name="author" content="John Doe">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

The `<meta>` tag defines metadata about an HTML document. Metadata is data (information) about data.

`<meta>` tags always go inside the `<head>` element, and are typically used to specify character set, page description, keywords, author of the document, and viewport settings.

Metadata will not be displayed on the page, but is machine parsable.

Metadata is used by browsers (how to display content or reload page), search engines (keywords), and other web services.

### Quiz

You look up the tech specs for the screen of a mobile device and find it has a resolution of 1920x1080 pixels . Which kind of pixels are the tech specs referencing?

* [ ] Device Independent Pixels
* [ ] CSS Pixels
* [X] Hardware Pixels

### Calculating DPR

![image][dpr]

#### QUIZ QUESTION

Each cell in the blue grid represents 1 hardware pixel (i.e., 16 total per diagram), and the entire orange-shaded area in each diagram represents 1 dip.

Which of the above diagrams demonstrates a display with a device pixel ratio of 2?

* [ ] A
* [ ] B
* [X] C
* [ ] D

### Quiz Question

Why would the same websites look different on screens of identical resolutions?

`Solution`

* The device pixels ratio differs different device
* The viewport wasn't set
  
### Calculating Viewport Width

`Question`: Calculate the width (in dips) of the viewport for all of the devices below. Entering in just the number is fine!

A phone that is 640px wide, DPR = 2

`Solution`: 320

`Question`: A phablet that is 780px wide, DPR = 2.5

`Solution`: 312

### Setting View Port

```html
<!-- Inside the <head> -- </head> tag put this code-->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

> #### Note: Don't forget to set the viewport

### Large fixed width-element

`Large image  problem for small device`

`max-width` on elements

```css
/* Set max-width on elements */
img {
  max-width: 100%;
}

/* Recommended */
img, embed, object, video {
  max-width: 100%;
}
```

### Which Element Will Respond

Which of the following four elements could look great on any device? If you're not sure, feel free to open it up in a browser and see what happens. Make sure you test on several different devices!

`Question`:

```css
<img id="owl">
#owl {
  width: 640px;
  max-width: 100%;
}
```

`Answer`: Responsive, because max-width override width.

`Question`:

```css
<img class="logo">
.logo {
  width: 125px;
}
```

`Answer`: Responsive, because 125 px is too small.

`Question`:

```css
<div class="box"></div>
.box {
  width: 350px;
}
```

`Answer`: Not Responsive, because there is exits less 250 pixels device.

`Question`:

```css
<div class="city"></div>
.city {
  width: 100%;
}
```

`Answer`: Responsive, because set width 100%

### Tab Target Size

Visit: <https://www.youtube.com/watch?v=sFzdU8Z1Wd8&feature=youtu.be&ab_channel=Udacity>

`Minimum Button Size`: 40px

### Tab Target

Consider the following:

```css
nav a, button {

}
```

Which CSS styles would you include inside the curly braces so that Cameron won't be tortured by tiny, impossible-to-hit buttons?

* [X] `min-height: 48px`;
* [ ] `height: 48px`;
* [X] `min-width: 48px`;
* [ ] `size: 48px`;

#### Note: Start Small

### Responsive Web Design Solution

* [Project Solution](https://www.udacity.com/api/nodes/3471369785/supplemental_media/rwdf-l2-solutionzip/download?_ga=1.242116037.672083044.1467344711)

  * This solution is also available in the workspace from Project Part 1 (via the Solution folder)

* [pattern-mostly-fluid-quiz-blankcss.html](https://s3-us-west-2.amazonaws.com/gae-supplemental-media/pattern-mostly-fluid-quiz-blankcsshtml/pattern-mostly-fluid-quiz-blankcss.html)


  * This can help you to use flexbox to make your page responsive and learn how to use the viewport property
  * Use the Developers tools to find the Elements and the css properties.

Note that these files are also available in the `Supporting Materials` at the very bottom of this page.

#### 💡 CSS `inherit` keyword 💡

As mentioned in the video above, the solution in `main.css` uses the following code:

```css
.top-news__item a {
  text-decoration: none;
  color: #666;
  padding: 1.5em inherit;
}
```

Let's check out what's happening in the fourth line of code.

Here, we give some space to that element between its content and border via the `padding` property. The first value sets the top and bottom padding to `1.5em`; that is, 1.5 times the font size of the current element. As such, we are dealing with a relative unit, rather than an absolute unit (e.g., pixels, centimeters, etc.).

While the first value given to `padding` takes care of the top and bottom padding, the second value sets the left and right padding. By using the CSS keyword `inherit`, we are saying we want the padding property to inherit its value from its container (i.e., its parent element).

Feel free to check out [inherit on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/inherit) for more examples!

<!-- link/urls and files path -->
[intro]: https://youtu.be/7DJLa4owtIU
[bs]: https://www.browserstack.com/
[dpr]: https://video.udacity-data.com/topher/2018/September/5bae86f9_screen-shot-2018-09-28-at-12.53.00-pm/screen-shot-2018-09-28-at-12.53.00-pm.png