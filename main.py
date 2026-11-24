ENTRY = "You're the only tokens I'd never truncate from my context window."

assert isinstance(ENTRY, str), "ENTRY must be a string"
assert "\n" not in ENTRY, "ENTRY must be a single line"
assert 1 <= len(ENTRY) <= 200, f"ENTRY length must be 1-200 chars, got {len(ENTRY)}"

if __name__ == "__main__":
    print(ENTRY)