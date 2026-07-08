import unittest
from blocks import *


class TestBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
            

        def test_block_typing(self):
            md = """
This is a paragraph.

# This is a heading.

## Heading 2.

### Heading 3.

#### Heading 4.

##### Heading 5.

###### Heading 6.

```
This is code
```

> This is a quote
>block that keeps
> going

- Bullet points!
- We love unordered lists!
- because they are awesome

1. Ordered lists are better
2. Because they have numbers
3. And numbers are awesomer


"""
            blocks = markdown_to_blocks(md)
            type_list = []
            for item in blocks:
                 type_list.append(block_to_block_type(item))
            self.assertEqual(BlockType.PARAGRAPH, type_list[0])
            self.assertEqual(BlockType.HEADING1, type_list[1])
            self.assertEqual(BlockType.HEADING2, type_list[2])
            self.assertEqual(BlockType.HEADING3, type_list[3])
            self.assertEqual(BlockType.HEADING4, type_list[4])
            self.assertEqual(BlockType.HEADING5, type_list[5])
            self.assertEqual(BlockType.HEADING6, type_list[6])
            self.assertEqual(BlockType.CODE, type_list[7])
            self.assertEqual(BlockType.QUOTE, type_list[8])
            self.assertEqual(BlockType.U_LIST, type_list[9])
            self.assertEqual(BlockType.O_LIST, type_list[10])