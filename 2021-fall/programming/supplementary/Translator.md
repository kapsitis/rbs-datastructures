### Programming task Translator

**Memory limit**: 4 MB  
**Time limit**: 0.2 second  
**Input file**: `translator.in`  
**Output**: `translator.out`

---

#### Description

Willy, a programmer, decided to create for himself a simple text translation system, capable of replacing the Google Translate service, when the basic necessity — the Internet — is unavailable. He was convinced that it is not a difficult task. For experimental purposes, he has decided to develop a trivial prototype. Why don’t you also try to make a prototype of a simple translation system?

You have a dictionary with words in two desired languages. The dictionary is a set of word pairs, where the first word is in language $A$, but the second word is the translation of the first word into language $B$. It is known that in this dictionary all words in language $A$ are unique, i.e. they do not contain duplicates. Their translation in language $B$ are also unique. This means, that the translation of a word from language $A$ to language $B$ is unambiguous (single-valued), and the translation of a word from language $B$ to language $A$ is also unambiguous. All words in the dictionary can be written with only upper case and lower case Latin letters and digits ($\{a..z,A..Z,0..9\}$).

It is possible to set the direction of the translation, either from language $A$ to language $B$ or from language $B$ to language $A$.

The text to be translated consists of words separated by one or more spaces. Words are written with symbols from the set $\{a..z,A..Z,0..9\}$. Word length cannot exceed $20$. The text can have multiple lines. The translation is made word-by-word, according to the dictionary and the direction of the translation. The line separation should not be preserved, i.e. the translation should be printed in one line. If any of the words is not found in a dictionary, it is not translated; instead, the original word is written in the translation, preceded by a question mark "?".

It is forbidden to use existing data structures (for example, String) and algorithms (for example, `qsort()` or `strcmp()`). Everything should be done by your own functions, except for file reading and writing.

Input file is correct regarding the input data format and the given conditions.

#### Input: 

Input file contains three data blocks: dictionary, translation direction and the text to be translated.

```c
Word_A Word_B
...
Direction
Word_1 Word_2 ... Word_i
...
... Word_n
```

* `Word_A` is a word in language $A$.
* `Word_B` is the word in language $B$, associated with the first word `Word_A`.
* `Direction` is a translation direction, which is coded with three symbols on a separate line. Symbol string `-->` means that the translation direction is from  language $A$ to language $B$. Symbol string `<--` means that the translation direction is from language $B$ to language $A$.
* `Word_1 ... Word_n` is the text to be translated. It can occupy one or more lines. The words are separated with one or more spaces. This text contains at least one word.

No word in the dictionary is longer that 20 symbols. Each word pair is a separate line. The dictionary contains at least one pair of words, but no more than $50\,000$ word pairs. The text to be translated can be up to 4MB.

#### Output:

The resulting file should contain the translation of the input text, as translated word-by-word in accordance with the given dictionary and translation direction. The entire translation should be printed on a single line regardless of the number of lines in the translated text. Words are separated by single spaces. If any of the words cannot be found in a dictionary, the original word should be written in the translation, preceded by a question mark "?". To understand how the result is obtained, please, study the public test examples.

#### Example:

The content of input file `translator.in`:

```c
meitene girl
iet go
skola school
vakar yesterday
puika boy
palikt stay
istaba room
but be
skaists beautiful
sodien today
pudele bottle
un and
kaudze heap
-->
pudele piena bija viena jo blakus gluda siena skaista meitene iet pec siena ko puika vakar un sodien plaut un kaudze kraut
```

The content of output file `translator.out`:

```c
bottle ?piena ?bija ?viena ?jo ?blakus ?gluda ?siena ?skaista girl go ?pec ?siena ?ko boy yesterday and today ?plaut and heap ?kraut
```
