import json
import sys

SOURCE = sys.argv[1]
OUT = sys.argv[2]

EXCLUDE_PREFIXES = (
    "out/", "dist/", "build/", "node_modules/", ".agents/", ".git/",
    "coverage/", "vendor/", "packages/whatsapp/vendor/",
)
EXCLUDE_PARTS = ("/vendor/", "/dist/", "/out/", "/build/", "/node_modules/")

with open(SOURCE, encoding="utf-8") as handle:
    data = json.load(handle)

results = []
for row in data.get("results", []):
    path = row["arquivo"].replace(chr(92), "/")
    if path.startswith(EXCLUDE_PREFIXES) or any(part in path for part in EXCLUDE_PARTS):
        continue
    results.append(row)

results.sort(key=lambda row: row["cc"], reverse=True)
summary = {
    "funcoes_fonte": len(results),
    "cc_total_fonte": sum(row["cc"] for row in results),
    "cc_max_fonte": results[0]["cc"] if results else 0,
    "cc_media_fonte": round(sum(row["cc"] for row in results) / len(results), 2) if results else 0,
    "acima_10": sum(1 for row in results if row["cc"] > 10),
    "acima_50": sum(1 for row in results if row["cc"] > 50),
    "top": results[:30],
    "excluded_files": len(data.get("results", [])) - len(results),
    "covered_files_note": "out/ and vendor/ excluded from the source podium",
}
with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
    json.dump(summary, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps({
    "funcoes_fonte": summary["funcoes_fonte"],
    "cc_max_fonte": summary["cc_max_fonte"],
    "cc_media_fonte": summary["cc_media_fonte"],
    "acima_10": summary["acima_10"],
    "acima_50": summary["acima_50"],
    "top5": [(row["arquivo"], row["funcao"], row["cc"]) for row in results[:5]],
}, indent=2))
