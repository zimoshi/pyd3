# Pytecimalthon

**Pytecimalthon** is a custom Python runtime built to enforce **DBR 316 (Decimal Binary Rule 316)** — overriding traditional binary floating-point math with exact decimal arithmetic.

> "0.1 + 0.2 = 0.3 — exactly."

---

## 🚀 Features

- ✅ Replaces all float literals with `decimal.Decimal`
- ✅ Enforces consistent precision and rounding
- ✅ `.pyd` file support (Pytecimalthon scripts)
- ✅ CLI runner with multiple flags
- ✅ `.pydrc` config support (user-defined precision)
- ✅ Build `.pydc` precompiled files

---

## 🛠 Installation

Requires Python 3.7+  
You can make `pyd3` a global command using [py3sh](https://github.com/zimoshi/py3sh):

```bash
git clone https://github.com/zimoshi
cd pytecimalthon
sh setup.sh
```

---

## 📄 Example

```python
# test.pyd
print(0.1 + 0.2)
```

```bash
pyd3 test.pyd
# Output: 0.3
```

Compare with:

```bash
python3 test.pyd
# Output: 0.30000000000000004
```

---

## ⚙️ Config `.pydrc`

Supports custom settings:

```ini
precision=50
rounding=ROUND_HALF_UP
```

Apply via:

```bash
pyd3 configure ~/.pydrc test.pyd
```

---

## 🧠 Flags

| Flag | Description                               |
|------|-------------------------------------------|
| `-b` | Build `.pydc` precompiled file            |
| `-c` | Check DBR 316 compliance                  |
| `-d` | Debug: show transformed code              |
| `-h` | Help                                      |
| `-i` | Interactive REPL *(coming soon)*          |
| `-m` | Show current decimal context              |
| `-o` | Optimize: strip comments/whitespace       |
| `-p` | Profile execution time                    |
| `-q` | Quiet mode *(not yet used)*               |
| `-s` | Show result only *(not implemented)*      |
| `-u` | Update config from `.pydrc`               |
| `-v` | Version info                              |
| `-w` | Warn for imprecision *(not implemented)*  |
| `-x` | Execute inline code                       |

---

## 📜 License

MIT

---

Made with 🧠 by [@zimoshi](https://github.com/zimoshi)
