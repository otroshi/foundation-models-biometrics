import re

with open("README.md", "r") as f:
    content = f.read()

sections = re.split(r"^## ", content, flags=re.MULTILINE)

for section in sections[1:]:
    title, *body = section.split("\n", 1)
    filename = title.lower().replace(" ", "_") + ".md"

    with open(f"docs/{filename}", "w") as f:
        f.write(f"# {title}\n\n{body[0]}")