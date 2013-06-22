import markdown
from markdown.treeprocessors import Treeprocessor


class LeadTrailTreeprocessor(Treeprocessor):
    def run(self, root):
        root[0].set("class", "leader")
        root[-1].set("class", "trailer")
        return root


class LeadTrailExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        ext = LeadTrailTreeprocessor(md)
        md.treeprocessors.add('leadtrail', ext, '_end')


def makeExtension(configs=None):
    return LeadTrailExtension(configs=configs)


if __name__ == "__main__":
    pass
