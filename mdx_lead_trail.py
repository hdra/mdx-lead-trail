'''
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
'''

import markdown
from markdown.treeprocessors import Treeprocessor


class LeadTrailTreeprocessor(Treeprocessor):
    def run(self, root):
        root[0].set("class", self.config.get('leader_class')[0])
        root[-1].set("class", self.config.get('trailer_class')[0])
        return root


class LeadTrailExtension(markdown.Extension):
    def __init__(self, configs=None):
        self.config = {
            'leader_class': ['leader', 'Class name for the first element'],
            'trailer_class': ['trailer', 'Class name for the last element']
        }
        if configs is not None:
            configs = dict(configs)
        else:
            configs = {}
        for key, value in configs.items():
            self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        ext = LeadTrailTreeprocessor(md)
        ext.config = self.config
        md.treeprocessors.add('leadtrail', ext, '_end')


def makeExtension(configs=None):
    return LeadTrailExtension(configs=configs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
