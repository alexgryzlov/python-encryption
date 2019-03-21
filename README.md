# python-encryption

## Usage
```
$ python main.py {encrypt decrypt train hack}
```
## Encrypt/Decrypt
```
4 optional arguments:
-i, --input
-o, --output
-c, --cipher[caesar vigenere vernam]
-k, --key
```

## Train
```
Train creates a language model (character frequencies distribution)

2 optional arguments:
--model_file (where to save the {character: frequency} table)
-i, --input
```

## Hack
```
Decrypts Caesar Cipher using the given language model

3 optional arguments:
-i, --input
-o, --output
--model_file
```
