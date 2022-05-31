__all__ = ["Tree", "H", "V", "construct_page"]

from torch_snippets import *
from copy import deepcopy


def construct_page(*regions, **kwargs):
    page = {}
    page["split"] = "horizontal" if isinstance(regions[0], H) else "vertical"
    _n = sum(L(regions).map(lambda x: x[x["split_dimension"]]))
    for region in regions:
        region[region["split_dimension"]] /= _n
    page["children"] = [region for region in regions]
    return Tree(page, **kwargs)


class R(AttrDict):
    def __init__(self, split_dimension, children):
        self.split_dimension = split_dimension
        self.children = L(children) if isinstance(children, (list, tuple)) else L([])
        self.normalize_children()

    def normalize_children(self):
        if len(self.children) < 2:
            return
        _n = sum(self.children.map(lambda x: x.split))
        for child in self.children:
            split_dimension = child.split_dimension
            child.split = child.split / _n
            child[split_dimension] = child.split

    def init_region(self, metric, **kwargs):
        split = self.split_dimension
        region = dict(
            split=metric,
            children=self.children,
            content=kwargs.pop("content", None),
            id=kwargs.pop("id", rand(12)),
            **kwargs,
        )
        super().__init__(region)

    def __repr__(self):
        return f"{self.__class__.__name__}: {super().__repr__()}"


class H(R):
    def __init__(self, height=-1, children=None, **kwargs):
        super().__init__(split_dimension="height", children=children)
        self.init_region(height, **kwargs)
        self.height = height


class V(R):
    def __init__(self, width=-1, children=None, **kwargs):
        super().__init__(split_dimension="width", children=children)
        self.init_region(width, **kwargs)
        self.width = width


class Tree:
    def __init__(self, cfg, **kwargs):
        if isinstance(cfg, str):
            cfg = read_json(cfg)
        self.cfg = AttrDict({**cfg, **kwargs})
        self.splits = ["horizontal", "vertical"]
        self.vars = ["width", "height"]

    def generate(self, h=100, w=100, noisy=False, shuffle_children=False):
        self.noisy = noisy
        self.shuffle_children = shuffle_children
        self.bbs = L([])
        self.im = Image.fromarray((np.ones((h, w, 3)) * 255).astype(np.uint8))
        regions = L([])
        cfg = deepcopy(self.cfg)
        cfg["bb"] = (0, 0, w, h)
        self.leaves = L()
        self.bordered_leaves = L()

        self.parse_children(node=cfg)
        return self.im, self.leaves

    def show(self, texts=None, **kwargs):
        if texts is not None and texts != "ixs":
            texts = self.leaves.map(lambda l: l.get(texts, ""))

        show(self.im, bbs=self.leaves.map(lambda l: l.bb), texts=texts, **kwargs)

    def parse_children(self, node):
        _split = self.splits.index(node.split)
        x, y, X, Y = node.bb
        W, H = X - x, Y - y

        if "b" in node:
            self.bordered_leaves.append(node)

        if "children" not in node or node.children == L([]):
            del node.split
            if "height" in node:
                del node.height
            if "width" in node:
                del node.width
            node.shape = node.bb.h, node.bb.w
            self.leaves.append(node)
            return

        head = 0
        if (
            ("shufflable_children" in node)
            and node.shufflable_children
            and self.shuffle_children
        ):
            # memorize position of fixed elements
            items = node.children
            og = node.children.map(lambda x: x.split)
            if "fix_children" in node:
                fix_children = set(node.fix_children)
                fixed = [
                    (pos, item)
                    for (pos, item) in enumerate(node.children)
                    if pos in fix_children
                ]
            else:
                fix_children = set()
                fixed = []
            # shuffle list
            np.random.shuffle(node.children)
            # swap fixed elements back to their original position
            for pos, item in fixed:
                index = node.children.index(item)
                node.children[pos], node.children[index] = (
                    node.children[index],
                    node.children[pos],
                )
            nw = node.children.map(lambda x: x.split)
            for i in fix_children:
                assert og[i] == nw[i]

        for ix, child in enumerate(node.children):
            child.split = self.splits[(1 - _split)]
            var = self.vars[(1 - _split)]

            if self.noisy:
                delta = child[var] * (1 + np.random.uniform(-0.1, 0.1))
            else:
                delta = child[var]

            if var == "height":
                a, b, A, B = x, y + int(head * H), X, y + int((head + delta) * H)
                if ix == len(node.children) - 1:
                    B = Y - 2

            if var == "width":
                a, b, A, B = x + int(head * W), y, x + int((head + delta) * W), Y
                if ix == len(node.children) - 1:
                    A = X - 2

            head += delta
            child.bb = BB(a, b, A, B)

        for child in node.children:
            self.parse_children(child)

    def draw_borders(self, th=2):
        im = np.array(self.im)
        for leaf in self.leaves:
            bb = leaf.bb
            rect(im, bb, c=(0, 0, 0), th=th)
        self.im = Image.fromarray(im)

    def get(self, id):
        """Return a region by its `id` and None if `id` is not found"""
        return self.leaves.get(lambda x: x.id == id)


if __name__ == "__main__":
    page = construct_page(
        H(0.05, id="tax-invoice"),
        H(0.15, [V(0.4), V(-1)]),
        H(0.15, [V(0.4), V(-1)]),
        H(0.05),
        H(0.3),
        H(0.15, [V(0.6), V(-1)]),
        H(0.15, [V(0.6), V(-1)]),
    )
    page.generate(1000, 800)
    page.show(texts="id")
