from unittest import TestCase
from unittest import main
from blogging.blog import Blog
from datetime import datetime, date

class BlogTester(TestCase):
    def setup(self):
           self.blog = Blog

    def test_blog_class(self):
            expected_blog_1 = Blog(1111114444, "Short Journey", "short_journey", "short.journey@gmail.com")
            expected_blog_2 = Blog(1111115555, "Long Journey", "long_journey", "long.journey@gmail.com")
            expected_blog_3 = Blog(1111112000, "Long Trip", "long_trip", "long.trip@gmail.com")
            expected_blog_4 = Blog(1111112000, "Long Trip", "long_trip", "long.trip@gmail.com")
            expected_post_5 = expected_blog_1.add_post("Fourth step", "When less expected,\nAll worked fine.")

            self.assertEqual(datetime.now().date(), expected_post_5.creation.date(), "Testing creation time")

            self.assertEqual(len(expected_blog_1.posts), 1, "Testing add post") # add a post to a blog

            self.assertTrue(expected_blog_3 == expected_blog_4, "Testing if 2 blogs are equal")
            self.assertFalse(expected_blog_1 == expected_blog_2, "Testing if 2 blogs are not equal")

            self.assertEqual("ID Number: 1111114444. Name: Short Journey. URL: short_journey. Email: short.journey@gmail.com.", str(expected_blog_1), "Testing str function")
            self.assertEqual("ID Number: 1111114444. Name: Short Journey. URL: short_journey. Email: short.journey@gmail.com.",repr(expected_blog_1), "Testing repr function")

if __name__ == '__main__':
	unittest.main()