import collections
import json
import sys

INVENTORY = sys.argv[1]
OUT = sys.argv[2]

rows = []
with open(INVENTORY, encoding="utf-8") as handle:
    header = handle.readline().rstrip("\n").split("\t")
    for line in handle:
        parts = line.rstrip("\n").split("\t")
        if len(parts) != len(header):
            continue
        rows.append(dict(zip(header, parts)))

groups = collections.OrderedDict()
for row in rows:
    parts = row["path"].split("/")
    if len(parts) == 1:
        key = "(root)"
    elif parts[0] in ("packages", "apps") and len(parts) > 1:
        key = parts[0] + "/" + parts[1]
    else:
        key = parts[0]
    item = groups.setdefault(key, {
        "files": 0, "lines": 0, "bom": 0, "crlf": 0, "high": 0, "non_utf8": 0, "nul": 0,
    })
    item["files"] += 1
    item["lines"] += int(row["lines"])
    item["bom"] += 1 if row["bom"] == "True" else 0
    item["crlf"] += 1 if int(row["crlf"]) > 0 else 0
    item["high"] += 1 if int(row["high"]) > 0 else 0
    item["non_utf8"] += 1 if row["utf8"] == "False" else 0
    item["nul"] += 1 if int(row["nul"]) > 0 else 0

lines = [
    "| Grupo | Arquivos | Linhas | Arquivos >0x80 | Arquivos BOM | Arquivos CRLF | Nao-UTF8 | NUL | Encoding medido |",
    "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
]
for key, item in sorted(groups.items(), key=lambda pair: pair[1]["lines"], reverse=True):
    encoding = "UTF-8 LF"
    if item["non_utf8"]:
        encoding = "MISTO"
    lines.append(
        f"| {key} | {item['files']} | {item['lines']} | {item['high']} | {item['bom']} | {item['crlf']} | {item['non_utf8']} | {item['nul']} | {encoding} |"
    )
with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
    handle.write("\n".join(lines) + "\n")
print("\n".join(lines))
