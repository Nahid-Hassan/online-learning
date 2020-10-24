# Troubleshooting and Debugging Techniques

Google IT Automation with Python Course#4

## Welcome To The Course

Welcome to the course!
In this course, you’ll learn how to debug and troubleshoot a wide range of technical problems, both in your code and in someone elses code.

### Course prerequisites

This course requires some familiarity with basic IT concepts:

* __Operating systems__: `file systems`, `processes`, `log files`
* __Computer hardware__: `CPU`, `RAM`, `disk`, `graphic`, and `network cards`
* __Basic networking__: `network connections` and `network bandwidth`

The example scripts and programs in this course are written in `Python`, so you’ll need an understanding of this programming language, too.

🔗 [Stack Overflow Troubleshoot][stackoverflow]

### Introduction to Debugging

Whether it's an application crashing, a hardware issue, or network outage, as IT specialists, we tend to run into problems that need solving pretty regularly. When facing these issues, we need to make sure that people affected by the problem can get back to doing their jobs as fast as possible. We also have to plan for how to prevent against the same problems from happening again in the future. In this module, we'll learn some essential debugging techniques. 

We'll keep applying them throughout the course as we explore different issues that can affect us or the users we're supporting in different ways. As with any other skills that you've learned throughout this program, the best way to get good at something is practice. So at the end of the module, you'll have the opportunity to apply these techniques and try solving a technical issue yourself on a virtual machine running Linux.

### What is Debugging

**Troubleshooting**:

![Troubleshoot][troubleshoot-definition]

**Debugging**:

![Debug-Definition][debug-definition]

We sometimes use troubleshooting and debugging interchangeably. But generally, we say troubleshooting when we're fixing problems in the system running the application, and debugging when we're fixing the bugs in the actual code of the application. 

There are lots of tools that we can use to get more information about the system and what the programs in our system are doing. Tools like, `tcpdump` and `Wireshark` can show us `ongoing network connections`, and help us analyze the traffic going over our cables.

Tools like `ps, top, or free` can show us the number and types of resources used in the system. We can use a tool like `strace` to look at the system calls made by a program, or `ltrace` to look at the library calls made by the software.

**Debuggers**:

![Debug][debuggers]

> Both troubleshooting and debugging is an art

### Problem Solving Skills

There's a wide range of different technical problems that you might face as an IT specialist or systems administrator. But fortunately, there's a set of steps that you can usually take to solve almost any technical problem.

* The `first step is getting information`. This means gathering as much information as we need about the current state of things, what the issue is, when it happens, and what the consequences are, for example. To get this information, we can use any existing documentation that might help. This can be `internal documentation`, `manual pages`, or `even questions asked on the Internet`. 

One super important resource to solve a problem is the `reproduction case`, `which is a clear description of how and when the problem appears`.

* The `second step is finding the root cause of the problem`. `This is usually the most difficult step`. Throughout this course, we'll discuss a lot of possibilities on how to get there. But the key here is to get to the bottom of what's going on, what triggered the problem, and how we can change that.
  
* The `final step is performing the necessary remediation`. Depending on the problem, this might include an immediate remediation to get the system back to health, and then a medium or long-term remediation to avoid the problem in the future. While these are three basic steps of problem-solving, they don't always happen sequentially. It's pretty common that while trying to find the root cause, we discover that we need even more info about the current state. So we gather more information until we find the answer we're looking for, or we could understand the problem just enough to create a workaround that lets our users get back to work quickly, but we'd still need more time to get to the root cause and prevent the problem from happening again. Preventing the problem from occurring can sometimes feel like a hassle, but it can actually save us and our users a lot of valuable time. This way we avoid having to solve the same problem over and over again.
  
* `Throughout the whole process, it's important that we document what we do`. We should note down the info that we get, the different things we tested to try, and figure out the root cause. Finally, the steps we took to fix the issue. This documentation might prove invaluable next time a similar issue pops up.

