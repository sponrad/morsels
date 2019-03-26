import unittest

from markdownify import markdownify


class MarkdownifyTests(unittest.TestCase):

    """Tests for markdownify"""

    def test_text_with_linebreaks(self):
        html = "This text\nhas words over\nmultiple lines"
        text = "This text has words over multiple lines"
        self.assertEqual(markdownify(html), text)

    def test_single_paragraph(self):
        html = "<p>This text is in a paragraph</p>"
        text = "This text is in a paragraph"
        self.assertEqual(markdownify(html), text)

    def test_multiple_paragraphs(self):
        html = "<p>This text is in a paragraph</p><p>And so is this text</p>"
        text = "This text is in a paragraph\n\nAnd so is this text"
        self.assertEqual(markdownify(html), text)
        html = "<p>This paragraph has\nnewlines in it</p><p>This doesn't</p>"
        text = "This paragraph has newlines in it\n\nThis doesn't"
        self.assertEqual(markdownify(html), text)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_br_tags_converted(self):
        html = "This text<br>has breaks<br>in it"
        text = "This text  \nhas breaks  \nin it"
        self.assertEqual(markdownify(html), text)
        html = "<p>A paragraph with a<br>linebreak</p>"
        text = "A paragraph with a  \nlinebreak"
        self.assertEqual(markdownify(html), text)

    # To test the Bonus part of this exercise, comment out the following line
    #@unittest.expectedFailure
    def test_bolding(self):
        html = "This text contains <strong>bolding</strong>."
        text = "This text contains **bolding**."
        self.assertEqual(markdownify(html), text)
        html = "<strong>bolding</strong> and <strong>more bolding</strong>"
        text = "**bolding** and **more bolding**"
        self.assertEqual(markdownify(html), text)
        html = "<p>Some <strong>bolded text</strong></p><p>In a paragraph</p>"
        text = "Some **bolded text**\n\nIn a paragraph"
        self.assertEqual(markdownify(html), text)

    # To test the Bonus part of this exercise, comment out the following line
    #@unittest.expectedFailure
    def test_hyperlinks(self):
        html = '<a href="https://www.pythonmorsels.com">Python Morsels</a>'
        text = "[Python Morsels](https://www.pythonmorsels.com)"
        self.assertEqual(markdownify(html), text)
        html = (
            'link 1 <a href="http://trey.io">here</a> and '
            'link 2 <a href="http://pypi.io">there</a>!'
        )
        text = (
            'link 1 [here](http://trey.io) and link 2 [there](http://pypi.io)!'
        )
        self.assertEqual(markdownify(html), text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
