"""The Decorator pattern is used to dynamically add a new features/functionalities
to an object without changing its implementation. It differs from inheritance because
the new functionalities are attached to that particular object on-demand,
not to the entire subclass."""

class HashTag: # pylint: disable=too-few-public-methods
    """Represents a hash tag text."""

    def __init__(self, text):
        """A HastTag is a simple text string."""
        self._text = text

    def render(self):
        """This function represents a text rending in html format."""
        return self._text

    # def len(self):
    #     """Just in case if we want to know the lenght."""
    #     return len(self._text)


class BoldWrapper(HashTag): # pylint: disable=too-few-public-methods
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        super().__init__(self)
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(HashTag): # pylint: disable=too-few-public-methods
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        super().__init__(self)
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"

def main():
    """This main function implements a test example run of this decorator pattern implementation"""
    simple_hello = HashTag("#helloWorld!")

    bold_hello = BoldWrapper(simple_hello)

    italic_and_bold_hello = ItalicWrapper(bold_hello)

    print("before: ", simple_hello.render())

    print("after: ", bold_hello.render())
    print("after: ", italic_and_bold_hello.render())



if __name__ == "__main__":
    main()
    