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

---
