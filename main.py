import os

LINE = "The office bathroom is the only meeting room nobody can book — it's also the only one where anything gets done."

assert 1 <= len(LINE) <= 200 and LINE.strip()
assert "\n" not in LINE

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
