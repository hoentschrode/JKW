from .content import FlyerSwiperBlock, LinkBlock
from .layout import GridBlock, SwiperBlock
from .html import HeadingBlock, RichTextBlock

HTML_BLOCKS = [("text", RichTextBlock()), ("heading", HeadingBlock())]

CONTENT_BLOCKS = HTML_BLOCKS + [("link", LinkBlock()), ("row", GridBlock())]

LAYOUT_BLOCKS = [
    ("row", GridBlock()),
    ("swiper", SwiperBlock()),
    ("flyer_swiper", FlyerSwiperBlock()),
]
