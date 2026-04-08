import datetime
import re
import os
import bs4
from bs4 import BeautifulSoup

subfolders = [
    'classes', 'documents', 'functions',
    'interfaces', 'modules', 'types', 'variables'
]
base_dir = os.getcwd()

def prettify_signature(sig_div):
    """
    Converts a TypeDoc .tsd-signature div to well-formatted TypeScript code.
    """
    # Step 1: Raw line break reconstruction
    lines = []
    line_parts = []
    for elem in sig_div.children:
        if isinstance(elem, bs4.element.NavigableString):
            text = str(elem).replace('\u00a0', ' ').strip()
            if text:
                line_parts.append(text)
        elif isinstance(elem, bs4.element.Tag):
            if elem.name == "br":
                if line_parts:
                    lines.append(" ".join(line_parts))
                    line_parts = []
            else:
                text = elem.get_text(strip=True).replace('\u00a0', ' ')
                if text:
                    line_parts.append(text)
    if line_parts:
        lines.append(" ".join(line_parts))
    
    # Step 2: Fix common TypeScript syntax (spaces, indentation)
    def fix_line(l, is_first):
        # spaces for keywords
        l = re.sub(r'\b(typeof|readonly|keyof|as)\s*', r'\1 ', l)
        # spaces around colons (but NOT in mapped types)
        l = re.sub(r'([A-Za-z0-9_$$"\'])\s*:\s*', r'\1: ', l)
        # spaces around = (but NOT in objects)
        l = re.sub(r'\s*=\s*', r' = ', l)
        # indent "|", except first line
        l = re.sub(r'^\s*\|', r'|', l)
        # For unions/arrays/mapped types, indent if not the first line
        if not is_first:
            if l.strip().startswith(("|", "{", "}", "(", "[")) or re.match(r'^[A-Z_]+\:|$$.*$$\:', l):
                return "  " + l
            return "  " + l
        return l

    out_lines = []
    for idx, l in enumerate(lines):
        fixed = fix_line(l, idx == 0)
        out_lines.append(fixed)
    # Join and fix closing braces for objects
    sig = "\n".join(out_lines)
    sig = re.sub(r'\}\s*=\s*\.\.\.', '} = ...', sig)
    sig = re.sub(r';\s*\}', ';\n}', sig)
    return sig.strip()

def auto_frontmatter(output_path, input_html_path, markdown_text):
    """
    Prepends a YAML frontmatter block to Markdown text.
    For classes/interfaces/types/functions/variables/modules, 
    always use 'SDK.MemberType class/interface/type/...' from filename, not heading.
    For docs/changelog/etc., fallback to heading.
    """

    # Get first Markdown heading, if present
    match = re.search(r'^#\s*(.+)', markdown_text, re.MULTILINE)
    heading_title = match.group(1).strip() if match else None

    # Normalize relative path and filename (for source/title)
    rel_path = os.path.relpath(input_html_path, os.getcwd()).replace("\\", "/")
    filename = os.path.basename(input_html_path)
    base_title = filename.replace('.html', '').replace('index.', '')
    category = os.path.basename(os.path.dirname(input_html_path))

    # Canonical title logic
    if filename.lower() == 'changelog.html':
        file_title = "CHANGELOG"
    elif filename.lower() == 'modules.html':
        file_title = "SDK Modules"
    elif category == 'classes':
        file_title = f"{base_title} class"
    elif category == 'interfaces':
        file_title = f"{base_title} interface"
    elif category == 'types':
        file_title = f"{base_title} type"
    elif category == 'functions':
        file_title = f"{base_title} function"
    elif category == 'variables':
        file_title = f"{base_title} variable"
    elif category == 'modules':
        file_title = f"{base_title} module"
    else:
        file_title = base_title  # For documents, use filename

    # For technical pages, always use filename-derived title.
    # For documents, fallback to heading if it exists.
    if category in [
        'classes', 'interfaces', 'types', 'functions', 'variables', 'modules'
    ]:
        title = file_title
    else:
        title = heading_title if heading_title else file_title

    today = datetime.date.today().isoformat()
    tool = "extract-to-md.py"
    notes = "Extracted from Waze SDK HTML docs. Cleaned for LLM context."

    frontmatter = (
        f"---\n"
        f"title: {title}\n"
        f"source: {rel_path}\n"
        f"created: {today}\n"
        f"tool: {tool}\n"
        f"notes: {notes}\n"
        f"---\n\n"
    )

    return frontmatter + markdown_text

