
import unittest
from html.parser import HTMLParser


class FormChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = []
        self.input_types = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)

        if "id" in attrs:
            self.ids.append(attrs["id"])

        if tag == "input":
            self.input_types.append(attrs.get("type", ""))


class TestRegistrationForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("index.html", encoding="utf-8") as file:
            cls.html = file.read()

        cls.parser = FormChecker()
        cls.parser.feed(cls.html)

    def test_form_exists(self):
        self.assertIn("form", self.parser.tags)

    def test_student_name(self):
        self.assertIn("name", self.parser.ids)

    def test_roll_number(self):
        self.assertIn("roll", self.parser.ids)

    def test_email(self):
        self.assertIn("email", self.parser.ids)
        self.assertIn("email", self.parser.input_types)

    def test_course(self):
        self.assertIn("course", self.parser.ids)

    def test_submit_button(self):
        self.assertIn("button", self.parser.tags)
        self.assertIn('type="submit"', self.html.lower())


if __name__ == "__main__":
    unittest.main()
