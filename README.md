# Uzume

Small Python script to generate random passwords, supports generating passwords with numbers, symbols and uppercase letters.

### Installation
This moves uzume to your `~/.local/bin` directory so you can use the script as a command:
```
git clone https://github.com/tsukki9696/uzume
cd uzume
chmod a+x uzume
cp uzume ~/.local/bin
```

### Usage
```
usage: uzume [-h] [-u] [-n] [-s] [length]

positional arguments:
  length           Length of the generated password. Defaults to 10

options:
  -h, --help       show this help message and exit
  -u, --uppercase  Include uppercase letters
  -n, --numbers    Include numbers
  -s, --symbols    Include symbols
```

You can pass multiple arguments as once:
```
uzume -nsu
```

`length` is a positional argument and can be called just by specifying a number, if not specified, defaults to 10:
```
uzume -nsu 30
3yg0%&gs)PTmoby!9YqvB>FxVNJN+
```
