# Lab 3 - Huffman Encoding Binary Tree
Programmer: Chris Vaisnor

OS: Linux 20.04 LTS

Python Version: 3.10.8

IDE's: PyCharm and VSCode

# How To Use:
In the terminal, run:

```commandline
python3 lab3.py
```
First prompt is for the frequency table file name (FreqTable.txt)

Then the user moves to the Main Menu **enhancement**.

## -------------------Main Menu has 6 options -------------------

Encode/Decode A File | Encode/Decode A Manual Input | Print Tree in Preorder | Quit

When encoding/decoding from a file, the inputs and outputs are printed to the console and the user has an option to save to a file as well. 

Encoding/decoding a manual input is an **enhancement** I made which helps with testing.

# Note:
/broken_files_from_canvas contains the original files that were uploaded
to the canvas lab page. At the end of each line in each file is an 'artifacted' bit from the Windows OS it was written on. Both MacOS and Linux do not use that same 'new line' character, and Python cannot read that bit in defaut form.

I have created **fixed** versions of those files without that unreadable bit. The new versions are in the main directory with the new names:

clear_input.txt (instead of ClearText.txt)

coded_input.txt (instead of Encoded.txt)

FreqTable.txt (same name, fixed broken characters)

I have also included my own **test cases** for inputs and outputs following the same naming scheme.