import os

# Verified count: 101 characters (101 UTF-8 bytes).
LINE = "Your next update will fix everything except the bug you actually reported. That one is now a feature."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(LINE)

print(len(LINE.encode("utf-8")))
