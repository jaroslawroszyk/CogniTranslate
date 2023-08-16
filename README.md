# Translator Tool

This is a simple translation tool that translates English words from an input file to Polish using the translate package.

## Usage

1. Make sure you have Python and the `translate` package installed.
2. Place the words you want to translate in the `input.txt` file, with each word on a separate line.
3. Open `translate.py` and modify the third line to choose the target language. For example:
   - To translate to Polish: `translator = Translator(to_lang="pl")`
   - To translate to German: `translator = Translator(to_lang="de")`
   - And so on for other languages.
4. Run the script by executing `python CogniTranslate.py` or `python3 CogniTranslate.py`.
5. The translated words will be saved in the `output.txt` file.

## Requirements

- Python 3.x
- `translate` package (`pip install translate`)

## Example
**input.txt**
```
foreign
money
language
```

**output.txt**
```
foreign - obcy
money - pieniądze
language - język
```