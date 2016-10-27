# Testcases for [vfmd]

This repository hold testcases for verifying whether an implementation
of [vfmd] \(that outputs HTML\) confirms to the [vfmd specification].


[vfmd]: http://vfmd.github.io/
[vfmd specification]: http://vfmd.github.io/vfmd-spec/specification/

## Organization

The tests are organized in a folder/subfolder hierarchy, for e.g.
`block_level/blockquote`, `span_level/emphasis`, with test `.md` files
placed in the subfolders.

  * **Block-level elements:** Each subfolder contains tests for how the
    block-level element is parsed when standalone, and when intermingled
    with other blocks (i.e. followed by other blocks, containing other
    blocks, text that looks similar to other blocks, etc.).
      * Paragraph
      * atx-style header
      * setext header
      * Code block
      * Blockquote
      * Unordered list
      * Ordered list
      * Horizontal rule
  * **Span-level elements:**  Each subfolder contains tests for how the
    span-level element is parsed when standalone, and when intermingled
    with other spans.
      * Link
      * Emphasis
      * Code span
      * Image
      * Automatic links
  * **Text processing**
      * UTF-8: Tests for handling of multibyte UTF-8 sequences
      * UTF-8 BOM: Tests for handling of the leading byte-order-mark in
        UTF-8
  * **Mixing HTML with vfmd**
      * Verbatim container elements: Tests for including `pre`, `style`
        and `script` elements in vfmd.

## Running tests

To run the tests, you need an executable command that reads Markdown
from `stdin` and outputs XHTML to `stdout`. Assuming that command is
at `/path/to/vfmd_impl`, you can say:

    ./run_tests /path/to/vfmd_impl

You can also run specific tests from specific subfolders.

    # Test just ordered and unordered lists
    ./run_tests vfmd_impl --dir="block_level/*list"

    # Run all tests involving ref links
    ./run_tests vfmd_impl --dir="tests/span_level/*" --testcase="*ref_link*"

## TODO

Per my assessment, the following tests are required to complete the test
suite, but I have not managed to write them myself yet:

  * **Text processing**
      * [HTML text escaping](http://www.vfmd.org/vfmd-spec/specification/#html-text-escaping)
      * [Backslash escaping](http://www.vfmd.org/vfmd-spec/syntax/#backslash-escapes)
      * [Hard line-breaks](http://www.vfmd.org/vfmd-spec/syntax/#paragraphs)
      * Handling of tabs
  * **Mixing HTML with vfmd**
      * Verbatim starter elements: Tests for blocks treated as
        [verbatim HTML](http://www.vfmd.org/vfmd-spec/syntax/#verbatim-html)
        because of a
        [verbatim HTML starter element](http://www.vfmd.org/vfmd-spec/syntax/#verbatim-html-starter-elements)
        \(like `div` or `table`\).
      * Other elements: Test that
        [other HTML elements](http://www.vfmd.org/vfmd-spec/syntax/#other-html-elements)
          * can contain vfmd span constructs
          * cannot be contained by vfmd span constructs
          * occurring in paragraphs make those paragraphs be output without
            `p` tags

    Please note that it is not necessary to include all relevant HTML
    elements in the above tests - just a few candidate elements should
    suffice.

    There is no need to have a test subfolder for [phrasing HTML
    elements](http://www.vfmd.org/vfmd-spec/syntax/#phrasing-html-elements)
    because that's already covered under the other span-level tests (in
    the `tests/span_level/*/vs_html.md` files).

## Contributions

I'll be glad to receive tests from contributors that augument the
current set of tests, whether it's a TODO item listed above or not.

If you have any questions, please [contact
me](http://www.vfmd.org/introduction#contact) or open [an
issue](https://github.com/vfmd/vfmd-test/issues).

---
