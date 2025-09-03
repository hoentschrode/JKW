from .html import HeadingBlock, RichTextBlock
from .content import CarouselBlock, FlyerSwiperBlock, HeroBlock, LinkBlock
from .layout import GridBlock

HTML_BLOCKS = [("text", RichTextBlock()), ("heading", HeadingBlock())]

CONTENT_BLOCKS = HTML_BLOCKS + [
    ("link", LinkBlock()),
    ("row", GridBlock()),
    ("flyer_swiper", FlyerSwiperBlock()),
    ("carousel", CarouselBlock()),
]

LAYOUT_BLOCKS = [
    ("row", GridBlock(CONTENT_BLOCKS)),
    ("hero", HeroBlock([("row", GridBlock(CONTENT_BLOCKS))])),
]
