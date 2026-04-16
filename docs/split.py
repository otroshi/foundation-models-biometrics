import re
import unicodedata

with open("README.md", "r") as f:
    content = f.read()

sections = re.split(r"^## ", content, flags=re.MULTILINE)

# First part is intro → goes to index.md
intro = sections[0].strip()

with open("docs/index.md", "w", encoding="utf-8") as f:
    f.write(f"""---
title: Home
nav_order: 1
---

# Foundation Models and Biometrics

{intro}
""")

# Function to clean filenames
def clean_filename(title):
    # Remove emojis / non-ascii
    title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode()
    # Lowercase, replace spaces with underscores
    title = title.lower().strip()
    title = re.sub(r'[^a-z0-9\s-]', '', title)
    title = title.replace(" ", "_")
    return title

# Process sections
for i, section in enumerate(sections[1:], start=2):
    lines = section.strip().split("\n")
    title = lines[0].strip()
    body = "\n".join(lines[1:]).strip()

    filename = clean_filename(title)

    filepath = f"docs/{filename}.md"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""---
title: {title}
nav_order: {i}
---

# {title}

{body}
""")

print("Docs generated successfully!")