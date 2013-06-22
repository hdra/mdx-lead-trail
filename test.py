import markdown
import mdx_lead_trail

src = """
Hello, World!! This is paragraph #1

This is paragraph #2

This is paragraph #3

Goodbye, World! This is the last paragraph. """.strip()

ext = mdx_lead_trail.LeadTrailExtension()
html = markdown.markdown(src, extensions=[ext])

print(html)