def extract_method_block(method_section):
    """Extract a single method/member block as advanced Markdown."""
    out = []
    # Method name = h3 with id
    h3 = method_section.find('h3')
    if h3:
        method_name = h3.get_text(strip=True)
        out.append(f"### {method_name}")

    # Signatures
    for sig_ul in method_section.find_all('ul', class_='tsd-signatures'):
        for li in sig_ul.find_all('li', recursive=False):
            # The .tsd-signature div (with what looks like the actual signature)
            sig_div = li.find('div', class_='tsd-signature')
            if sig_div:
                sig_text = prettify_signature(sig_div)
                if sig_text:
                    out.append("")
                    out.append("```typescript")
                    out.append(sig_text)
                    out.append("```")
            # More info below signature: Returns, description, etc.
            desc = li.find('div', class_='tsd-description')
            if desc:
                out.append(desc.get_text(strip=True))

            # Parameters block
            param_div = li.find('div', class_='tsd-parameters')
            if param_div:
                param_title = param_div.find('h4')
                if param_title:
                    out.append(f"**{param_title.get_text(strip=True)}**")
                for param_list in param_div.find_all('ul', class_='tsd-parameter-list'):
                    # Parameter(s)
                    for param_li in param_list.find_all('li', recursive=False):
                        pl = param_li.find('h5')
                        if pl:
                            param_name = pl.get_text(strip=True)
                            desc_divs = param_li.find_all('div', class_='tsd-comment')
                            descr = " ".join([d.get_text(" ", strip=True) for d in desc_divs])
                            out.append(f"- `{param_name}`: {descr}")

            # Returns
            for ret_title in li.find_all('h4', class_='tsd-returns-title'):
                out.append(f"**Returns:** `{ret_title.get_text(strip=True)}`")
            for ret_desc in li.find_all('p'):
                if ret_desc.get_text(strip=True):
                    out.append(ret_desc.get_text(strip=True))

            # Throws
            for throws in li.find_all('div', class_="tsd-tag-throws"):
                # Heading and content
                for h in throws.find_all('h4'):
                    out.append(f"**{h.get_text(strip=True)}**")
                for p in throws.find_all('p'):
                    out.append(f"- {p.get_text(strip=True)}")
    return "\n".join(out)

def extract_typedoc_code_block(code_tag):
    # Reconstruct TypeDoc code, joining adjacent spans and <br> as newlines
    lines = []
    current = []
    for elem in code_tag.children:
        if isinstance(elem, bs4.element.NavigableString):
            txt = str(elem).replace('\u00a0', ' ')
            if txt:
                current.append(txt)
        elif isinstance(elem, bs4.element.Tag):
            if elem.name == "span":
                current.append(elem.get_text().replace('\u00a0', ' '))
            elif elem.name == "br":
                if current:
                    lines.append(''.join(current))
                    current = []
    if current:  # flush remaining
        lines.append(''.join(current))
    # The lines are ready!
    return '\n'.join(line.rstrip() for line in lines if line.strip())

def extract_description_markdown(desc):
    out = []
    # Handle examples
    for example in desc.find_all("div", class_="tsd-tag-example"):
        example_title = example.find("h4")
        if example_title:
            out.append(f"**{example_title.get_text(strip=True)}**")
        for code_block in example.find_all("code"):
            parent_pre = code_block.find_parent("pre")
            if parent_pre:
                code_text = extract_typedoc_code_block(code_block)
                out.append("```typescript")
                out.append(code_text)
                out.append("```")
    # Handle regular paragraphs and inline code
    for node in desc.children:
        if getattr(node, "name", None) == "pre":
            code_block = node.find("code")
            if code_block:
                code_text = extract_typedoc_code_block(code_block)
                out.append("```typescript")
                out.append(code_text)
                out.append("```")
        elif getattr(node, "name", None) in ("p", "ul", "ol"):
            out.append(node.get_text(" ", strip=True))
    return "\n".join(out)

