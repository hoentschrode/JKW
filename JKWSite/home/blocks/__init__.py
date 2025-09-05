from .html import HeadingBlock, RichTextBlock
from .content import CarouselBlock, FlyerSwiperBlock, HeroBlock, LinkBlock
from .layout import GridBlock, RowBlock

HTML_BLOCKS = [("text", RichTextBlock()), ("heading", HeadingBlock())]

CONTENT_BLOCKS = HTML_BLOCKS + [
    ("link", LinkBlock()),
    ("carousel", CarouselBlock()),
]

LAYOUT_BLOCKS = [
    ("row", GridBlock(CONTENT_BLOCKS + [("row", RowBlock())])),
    ("hero", HeroBlock([("row", GridBlock(CONTENT_BLOCKS))])),
    ("flyer_swiper", FlyerSwiperBlock()),
]
