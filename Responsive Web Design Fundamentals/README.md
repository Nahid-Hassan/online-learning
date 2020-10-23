# Responsive Web Design Fundamentals
[Course Intro][intro]


# Lesson 1: Why Responsive?
>Responsive Web Design(RWD) is a Art not a Science.

[Want to test with different browsers in the cloud? Try [BrowserStack][bs].


### Accessing Chrome's Developer Tools
To access Chrome's Developer Tools, using the following shortcuts (depending on which operating system you are using):

#### Mac:

`⌘` + `⌥` + `J`

#### Windows:

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

#### What is Chrome Canary and why should I use it?
Chrome Canary is the developer version of Chrome. It looks and acts like the regular Chrome browser, but it includes new and experimental features that haven't been released yet. We recommend analyzing websites with Canary to take advantage of the latest tech. However, be warned that Canary isn't guaranteed to be stable, so expect crashes and occasional bugs.

#### Do I have to test on mobile?
For the purposes of this course, no. But testing your websites on mobile is a best practice, and if you have the means to do so we highly recommend it.

#### Mobile Tools for iOS
[iOS WebKit Debug Proxy](https://github.com/google/ios-webkit-debug-proxy)

Please note that in the community, there is a discussion continuing about ios-webkit-debug-proxy. Depending on your version of canary, if you're using it, it might take a lot of time and some students suggest trying Safari Dev Tools and point to links like this:

Visit: https://www.smashingmagazine.com/2014/09/testing-mobile-emulators-simulators-remote-debugging/

Remember you can run in simulator mode in Chrome Dev Tools.


# Lesson 2: Starting Small
### Defining the viewport






<!-- link/urls and files path -->
[intro]: https://youtu.be/7DJLa4owtIU
[bs]: https://www.browserstack.com/