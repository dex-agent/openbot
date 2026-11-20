import json
import sqlite3
import sys

DB = sys.argv[1]
OUT = sys.argv[2]

con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
con.row_factory = sqlite3.Row
cur = con.cursor()

classes = [dict(row) for row in cur.execute("""
select n.file_path, n.name, n.line_start, n.line_end,
       (n.line_end - n.line_start + 1) as span,
       (select count(*) from edges e
          join nodes c on c.qualified_name = e.target_qualified
         where e.kind = 'CONTAINS' and e.source_qualified = n.qualified_name and c.kind = 'Function') as methods
  from nodes n
 where n.kind = 'Class' and n.is_test = 0
   and n.file_path not like '%/vendor/%'
 order by methods desc, span desc
 limit 40
""")]

functions = [dict(row) for row in cur.execute("""
select file_path, name, line_start, line_end, (line_end - line_start + 1) as span
  from nodes
 where kind = 'Function' and is_test = 0
   and file_path not like '%/vendor/%'
 order by span desc
 limit 40
""")]

hotspots = [dict(row) for row in cur.execute("""
select n.file_path, count(*) as inbound
  from edges e join nodes n on n.qualified_name = e.target_qualified
 where e.kind in ('IMPORTS_FROM','CALLS')
 group by n.file_path
 order by inbound desc
 limit 20
""")]

payload = {"god_class": classes, "long_method": functions, "file_hotspots": hotspots}
with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
    json.dump(payload, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps({
    "god_class_top5": [(row["file_path"], row["name"], row["methods"], row["span"]) for row in classes[:5]],
    "long_method_top5": [(row["file_path"], row["name"], row["span"]) for row in functions[:5]],
}, indent=2))
