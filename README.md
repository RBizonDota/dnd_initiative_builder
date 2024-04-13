Util is designed to generate initiative list by provided configuration file.

Usage:
```bash
python setup.py install
dnd_ini examples/test_ini.yaml -w
```

Show help:
```bash
dnd_ini --help
```

Manual:
```
Usage: dnd_ini [OPTIONS] FILENAME

Options:
  --parser TEXT   Parser to use. Available options: ['yaml']  [default: yaml]
  --builder TEXT  Builder to use. Available options: ['std']  [default: std]
  --help          Show this message and exit.
  -w --web        Run in web interface
```

Output example:
```
> dnd_ini examples/test_ini.yaml
+-------+---------------+-------+-----+
| Номер | Имя персонажа | Игрок | Ини |
+-------+---------------+-------+-----+
|   1   |     test2     |       |  21 |
|   2   |     test5     |       |  17 |
|   3   |     test3     |       |  15 |
|   4   |     test4     |       |  12 |
|   5   |     test6     |       |  9  |
|   6   |    Маликет    | Роман |  6  |
|   7   |     test1     |       |  5  |
+-------+---------------+-------+-----+
```