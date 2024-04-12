Util is designed to generate initiative list by provided configuration file.

Usage:
```bash
python setup.py install
dnd_ini examples/test_ini.yaml
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
```