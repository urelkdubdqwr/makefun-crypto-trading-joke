import os

TEXT = "My stop-loss triggered at 3 a.m., the price doubled by 3:01, and my exchange sent a 'how did we do?' survey.\n"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
