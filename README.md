# DorkNinja: Google Dork Term Generator

## Description & Usage
A tool that assists in Google Dorks by simplifying your task enough to just adding the keywords to be turned into a strict search term.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/ScrambleNinja-File-Scrambler/master/Images/Example.png" >
<p>Example Execution</p>
</div>

Feeding the following lines into DorkNinja:
```
keyword
more keywords
some more keywords
```
The following strict search term is generated, and stored into the clipboard to be pasted into a Google Search bar:
```
intext:"keyword" AND "more keywords" AND "some more keywords" AND "actually, here is an entire sentence to strict-match"
```
The basic Dorking operators "inurl:" and :ext:" can also be used with DorkNinja, :
```
keyword
ext:txt
more keywords
inurl:.com/files/

```
The following output is generated, and stored into the clipboard to be pasted into a Google Search bar:
```
intext:"keyword" AND "more keywords" AND "actually, here is an entire sentence to strict-match" ext:txt inurl:.com/files/
```

This project was created in Python, to save time with searches with plagiarism checks (and not at all to look up answers to exam / test questions whatsoever).

## Applications
- Testing a suspected written piece for plagiarism by feeding keywords into DorkNinja
- Searching for those exam / test answers of which questions are too long to have accurate search results, but *do* exist within an online source
- Searching for those exam / test answers of which questions are cleverly rephrased to deliberately not match with an online source of answers
- General "short hand" searches with keywords instead of sentences to significantly increase accuracy and relevance within search results

## Dependencies to PIP-Install
- **pyperclip** (for automated copying into the clipboard)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
