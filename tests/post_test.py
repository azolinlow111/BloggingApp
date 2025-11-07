from unittest import TestCase
from unittest import main
from blogging.post import Post

class PostTester(TestCase):
    def setup(self):
         self.post = Post

    def test_post_class(self):
            expected_post_1 = Post(1, "Starting my journey", "Once upon a time\nThere was a kid...")
            expected_post_2 = Post(2, "Second step", "Before one could think,\nA storm stroke.")
            expected_post_3 = Post(3, "Continuing my journey", "Along the way...\nThere were challenges.")
            expected_post_4 = Post(4, "Fourth step", "When less expected,\nAll worked fine.")
            expected_post_5 = Post(4, "Fourth step", "When less expected,\nAll worked fine.")

            self.assertTrue(expected_post_4 == expected_post_5, "Testing if 2 posts are equal")
            self.assertFalse(expected_post_1 == expected_post_2, "Testing if 2 posts are not equal")

            self.assertEqual("Title: Starting my journey. Post Content: Once upon a time\nThere was a kid...", str(expected_post_1), "Testing str function")
            self.assertEqual("Integer Code: 1. Title: Starting my journey. Post Content: Once upon a time\nThere was a kid...", repr(expected_post_1), "Testing repr function")
            
if __name__ == '__main__':
    unittest.main()