## Essential Directory Navigation Commands

## pwd (Print Working Directory)

> [!question] What does the pwd command do?
>
> > [!success]- Answer
> > The pwd command displays the complete path of your current working directory.

Syntax: pwd [OPTIONS]

Usage:

- pwd → Shows current directory path
- pwd -L → Shows symbolic path (resolves symbolic links)
- pwd -P → Shows actual path without resolving symbolic links

The pwd command prints the path starting from the root directory, with directories separated by forward slashes.

## ls (List Directory Contents)

> [!question] What is the primary function of the ls command?
>
> > [!success]- Answer
> > The ls command lists files and directories in the current or specified directory.

Syntax: ls [options] [file/directory]

Common Options:

- ls → Basic listing in alphabetical order
- ls -l → Long format with detailed information (permissions, ownership, size)
- ls -a → Show all files including hidden files (starting with .)
- ls -la → Combines long format with hidden files
- ls -t → Sort by modification time
- ls -r → Reverse the listing order
- ls -S → Sort by file size
- ls -h → Human-readable file sizes (1K, 234M, 2G)

## cd (Change Directory)

> [!question] How do you navigate to your home directory using cd?
>
> > [!success]- Answer
> > Simply type cd or cd ~ to go to your home directory.

Syntax: cd [directory]

Usage Examples:

- cd → Go to home directory
- cd Documents → Move to Documents subdirectory
- cd /path/to/directory → Move using absolute path
- cd .. → Go up one directory level
- cd ../.. → Go up two directory levels
- cd - → Return to previous directory
- cd ~ → Go to home directory

You can combine with ls: cd Documents && ls to change directory and list contents simultaneously.

## clear (Clear Terminal Screen)

> [!question] What are alternative methods to clear the terminal screen?
>
> > [!success]- Answer
> > You can use Ctrl + L as a keyboard shortcut or the reset command to clear the screen and reset terminal settings.

Function: Clears the terminal screen of all previous commands and output

Syntax: clear [options]

Usage:

- clear → Standard screen clearing
- clear -x → Clear screen but keep scrollback buffer