def extract_class_overview(main):
    """Extracts overview for class/type/variable/alias including signature and variable members."""
    out = []

    # Title block
    page_title = main.find(class_="tsd-page-title")
    if page_title:
        for h1 in page_title.find_all('h1'):
            out.append(f"# {h1.get_text(strip=True)}")

    signature = main.find('div', class_='tsd-signature')
    if signature:
        sig_text = prettify_signature(signature)
        if sig_text:
            out.append("")
            out.append("```typescript")
            out.append(sig_text)
            out.append("```")

    # Description/comments
    for sec in main.find_all('section', class_="tsd-panel tsd-comment"):
        for c in sec.find_all(class_='tsd-comment'):
            txt = c.get_text(strip=True)
            if txt:
                out.append(txt)

    # Variable/type alias extra members (if present)
    decl = main.find('div', class_='tsd-type-declaration')
    if decl:
        params = decl.find_all('li', class_='tsd-parameter')
        if params:
            out.append("#### Members")
            out.append("| Name | Type/Value | Tags |")
            out.append("|------|------------|------|")
            for param in params:
                h5 = param.find('h5')
                if not h5:
                    continue
                tags = ','.join([t.get_text(strip=True) for t in h5.find_all('code', class_="tsd-tag")])
                name = h5.find('span', class_="tsd-kind-property")
                name = name.get_text(strip=True) if name else ""
                value = h5.find('span', class_="tsd-signature-type")
                value = value.get_text(strip=True) if value else ""
                out.append(f"| {name} | {value} | {tags} |")

    # Detailed Property/Method headers
    for member_group in main.find_all('details', class_='tsd-member-group'):
        h2 = member_group.find('h2')
        if h2:
            out.append(f"## {h2.get_text(strip=True)}")
        for member in member_group.find_all("section", class_="tsd-panel tsd-member"):
            h3 = member.find("h3")
            if h3:
                tag = h3.find("code", class_="tsd-tag")
                tag_text = tag.get_text(strip=True) if tag else ""
                span = h3.find("span")
                name_text = ""
                if span:
                    name_text = "".join(span.strings).replace("\n", "").replace("\r", "").strip()
                # If no tag/span, try to split Readonly/Optional prefix
                if not tag_text and not name_text:
                    raw = h3.get_text(" ", strip=True)
                    m = re.match(r"(Readonly|Optional)?(.+)", raw)
                    if m:
                        tag_text = m.group(1) or ""
                        name_text = m.group(2) or raw
                if tag_text and name_text:
                    out.append(f"### **{tag_text}** `{name_text}`")
                elif name_text:
                    out.append(f"### `{name_text}`")
                # Signature (typescript, improved formatting)
                sig = member.find("div", class_="tsd-signature")
                if sig:
                    sig_text = prettify_signature(sig)
                    if sig_text:
                        out.append("")
                        out.append("```typescript")
                        out.append(sig_text)
                        out.append("```")
                desc = member.find("div", class_="tsd-description")
                if desc:
                    out.append(extract_description_markdown(desc))
    return "\n".join(out)

def extract_module_overview(main):
    """Extract a full overview of a TypeDoc module page as Markdown, .md links."""
    out = []
    page_title = main.find(class_="tsd-page-title")
    if page_title:
        for h1 in page_title.find_all('h1'):
            out.append(f"# {h1.get_text(strip=True)}")
    for details in main.find_all('details', class_='tsd-member-group'):
        h2 = details.find('h2')
        if h2:
            out.append(f"## {h2.get_text(strip=True)}")
        member_summaries = details.find_all('dt', class_='tsd-member-summary')
        if member_summaries:
            for dt in member_summaries:
                a = dt.find('a')
                name = a.get_text(strip=True) if a else '[No name]'
                href = a['href'] if a and a.has_attr('href') else ''
                # Change .html to .md in links
                md_href = href
                if md_href.endswith('.html'):
                    md_href = md_href[:-5] + '.md'
                next_dd = dt.find_next_sibling('dd')
                desc = ''
                if next_dd:
                    desc = next_dd.get_text(" ", strip=True)
                if href:
                    line = f"- [{name}]({md_href})"
                else:
                    line = f"- {name}"
                if desc:
                    line += f": {desc}"
                out.append(line)
    return "\n".join(out)

def extract_modules_toc(main):
    """Extracts the main modules.html page (TypeDoc SDK TOC) as Markdown, with .md links, minimal formatting."""
    out = []
    # Title
    page_title = main.find(class_="tsd-page-title")
    if page_title:
        h1 = page_title.find('h1')
        if h1:
            out.append(f"# {h1.get_text(strip=True)}")
    # For each section (Documents, Modules, etc.)
    for details in main.find_all('details', class_='tsd-member-group'):
        h2 = details.find('h2')
        if h2:
            out.append(f"## {h2.get_text(strip=True)}")
        member_summaries = details.find_all('dt', class_='tsd-member-summary')
        for dt in member_summaries:
            a = dt.find('a')
            name = a.get_text(strip=True) if a else '[No name]'
            href = a['href'] if a and a.has_attr('href') else ''
            # Convert .html to .md for markdown links
            md_href = href
            if md_href.endswith('.html'):
                md_href = md_href[:-5] + '.md'
            out.append(f"- [{name}]({md_href})")
    return "\n".join(out)

