# Reflections 20251002

## CLI workshop

### Commands I'm not using yet
    ls -la is a list of just files
    cd on its own takes us to the top level directory i.e. ~ 
    ctr r and you can search venv_ and more ctr r will cycle through older commands
    tab and tab gives a dropdown and you can tab through the options under the -> 
    man gives you the help files
    

### Cursor Movement

Firstly iterm has different movement rules, but you can make it feel like every other app. >iterm>settings>profiles>keys then change left and right ⌘ from normal to Esc+ other wise ⌘ + → changes iterm windows

    Control + A	Beginning of line	Moves the cursor to the very start of the line. Super fast.

    Control + E	End of line	The counterpart to Ctrl+A. Moves the cursor to the very end.

    Option (⌥) + ←	Back one word	Jumps the cursor to the beginning of the previous word.

    Option (⌥) + →	Forward one word	Jumps the cursor to the beginning of the next word.

### Editing & Deleting Text
    Control + F	Forward one character	Same as the → arrow key. ("F" for Forward)

    Control + B	Back one character	Same as the ← arrow key. ("B" for Backward)

    Control + W	Delete previous word	Deletes the entire word behind the cursor. Incredibly useful.

    Control + K	Delete to end of line	Deletes ("Kills") everything from the cursor to the end of the line.

    Control + U	Delete entire line	Deletes everything from the cursor to the beginning of the line.

    Control + D	Delete character forward	Deletes the character under the cursor (like a standard Delete key).

    Control + H	Delete character back	Same as the Backspace key.

    Control + T	Transpose characters	Swaps the two characters immediately before the cursor. Great for typos.

    ↑ / ↓ Arrow	Previous/Next Command	The basic way to cycle through your command history.

### Command History Navigation
    Control + R	Reverse Search History	This is a superpower. Press it, then start typing any part of an old command. The most recent match will appear. Press Ctrl+R again to cycle through older matches. Press Enter to run it or an arrow key to edit it.

    (type) + ↑ Arrow	Zsh History Search	Type the first few letters of a command (e.g., git) and then press the ↑ arrow. Zsh will only cycle through commands in your history that start with git.

    !!	Run last command	Type !! and press Enter to execute the previous command again. Most useful with sudo !! to re-run a failed command with admin privileges.

    Control + L	Clear Screen	Clears the visible screen and puts your current line at the top. It doesn't delete your scrollback history.

    Command (⌘) + K	Clear Scrollback	This is an iTerm2-specific command that completely clears the terminal window, including all the history you can scroll back to.

    Control + C	Interrupt Process	Sends an interrupt signal to the currently running program to stop it. This is your "get me out of here" command.

    Control + Z	Suspend Process	Pauses the current process and sends it to the background. You can bring it back with the fg (foreground) command.

## REPL
    You can do python in the terminal.

### Tips
    python3 -i your_file.py will allow you to use user defined functions from that file. But its a snapshot so if you change the file you wont have that change in the REPL 
    exit() or ctrl d also exits
    " or ' dont matter. but you must be consistent. 
    "_" The REPL automatically stores the result of the last evaluated expression in a special variable _.
    help() enters interactive help mode 
    help(object)
    type(variable): Tells you what type of object something is.
    dir(variable): Shows you a list of all the methods and attributes available on that object.

    *Strings*
    you can just type the name of a string and it will return the string with "your string". alternatively print("string") will give string - i.e. no quotes
    calling a method doesnt change the original string it just gives you a new output. 
    same tab command gives you auto complete.
    >>><string>. + tab and tab again pulls up a list of all the methods!!! <string>.a gives you all the methods starting with a
    if you press enter at the wrong time you'll get >>>h.strip(
    ... and all you'll need to do is add the ) after the ... and hit enter.
    you can chain .methods i.e. .strip().upper() gives an uppercase string with no spaces at start and finish. The order may matter depending on what we're doing - order is left to right. 

    *Lists*
    Lists (& arrays) start at 0. 
    l = [1,2,3,4,]
    sorted(1)

### iPython is better...
    pip install ipython

