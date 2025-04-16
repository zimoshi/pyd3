import sys, re, decimal, os, time

VERSION = "Pytecimalthon v0.1 — DBR 316 Enabled"

def load_config(path):
    config = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if "=" in line:
                    key, val = line.strip().split("=", 1)
                    config[key.strip()] = val.strip()
    return config

def apply_config(config):
    if 'precision' in config:
        decimal.getcontext().prec = int(config['precision'])
    if 'rounding' in config:
        decimal.getcontext().rounding = getattr(decimal, config['rounding'], decimal.ROUND_HALF_EVEN)

def transform(code):
    return re.sub(r"(?<![\w.])(\d+\.\d+)", r"decimal.Decimal('\1')", code)

def run_code(code, options):
    if options.get("debug"):
        print("=== Transformed Code ===")
        print(code)
        print("========================")

    if options.get("profile"):
        start = time.time()
        exec(code, {"decimal": decimal})
        print(f"\n[Execution time: {time.time() - start:.4f}s]")
    else:
        exec(code, {"decimal": decimal})

def run_file(filepath, options):
    with open(filepath, 'r') as f:
        code = f.read()
    if options.get("optimize"):
        code = re.sub(r"#.*", "", code)  # strip comments
        code = re.sub(r"\n+", "\n", code).strip()
    run_code(transform(code), options)

def build_pydc(filepath):
    with open(filepath, 'r') as f:
        code = f.read()
    transformed = transform(code)
    out = filepath.replace(".pyd", ".pydc")
    with open(out, 'w') as f:
        f.write(transformed)
    print(f"Built: {out}")

def show_meta():
    ctx = decimal.getcontext()
    print(f"Precision: {ctx.prec}")
    print(f"Rounding: {ctx.rounding}")

def check_dbr316(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if re.search(r"(?<![\w.])(\d+\.\d+)", line):
            print(f"Line {i+1}: {line.strip()}")

def run_inline(code, options):
    run_code(transform(code), options)

def print_help():
    print("""Usage: pyd3 [flags] <file.pyd>

Flags:
  -b     Build .pydc compiled version
  -c     Check DBR 316 compliance in code
  -d     Debug: show transformed code
  -h     Help
  -i     Launch interactive REPL (not implemented)
  -m     Show meta info (precision, rounding)
  -o     Optimize: strip comments and whitespace
  -p     Profile execution time
  -q     Quiet mode
  -s     Show result of final evaluated expression (not implemented)
  -u     Update config from ~/.pydrc
  -v     Version info
  -w     Warn for imprecise decimals (not implemented)
  -x     Execute inline code
""")

def main():
    args = sys.argv[1:]
    if not args:
        print_help()
        return

    options = {f: True for f in args if f.startswith("-")}

    if "-h" in options:
        print_help()
        return
    if "-v" in options:
        print(VERSION)
        return
    if "-m" in options:
        show_meta()
        return
    if "-u" in options:
        config = load_config(os.path.expanduser("~/.pydrc"))
        apply_config(config)

    if "-x" in options:
        idx = args.index("-x")
        if idx + 1 >= len(args):
            print("Error: No code after -x")
            return
        code = args[idx + 1]
        run_inline(code, options)
        return

    pyd_files = [arg for arg in args if arg.endswith(".pyd")]
    if not pyd_files:
        print("Error: No .pyd file specified")
        print_help()
        return

    filepath = pyd_files[0]

    if len(args) == 1 and filepath:
        run_file(filepath, options)
        return

    if "-b" in options:
        build_pydc(filepath)
        return
    if "-c" in options:
        check_dbr316(filepath)
        return

    run_file(filepath, options)

if __name__ == "__main__":
    main()
