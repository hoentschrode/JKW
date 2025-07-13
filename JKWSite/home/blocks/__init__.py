from .content import LinkBlock
from .layout import GridBlock, SwiperBlock
from .html import RichTextBlock

HTML_BLOCKS = [("text", RichTextBlock())]

CONTENT_BLOCKS = HTML_BLOCKS + [("link", LinkBlock())]

LAYOUT_BLOCKS = [("row", GridBlock()), ("swiper", SwiperBlock())]
