---
layout: page
title: Setup
root: .
---

There are several pieces of software you will wish to install before the
workshop. Though installation help will be provided at the workshop, we
recommend that these tools are installed (or at least downloaded) beforehand.

<!---
1. [A terminal application or command-line interface](
   #where-to-type-commands-how-to-open-a-new-shell)
2. [A Secure Shell application](#ssh-for-secure-connections)
--->

> ## Bash and SSH
>
> This lesson requires a terminal application (`bash`, `zsh`, or others) with
> the ability to securely connect to a remote machine (`ssh`).
{: .prereq}

## Where to Type Commands: How to Open a New Shell

The shell is a program that enables us to send commands to the computer and
receive output. It is also referred to as the terminal or command line.

Some computers include a default Unix Shell program. The steps below describe
some methods for identifying and opening a Unix Shell program if you already
have one installed. There are also options for identifying and downloading a
Unix Shell program, a Linux/UNIX emulator, or a program to access a Unix Shell
on a server.


### Windows

Computers with Windows operating systems do not automatically have a Unix Shell
program installed. In this lesson, we encourage you to use an emulator included
in Git for Windows, which gives you access to both Bash shell commands and Git.
If you have attended a Software Carpentry workshop session, it is likely you
have already received instructions on how to install Git for Windows.

Once installed, you can open a terminal by running the program Git Bash from
the Windows start menu.


#### Shell Programs for Windows

* [Git for Windows][git4win] -- *Recommended*
* [Windows Subsystem for Linux][ms-wsl] -- advanced option for Windows 10


> ## Alternatives to Git for Windows
>
> Other solutions are available for running Bash commands on Windows. There is
> now a Bash shell command-line tool available for Windows 10. Additionally,
> you can run Bash commands on a remote computer or server that already has a
> Unix Shell, from your Windows machine. This can usually be done through a
> Secure Shell (SSH) client. One such client available for free for Windows
> computers is PuTTY. See the reference below for information on installing and
> using PuTTY, using the Windows 10 command-line tool, or installing and using
> a Unix/Linux emulator.
>
> For advanced users, you may choose one of the following alternatives:
>
> * Install the [Windows Subsystem for Linux][ms-wsl]
> * Use the Windows [PowerShell][ms-shell]
> * Read up on [Using a Unix/Linux emulator][unix-emulator] (Cygwin) or Secure
>   Shell (SSH) client (PuTTY)
>
> > ## Warning
> >
> > Commands in the Windows Subsystem for Linux (WSL), PowerShell, or Cygwin
> > may differ slightly from those shown in the lesson or presented in the
> > workshop. Please ask if you encounter such a mismatch -- you're
> > probably not alone.
> {: .challenge}
{: .discussion}

### macOS

On macOS, the default Unix Shell is accessible by running the Terminal program
from the `/Application/Utilities` folder in Finder.

To open Terminal, try one or both of the following:

* In Finder, select the Go menu, then select Utilities. Locate Terminal in the
  Utilities folder and open it.
* Use the Mac ‘Spotlight’ computer search function. Search for: `Terminal` and
  press <kbd>Return</kbd>.

For an introduction, see [How to Use Terminal on a Mac][mac-terminal].

### Linux

On most versions of Linux, the default Unix Shell is accessible by running the
[(Gnome) Terminal](https://help.gnome.org/users/gnome-terminal/stable/) or
[(KDE) Konsole](https://konsole.kde.org/) or
[xterm](https://en.wikipedia.org/wiki/Xterm), which can be found via the
applications menu or the search bar.


### Special Cases

If none of the options above address your circumstances, try an online search
for: `Unix shell [your operating system]`.


## SSH client for secure connections

All students should have an SSH client installed. SSH is a tool that allows us
to connect to and use a remote computer as our own.


### Windows 

Git for Windows comes with SSH preinstalled: you do not have to do anything.

### SSH for macOS

macOS comes with SSH pre-installed: you do not have to do anything.

### SSH for Linux

Linux comes with SSH and X window support preinstalled: you do not have to do
anything.

> ## GUI Support for Windows
>
> If you know that the software you will be running on the cluster requires a
> graphical user interface (a GUI window needs to open for the application to
> run properly), please install [MobaXterm](https://mobaxterm.mobatek.net) Home
> Edition.
{: .discussion}

> ## GUI Support for macOS
>
> If you know that the software you will be running requires a graphical user
> interface, please install [XQuartz](https://www.xquartz.org).
{: .discussion}


## Account on Cirrus

Please sign up for your account on the EPCC HPC machine, Cirrus, which will be available to
you for the duration of the course and for a short while afterwards, to allow you to
complete the practical exercises and put some of what you have learned into practice.


### Sign up for a SAFE account


First you need to register for a [SAFE](https://safe.epcc.ed.ac.uk) account - SAFE is an online administration system.  Please ensure you use the same email address that you used to register for the course. If you have an existing SAFE account for ARCHER or Tier2 systems, then use your existing SAFE login credentials to log in, rather than creating a new account. Otherwise [register for an account](https://safe.epcc.ed.ac.uk/signup.jsp).

See [https://epcced.github.io/safe-docs/safe-for-users/#register](https://epcced.github.io/safe-docs/safe-for-users/#register)  for further help.


### Generate an SSH key pair

In addition to your password, you will need an SSH key pair to access Cirrus. You will need to generate this on your local machine and upload the public key part to your SAFE account. This will allow secure access to Cirrus from your local machine without the need to setup ssh keys directly on the machine.

[Set up a password protected ssh key pair](https://cirrus.readthedocs.io/en/main/user-guide/connecting.html)


### Sign up for an account on Cirrus through SAFE

Then [request your machine account on Cirrus](https://epcced.github.io/safe-docs/safe-for-users/#your-user-account-on-the-service-machine) adding your ssh public key when prompted.

The project code for this course is **tc036** on Cirrus

You will have to wait for the course organiser to accept your request to register. When this has happened, your account will be created on Cirrus. Once this has been done, you will receive an email once your account request has been approved and the account has been set up. 

_If you have not received an email but believe that your account should have been activated, check your account status in SAFE which will also show when the account has been activated._ 

You can then [retrieve the initial password](https://epcced.github.io/safe-docs/safe-for-users/#getpass) and get [logged on](https://cirrus.readthedocs.io/en/main/user-guide/connecting.html#ssh-clients).


### Logging in for the first time

Note that when you first log on you will be immediately prompted to change your initial password please see [documentation](https://cirrus.readthedocs.io/en/main/user-guide/connecting.html#changing-passwords) for guidance.


### Problems?

If you have any issues, please contact the Cirrus service desk, support@cirrus.ac.uk, and please mention that you are a student on the N8CIR Introduction to High Performance Computing course on 14th March 2023 and are using the Training Project tc036 on Cirrus





<!-- links -->
[git4win]: https://gitforwindows.org/
[mac-terminal]: https://www.macworld.co.uk/feature/mac-software/how-use-terminal-on-mac-3608274/
[ms-wsl]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
[ms-shell]: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core?view=powershell-7
[mobax-gen]: https://mobaxterm.mobatek.net/documentation.html
[unix-emulator]: https://faculty.smu.edu/reynolds/unixtut/windows.html
[wsl]: https://docs.microsoft.com/en-us/windows/wsl/install-win10