def extract_changelog_markdown(main):
    """
    Extracts the main changelog content as Markdown.
    - Preserves heading structure (h1=##, h2=###, etc.).
    - Preserves bullet points.
    - Removes anchor-link SVG icons and other non-doc junk.
    - Returns Markdown string.
    """
    # Changelog is inside: <div class="tsd-panel tsd-typography">...</div>
    panel = main.find('div', class_='tsd-panel tsd-typography')
    if not panel:
        return "[No changelog content found]\n"

    out = []

    # Optionally: Title at top of page (breadcrumb or just plain h1)
    page_title = main.find(class_="tsd-page-title")
    if page_title:
        h1 = page_title.find('h1')
        if h1:
            out.append(f"# {h1.get_text(strip=True)}")

    # For each direct child in the changelog panel
    for el in panel.children:
        if el.name is None:
            continue  # Skip NavigableString etc
        # Headings: h1/h2/h3 … use Markdown heading format
        if el.name in ['h1', 'h2', 'h3', 'h4']:
            level = {"h1": "##", "h2": "###", "h3": "####", "h4": "#####"}[el.name]
            # Remove anchor icon
            text_node = el.find(string=True)
            out.append(f"{level} {text_node.strip() if text_node else el.get_text(strip=True)}")
        # Bullet points
        elif el.name in ['ul', 'ol']:
            for li in el.find_all('li', recursive=False):
                # Get text content, handle code tags etc
                txt = li.get_text(" ", strip=True)
                out.append(f"- {txt}")
        # Numbered lists
        elif el.name == 'ol':
            idx = 1
            for li in el.find_all('li', recursive=False):
                out.append(f"{idx}. {li.get_text(' ', strip=True)}")
                idx += 1
        # Paragraphs
        elif el.name == 'p':
            out.append(el.get_text(" ", strip=True))
        # For <div> with more h2/h3, process recursively
        elif el.name == 'div':
            for subel in el.find_all(['h1', 'h2', 'h3', 'h4', 'ul', 'ol', 'p'], recursive=False):
                # Recursively apply same extraction as above (just copy-paste the above block, or call yourself)
                # Here, for brevity, just call recursively:
                out.append(extract_changelog_markdown(subel))
    return "\n\n".join(out).strip() + "\n"

def extract_advanced_markdown(soup, filename=None):
    """
    Extracts a doc page as Markdown.
    Special-cases 'modules.html' (main TOC), otherwise uses class/module logic.
    """
    main = soup.find('div', class_='col-content')
    if not main:
        return "[No main content found]\n"
    # Special: handle 'modules.html' as the main TOC
    if filename and os.path.basename(filename).lower() == "modules.html":
        return extract_modules_toc(main)
    
    # Special-case documents/CHANGELOG.html
    if filename and os.path.basename(filename).lower() == "changelog.html":
        return extract_changelog_markdown(main)

    page_title = main.find(class_="tsd-page-title")
    is_module = False
    if page_title:
        h1 = page_title.find('h1')
        if h1 and h1.get_text(strip=True).lower().startswith("module"):
            is_module = True
    lines = []
    if is_module:
        lines.append(extract_module_overview(main))
    else:
        lines.append(extract_class_overview(main))
    return "\n\n".join([line for line in lines if line]).strip() + '\n'

# FIRST: handle files directly in the root folder
for filename in os.listdir(base_dir):
    base, ext = os.path.splitext(filename)
    if ext.lower() != ".html":
        continue
    if "-clean" in base:
        continue
    input_path = os.path.join(base_dir, filename)
    with open(input_path, encoding='utf8') as f:
        soup = BeautifulSoup(f, 'lxml')
    # Pass input_path as filename when calling the extractor
    markdown_text = extract_advanced_markdown(soup, filename=input_path)
    output_filename = f"{base}.md"
    output_path = os.path.join(base_dir, output_filename)
    with open(output_path, 'w', encoding='utf8') as out:
        out.write(auto_frontmatter(output_path, input_path, markdown_text))
    print(f"Saved cleaned Markdown file: {output_path}")

# THEN: handle files in subfolders as before
for folder in subfolders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        base, ext = os.path.splitext(filename)
        if ext.lower() != ".html":
            continue
        if "-clean" in base:
            continue
        input_path = os.path.join(folder_path, filename)
        with open(input_path, encoding='utf8') as f:
            soup = BeautifulSoup(f, 'lxml')
        markdown_text = extract_advanced_markdown(soup, filename=input_path)
        output_filename = f"{base}.md"
        output_path = os.path.join(folder_path, output_filename)
        with open(output_path, 'w', encoding='utf8') as out:
            out.write(auto_frontmatter(output_path, input_path, markdown_text))
        print(f"Saved cleaned Markdown file: {output_path}")
