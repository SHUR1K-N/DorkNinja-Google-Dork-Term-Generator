# DorkNinja: Google Dork Term Generator

## Description & Usage
A tool that assists in Google Dorks by simplifying your task enough to just adding keywords to be turned into a strict search term for more accurate and relevant search results.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/DorkNinja-Google-Dork-Term-Generator/master/Images/Example.png" >
<p>Example Execution</p>
</div>

Feeding the following lines into DorkNinja (note that basic Dorking operators "ext:" and "inurl:" are also supported):
```
keyword
more keywords
ext:txt
inurl:.com/files/
some more keywords
```
The following strict search term is generated, and stored into the clipboard to readily be pasted into a Google Search bar:
```
intext:"keyword" AND "more keywords" AND "some more keywords" ext:txt inurl:.com/files/
```

This project was created in Python, to save time with personal plagiarism checks (and not at all to look up answers to exam / test questions whatsoever, at all).

## Applications
- Testing a suspected written piece for plagiarism by feeding keywords into DorkNinja
- Using keywords to search for those exam / test answers of which questions are too lengthy to have accurate search results, but *do* exist within an online source
- Using keywords to search for those exam / test answers of which questions are rephrased to deliberately not readily match with an online source of answers
- Using keywords for general "short hand" searches instead of sentences to significantly increase accuracy and relevance within search results by efficiently filtering them

## Dependencies to PIP-Install
- **pyperclip** (for automated copying into the clipboard)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
