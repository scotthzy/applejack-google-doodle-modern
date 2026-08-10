#!/usr/bin/env python3
"""Validate the distributable UserCSS without third-party dependencies."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "applejack-google-doodle.user.css"


def strip_comments_and_strings(text: str) -> str:
    result: list[str] = []
    index = 0
    state = "code"
    quote = ""

    while index < len(text):
        char = text[index]
        following = text[index + 1] if index + 1 < len(text) else ""

        if state == "comment":
            if char == "*" and following == "/":
                state = "code"
                result.extend("  ")
                index += 2
            else:
                result.append("\n" if char == "\n" else " ")
                index += 1
            continue

        if state == "string":
            if char == "\\":
                result.append(" ")
                if following:
                    result.append("\n" if following == "\n" else " ")
                    index += 2
                else:
                    index += 1
            elif char == quote:
                state = "code"
                result.append(" ")
                index += 1
            else:
                result.append("\n" if char == "\n" else " ")
                index += 1
            continue

        if char == "/" and following == "*":
            state = "comment"
            result.extend("  ")
            index += 2
        elif char in {'"', "'"}:
            state = "string"
            quote = char
            result.append(" ")
            index += 1
        else:
            result.append(char)
            index += 1

    if state != "code":
        raise ValueError(f"unterminated {state}")
    return "".join(result)


def validate_balanced(text: str) -> list[str]:
    cleaned = strip_comments_and_strings(text)
    pairs = {"}": "{", ")": "(", "]": "["}
    stack: list[tuple[str, int]] = []
    errors: list[str] = []

    for position, char in enumerate(cleaned):
        if char in "{([":
            stack.append((char, position))
        elif char in "})]":
            if not stack or stack[-1][0] != pairs[char]:
                errors.append(f"unexpected {char!r} at offset {position}")
            else:
                stack.pop()

    for char, position in stack:
        errors.append(f"unclosed {char!r} at offset {position}")
    return errors


def main() -> int:
    text = STYLE.read_text(encoding="utf-8")
    errors = validate_balanced(text)

    required_metadata = ["@name", "@namespace", "@version", "@description"]
    for field in required_metadata:
        if not re.search(rf"(?m)^\s*{re.escape(field)}\s+\S", text):
            errors.append(f"missing required metadata: {field}")

    if "/* ==UserStyle==" not in text or "==/UserStyle== */" not in text:
        errors.append("missing UserCSS metadata block markers")
    if "http://" in text:
        errors.append("insecure HTTP URL found")
    if "deviantart.net" in text:
        errors.append("dead DeviantArt host found")
    if "data:image/" in text:
        errors.append("embedded third-party image found")
    if "THIRD_PARTY_NOTICES.md" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        errors.append("README does not link to THIRD_PARTY_NOTICES.md")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {STYLE.name}")
    print("OK: metadata and delimiters")
    print("OK: no insecure, dead-host, or embedded image references")
    print("OK: third-party notice linked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
