# Key Bindings for ash

The following is a list of key bindings for **ash**. Please note that these bindings may change as the project develops.

### Global key combinations

These key combinations can be used even if no editor is currently active.

<kbd>Ctrl</kbd> + <kbd>Q</kbd> &nbsp;&nbsp;Closes the active window

<kbd>Ctrl</kbd> + <kbd>@</kbd> &nbsp;&nbsp;Force-quits the application, discarding all changes

<kbd>Tab</kbd> &nbsp;&nbsp;Moves focus to the next widget in the active dialog-box (if any)

<kbd>Shift</kbd> + <kbd>Tab</kbd> &nbsp;&nbsp;Moves focus to the previous widget in the active dialog-box

<kbd>Ctrl</kbd> + <kbd>&#8592;</kbd> <kbd>&#8593;</kbd> <kbd>&#8594;</kbd> <kbd>&#8595;</kbd> &nbsp;&nbsp;Moves the active dialog-box (if any) around the screen

<kbd>Ctrl</kbd> + <kbd>L</kbd> &nbsp;&nbsp;Changes the layout of splits

<kbd>Ctrl</kbd> + <kbd>N</kbd> &nbsp;&nbsp;Opens a new buffer

<kbd>Ctrl</kbd> + <kbd>O</kbd> &nbsp;&nbsp;Open a file

<kbd>Ctrl</kbd> + <kbd>E</kbd> &nbsp;&nbsp;Opens project explorer (if directory has been opened)

<kbd>F1</kbd> - <kbd>F6</kbd> &nbsp;&nbsp;&nbsp;&nbsp;Activates the corresponding editor (if exists in the current layout)

<kbd>F12</kbd>&nbsp;&nbsp;&nbsp;&nbsp;Shows this list of key-bindings


### Editor commands

These key combinations work only if an editor is currently active.

<kbd>&#8592;</kbd> <kbd>&#8593;</kbd> <kbd>&#8594;</kbd> <kbd>&#8595;</kbd> &nbsp;&nbsp;Moves the cursor in the document one character/line at a time

<kbd>Ctrl</kbd> + <kbd>&#8592;</kbd> <kbd>&#8594;</kbd> &nbsp;&nbsp;Moves the cursor one word at a time

<kbd>PgUp</kbd> <kbd>PgDown</kbd> &nbsp;&nbsp;Moves the cursor in the document one screenful at a time

<kbd>Home</kbd> <kbd>End</kbd> &nbsp;&nbsp;Moves the cursor to the beginning/end of the current line

<kbd>Ctrl</kbd> + <kbd>Home</kbd> <kbd>End</kbd> &nbsp;&nbsp;Moves the cursor to the beginning/end of the current document

<kbd>Tab</kbd> &nbsp;&nbsp;When some text is selected, it increases the indent of the selection

<kbd>Shift</kbd> + <kbd>Tab</kbd> &nbsp;&nbsp;When some text is selected, it decreases the indent of the selection if possible

<kbd>Shift</kbd> + <kbd>Home</kbd> <kbd>End</kbd> &nbsp;&nbsp;Selects text up to the beginning/end of the current line

<kbd>Shift</kbd> + <kbd>&#8592;</kbd> <kbd>&#8593;</kbd> <kbd>&#8594;</kbd> <kbd>&#8595;</kbd> &nbsp;&nbsp;Selects text one character at a time

<kbd>Shift</kbd> + <kbd>PgUp</kbd> <kbd>PgDown</kbd> &nbsp;&nbsp;Selects one screenful at a time

<kbd>Ctrl</kbd> + <kbd>A</kbd> &nbsp;&nbsp;Select all

<kbd>Ctrl</kbd> + <kbd>C</kbd> &nbsp;&nbsp;Copy

<kbd>Ctrl</kbd> + <kbd>X</kbd> &nbsp;&nbsp;Cut

<kbd>Ctrl</kbd> + <kbd>V</kbd> &nbsp;&nbsp;Paste

<kbd>Backspace</kbd>&nbsp;&nbsp;Deletes the character/selected-text before the cursor

<kbd>Del</kbd> &nbsp;&nbsp;Deletes the selected-text or, character at the cursor position

<kbd>Ctrl</kbd> + <kbd>S</kbd> &nbsp;&nbsp;Saves the current file

<kbd>Ctrl</kbd> + <kbd>P</kbd> &nbsp;&nbsp;Opens the preferences dialog-box

<kbd>Ctrl</kbd> + <kbd>G</kbd> &nbsp;&nbsp;Go to a given line/column

<kbd>Ctrl</kbd> + <kbd>Z</kbd> &nbsp;&nbsp;Undo

<kbd>Ctrl</kbd> + <kbd>Y</kbd> &nbsp;&nbsp;Redo

<kbd>Ctrl</kbd> + <kbd>F</kbd> &nbsp;&nbsp;Find

<kbd>Ctrl</kbd> + <kbd>H</kbd> &nbsp;&nbsp;Replace

### Commands for find and replace operations

These key combinations work when the Find/Replace dialog box is active:

<kbd>Enter</kbd> &nbsp;&nbsp;Find next match

<kbd>F7</kbd> &nbsp;&nbsp;Find previous match

<kbd>F8</kbd> &nbsp;&nbsp;Replace the current match

<kbd>Ctrl</kbd> + <kbd>F8</kbd> &nbsp;&nbsp;Replace all matches

### Commands for Project Explorer

These key combinations work when the Project Explorer dialog-box is active:

<kbd>Ctrl</kbd> + <kbd>R</kbd> &nbsp;&nbsp;Refresh file tree

<kbd>Ctrl</kbd> + <kbd>N</kbd> &nbsp;&nbsp;Create a new file under the selected directory

<kbd>Ctrl</kbd> + <kbd>D</kbd> &nbsp;&nbsp;Create a new directory under the selected directory

<kbd>+</kbd> &nbsp;&nbsp;Collapse the current selected directory

<kbd>-</kbd> &nbsp;&nbsp;Expand the current selected directory

## Other features

**ash** also provides certain shortcuts for helping in editing code. It has support for auto-indentation when the previous line is indented. Also, pressing any of theese keys: <kbd>\`</kbd> <kbd>\'</kbd> <kbd>\"</kbd> <kbd>\(</kbd> <kbd>\{</kbd> <kbd>\[</kbd> while some text is selected, will cause **ash** to enclose the selected text within the pair of opening/closing quote/brackets.