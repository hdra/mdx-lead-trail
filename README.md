#Lead Trail Extension

Extension for Python Markdown library, adding extra classes name to the
first and last element in the document to be used for setting alignments.

## Install

    pip install git+https://github.com/hdra/mdx-lead-trail

Or do it your way with the source.

## Usage

    >>> import markdown
    >>> import mdx_lead_trail
    >>> src = """
    ... Hello, World!! This is paragraph #1
    ... 
    ... This is paragraph #2
    ... 
    ... Goodbye, World! This is the last paragraph. """.strip()
    >>> ext = mdx_lead_trail.LeadTrailExtension()
    >>> html = markdown.markdown(src, extensions=[ext])
    >>> print(html)
    <p class="leader">Hello, World!! This is paragraph #1</p>
    <p>This is paragraph #2</p>
    <p class="trailer">Goodbye, World! This is the last paragraph.</p>

Or specify a custom class name:

    >>> import markdown
    >>> import mdx_lead_trail
    >>> src = """
    ... Hello, World!! This is paragraph #1
    ... 
    ... This is paragraph #2
    ... 
    ... Goodbye, World! This is the last paragraph. """.strip()
    >>> configs = {'leader_class': 'head', 'trailer_class': 'foot'}
    >>> ext = mdx_lead_trail.LeadTrailExtension(configs)
    >>> html = markdown.markdown(src, extensions=[ext])
    >>> print(html)
    <p class="head">Hello, World!! This is paragraph #1</p>
    <p>This is paragraph #2</p>
    <p class="foot">Goodbye, World! This is the last paragraph.</p>

The old way also works:

    >>> import markdown
    >>> src = """
    ... Hello, World!! This is paragraph #1
    ... 
    ... This is paragraph #2
    ... 
    ... Goodbye, World! This is the last paragraph. """.strip()
    >>> html = markdown.markdown(src, ['lead_trail'])
    >>> print(html)
    <p class="leader">Hello, World!! This is paragraph #1</p>
    <p>This is paragraph #2</p>
    <p class="trailer">Goodbye, World! This is the last paragraph.</p>