class HashTag:
    """Represents a hash tag text"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(HashTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(HashTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"

def main():
    simple_hello = HashTag("#helloWorld!")

    bold_hello = BoldWrapper(simple_hello)

    italic_and_bold_hello = ItalicWrapper(bold_hello)

    print("before: ", simple_hello.render())

    print("after: ", bold_hello.render())
    print("after: ", italic_and_bold_hello.render())



if __name__ == "__main__":
    main()
    