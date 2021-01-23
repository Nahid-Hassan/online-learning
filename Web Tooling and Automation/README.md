# Web tools and Automation

## Table of Contents

- [Web tools and Automation](#web-tools-and-automation)
  - [Table of Contents](#table-of-contents)
    - [Productive Editing](#productive-editing)
      - [From Notepad to IDE](#from-notepad-to-ide)
      - [Setup Your Editor](#setup-your-editor)
      - [Built in Editor Magic](#built-in-editor-magic)
      - [Figure out Shortcuts](#figure-out-shortcuts)
      - [Extending your Editor](#extending-your-editor)

### Productive Editing

Setup your development environment.

#### From Notepad to IDE

`IDE`: Integrated Development Environment

Commonly `IDE` features:

- Editing
- Debugging
- Building
- Compiling
- Optimizing

#### Setup Your Editor

- Sublime
- Atom
- VS Code

```console
root@admin: ~$ sudo apt update
root@admin: ~$ sudo apt install dirmngr gnupg apt-transport-https ca-certificates software-properties-common
root@admin: ~$ curl -fsSL https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
root@admin: ~$ sudo add-apt-repository "deb https://download.sublimetext.com/ apt/stable/"
root@admin: ~$ sudo apt install sublime-text
```

#### Built in Editor Magic

In the first couple of days of using a new editor, try out lots of build-in shortcuts and features, even if they seem overkill. Try them all out and observe yourself. Which shortcuts stick, which do you have to force yourself to use?

#### Figure out Shortcuts

The editor you choose.

#### Extending your Editor

Extending Sublime Text
Below are the links for the previous video. Recall that you can open the Sublime Text console with View > Show Console or Ctrl + `.

Package Control, the Sublime Text package manager

- Emmet home page
- Emmet on Package Control
- SideBarEnhancements on Package Control
- ColorPicker on Package Control
- ColorHighlighter on Package Control
- Extending Atom

Out of the box, Atom comes with the ability to install and manage packages. Head over to Atom > Preferences > Install on Mac (or File > Settings > Install on Windows) to search for packages. Alternatively, you can use the shortcut ⌘ + , on Mac (or Ctrl + , on Windows) to open up the Settings menu, and just select the Install tab.

There, you'll be able to search the official registry for Atom packages, such as Emmet and Color Picker.

Extending Visual Studio Code
VS Code extensions allow developers to add languages, debuggers, and tools to support the development process as well. To check it out, click on the Extensions icon on the sidebar of VS Code. Alternatively, you can use the command ⌘ + ⇧ + X on Mac (orCtrl + Shift + X on Windows).

Regardless of which method you choose, you'll be shown a collection of popular VS Code extensions in the VS Code Marketplace.
