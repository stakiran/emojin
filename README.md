# Emojin

A tool to help you create Emoji Art.

## Demo

Write a emojin file.

```
$ type demo.emojin
@o=:imp:
@-=:no_mouth:

--o--o--
--o--o--
ooo--ooo
--------
--------
ooo--ooo
--o--o--
--o--o--
```

Do emojin.py

```
$ python emojin.py -i demo.emojin --gfm | clip
```

And paste it to your markdown file.

:no_mouth::no_mouth::imp::no_mouth::no_mouth::imp::no_mouth::no_mouth:  
:no_mouth::no_mouth::imp::no_mouth::no_mouth::imp::no_mouth::no_mouth:  
:imp::imp::imp::no_mouth::no_mouth::imp::imp::imp:  
:no_mouth::no_mouth::no_mouth::no_mouth::no_mouth::no_mouth::no_mouth::no_mouth:  
:no_mouth::no_mouth::no_mouth::no_mouth::no_mouth::no_mouth::no_mouth::no_mouth:  
:imp::imp::imp::no_mouth::no_mouth::imp::imp::imp:  
:no_mouth::no_mouth::imp::no_mouth::no_mouth::imp::no_mouth::no_mouth:  
:no_mouth::no_mouth::imp::no_mouth::no_mouth::imp::no_mouth::no_mouth:  

## Requirement

- Python 2.7
- Windows 7+
  - Maybe works on Linux, but not tested yet.

## Install

- git clone https://github.com/stakiran/emojin

## How to use
Simple use:

- 1: Create your emojin file.
- 2: python emojin.py (your-emojin-file)
- 3: Copy outputs and paste it.

Detail of emojin file:

- For more detail about how to write emojin file, See [sample.emojin](sample.emojin).
- A Emojin file is a text simply, so you can also use another file-type. (i.e. `.txt`)

## Usage

```Terminal
$ python emojin.py -h
usage: emojin.py [-h] -i INPUT [--gfm]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
  --gfm                 Insert two-spaces to each line for line-breaking on
                        GFM. (default: False)
```

## License

[MIT License](LICENSE)

## Author

[stakiran](https://github.com/stakiran)
