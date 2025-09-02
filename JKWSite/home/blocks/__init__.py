from .content import CarouselBlock, FlyerSwiperBlock, HeroBlock, LinkBlock
from .layout import GridBlock
from .html import HeadingBlock, RichTextBlock

HTML_BLOCKS = [("text", RichTextBlock()), ("heading", HeadingBlock())]

CONTENT_BLOCKS = HTML_BLOCKS + [
    ("link", LinkBlock()),
    ("row", GridBlock()),
]

LAYOUT_BLOCKS = [
    ("row", GridBlock()),
    ("flyer_swiper", FlyerSwiperBlock()),
    ("carousel", CarouselBlock()),
    ("hero", HeroBlock()),
]
