# Generates the HTML pages from content/*.html fragments. Run: python3 build.py
import pathlib
pages = [
    ("index.html", "Home"),
    ("manage-users.html", "Manage users"),
    ("create-plan.html", "Create a plan"),
    ("create-pathway.html", "Create a pathway"),
    ("question-bank.html", "Question bank"),
    ("set-ujian.html", "Set ujian"),
    ("guru-exam-builder.html", "ExamBuilder"),
    ("guru-guide.html", "Guru guide"),
    ("pelajar-guide.html", "Pelajar guide"),
]
for f, title in pages:
    body = pathlib.Path("content/" + f).read_text()
    nav = "".join(
        f'<a href="{p}"{" class=\"active\"" if p == f else ""}>{t}</a>'
        for p, t in pages
    )
    pathlib.Path(f).write_text(
        f"""<!doctype html><html lang="ms"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · How-To Guides</title><link rel="stylesheet" href="assets/style.css"></head><body>
<header><div class="wrap"><a class="logo" href="index.html">How-To Guides</a><nav>{nav}</nav></div></header>
<main class="wrap">{body}</main><footer><div class="wrap">How-To Guides · Screens may differ slightly as the platform is updated.</div></footer></body></html>"""
    )
print("built", len(pages), "pages")