* Imagine a user asks you for your help because their computer is unexpectedly shutting down. Computers shouldn't shut down on their own, but the problem could be a hardware issue, a software issue, or even a configuration issue. So the first thing to do is to get more information. You'll want to know things like when it happened, what the user was doing when it happened, and how regularly it's happening. You'll also want to look at the computer logs to check if there are any interesting errors. If any aren't totally clear, you can look them up on the Internet to see what they mean. In our example, safe on a line in the logs that says the temperature threshold was exceeded and so the computer shutdown. That's useful information, you know why the computer shut down but you don't know why it overheated, so you'll need to keep investigating. After not finding anything else interesting in the logs, you decide to check if it's a hardware issue. When you open up the computer, you find that the fan that's supposed to cool down the CPU is full of dirt, and so it isn't spinning properly. That's the root cause of the problem. Now, the short-term remediation is to clean up the fan so that it can spin again and the computer doesn't overheat. But what's the long-term remediation? In this case, it would be deploying monitoring on the computers to make sure you get notified early when they're overheating. Long-term remediation would also include checking if you can reduce the amount of dust in the air so that there's less chance of this happening again.

### Silently Crashing Application

#### `strace` - trace system calls and signals

```sh
> ls
practice.py

> python3 practice.py
-- Assume practice.py has some internal error --

> strace python3 practice.py

execve("/usr/bin/python3", ["python3", "practice.py"], 0x7fff670025e8 /* 61 vars */) = 0
brk(NULL)                               = 0x1dc8000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffc796d5850) = -1 EINVAL (Invalid argument)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)

-----------------------------------So many system calls------------------------------------

read(3, "def hello(name):\n    print(\"hi \""..., 8192) = 80
read(3, "", 8192)                       = 0
close(3)                                = 0
write(2, "    hello()\n", 12    hello()
)           = 12
write(2, "TypeError: hello() missing 1 req"..., 66TypeError: hello() missing 1 required positional argument: 'name'
) = 66
sigaltstack(NULL, {ss_sp=0x1e0e5c0, ss_flags=0, ss_size=16384}) = 0
sigaltstack({ss_sp=NULL, ss_flags=SS_DISABLE, ss_size=0}, NULL) = 0
exit_group(1)                           = ?
+++ exited with 1 +++

> strace -o failure.strace python3 practice.py
> less failure.strace

read(3, "def hello(name):\n    print(\"hi \""..., 8192) = 80
read(3, "", 8192)                       = 0
close(3)                                = 0
write(2, "    hello()\n", 12    hello()


:/hello
Enter..... and find the errors.
```

`strace` command shows us all the `system calls` are program made. `System calls` are the calls that the programs running on our computer make to the running `kernel`. There are loads of different system calls and depending on what we're trying to debug.

#### Practice Quiz: Introduction to Debugging

__Question 1__:

What is part of the final step when problem solving?

* [ ] Documentation
* [X] Long-term remediation
* [ ] Finding the root cause
* [ ] Gathering information

__Question 2__:

Which tool can you use when debugging to look at library calls made by the software?

* [ ] top
* [ ] strace
* [ ] tcpdump
* [X] ltrace

__Question 3__:

What is the first step of problem solving?

* [ ] Prevention
* [X] Gathering information
* [ ] Long-term remediation
* [ ] Finding the root cause

__Question 4__:

What software tools are used to analyze network traffic to isolate problems? (Check all that apply)

* [X] tcpdump
* [X] wireshark
* [ ] strace
* [ ] top

__Question 5__:

The strace (in Linux) tool allows us to see all of the _____ our program has made.

* [ ] Network traffic
* [ ] Disk writes
* [X] System calls
* [ ] Connection requests

<!-- urls and file paths -->
[stackoverflow]: https://stackoverflow.com/search?q=troubleshoot
[troubleshoot-definition]: ./images/troubleshoot-definition.png
[debug-definition]: ./images/debug-definition.png
[debuggers]: ./images/debuggers.png