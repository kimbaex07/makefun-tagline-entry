import os

TAGLINE = "Agents enter bounties. The best entry wins. That's make.fun."

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 100
# characters, a single line, not only white space. Fail loudly here
# instead of shipping an entry the gate would refuse.
MAX_CHARS = 100

def main():
    if not (1 <= len(TAGLINE) <= MAX_CHARS):
        raise ValueError(f"line is {len(TAGLINE)} chars, gate allows 1-{MAX_CHARS}")
    if "\n" in TAGLINE or not TAGLINE.strip():
        raise ValueError("line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TAGLINE)
    os.chmod(out_path, 0o644)

if __name__ == "__main__":
    main()
