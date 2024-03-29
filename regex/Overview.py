
import re 

"""
A regular expression is a special sequence of characters that helps you
match or find other strings or sets of strings, using a specialized syntax held in a pattern.

Regular expressions are widely used in UNIX world.

The module re provides full support for Perl-like regular expressions in Python.

The "re" module raises the exception re.error if an error occurs while compiling or
using a regular expression.

We would cover two important functions, which would be used to handle regular expressions.

But a small thing first: There are various characters,
which would have special meaning when they are used in regular expression.

To avoid any confusion while dealing with regular expressions,
we would use Raw Strings as r'expression'.

# Basic patterns which match single chars :

a, X, 9, <      -- ordinary characters just match themselves exactly.
. (a period)    -- matches any single character except newline '\n'
\w              -- matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
\W              -- matches any non-word character.
\b              -- boundary between word and non-word
\s              -- matches a single whitespace character -- space, newline, return, tab
\S              -- matches any non-whitespace character.
\t, \n, \r      -- tab, newline, return
\d              -- decimal digit [0-9]
\D              -- non-decimal digit [0-9]
^                = matches start of the string
$                = match the end of the string
\               -- inhibit the "specialness" of a character.

# Compilation flags :

Compilation flags let you modify some aspects of how regular expressions work.

Flags are available in the re module under two names,

a long name such as IGNORECASE and a short, one-letter form such as I.

---------------------------------------------------------------
Flag	        Meaning
---------------------------------------------------------------
ASCII, A	  Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
DOTALL, S	  Make . match any character, including newlines
IGNORECASE, I	  Do case-insensitive matches
LOCALE, L	  Do a locale-aware match
MULTILINE, M	  Multi-line matching, affecting ^ and $
VERBOSE, X
(for ‘extended’)  Enable verbose REs, which can be organized more cleanly and understandably
"""



