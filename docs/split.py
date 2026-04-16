import re
import unicodedata

with open("README.md", "r") as f:
    content = f.read()

sections = re.split(r"^## ", content, flags=re.MULTILINE)

# First part is intro → goes to index.md
intro = sections[0].strip()

with open("docs/index.md", "w", encoding="utf-8") as f:
    f.write(f"""---
title: 🏠 Home
nav_order: 1
---

Welcome to the official webpage for the survey paper **Foundation Models and Biometrics: A Survey and Outlook**! 

This survey provides a comprehensive overview of the latest advancements in foundation models and their applications in the field of biometrics. We cover various types of foundation models, including large language models (LLMs), vision language models (VLMs), and multimodal models, and discuss their impact on biometric recognition, presentation attack detection, and other biometric applications.
            
The survey is published in the IEEE Transactions on Information Forensics and Security (TIFS) journal, and is **open access** on [IEEE Xplore](https://ieeexplore.ieee.org/document/11137396).            
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

def insert_toc(body):
    # find first ### heading
    match = re.search(r"\n###\s+", body)

    if match:
        idx = match.start()
        return body[:idx] + "\n\n* TOC\n{:toc}\n\n" + body[idx:]
    else:
        return body
    
TOC_PAGES = {
    "foundation_models",
    "applications_of_foundation_models_in_biometrics"
}

# Process sections
for i, section in enumerate(sections[1:], start=2):
    lines = section.strip().split("\n")
    title = lines[0].strip()
    body = "\n".join(lines[1:]).strip()

    body = body.replace("(#-foundation-models)", "(./foundation_models.html)") 
    body = body.replace("(#-applications-of-foundation-models-in-biometrics)", "(./applications_of_foundation_models_in_biometrics.html)") 

    filename = clean_filename(title)

    filepath = f"docs/{filename}.md"

    if filename in TOC_PAGES:
        body = insert_toc(body)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""---
title: {title}
nav_order: {i}
---

# {title}

{body}
""")

print("Docs generated successfully!")