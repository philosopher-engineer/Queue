import unittest
import queue


class QueueOperationsTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = queue.Queue()

    def tearDown(self):
        self.queue = None

    def test_default_length(self):
        self.assertEqual(self.queue.length(), 0)  # add assertion here
        self.assertEqual(self.queue.is_empty(), True)

    def test_remove_from_empty(self):
        self.assertEqual(self.queue.remove(), -1)

    def test_add_remove(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.assertEqual(self.queue.remove(), 1)
        self.assertEqual(self.queue.remove(), 2)
        self.assertEqual(self.queue.remove(), 3)

    def test_peek(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.remove(), 1)
        self.assertEqual(self.queue.remove(), 2)

    def test_length(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.assertEqual(self.queue.remove(), 1)
        self.assertEqual(self.queue.remove(), 2)
        self.assertEqual(self.queue.length(), 1)

    def test_is_empty(self):
        self.queue.add(1)
        self.queue.add(2)
        self.assertEqual(self.queue.remove(), 1)
        self.assertEqual(self.queue.is_empty(), False)
        self.assertEqual(self.queue.remove(), 2)
        self.assertEqual(self.queue.is_empty(), True)


if __name__ == '__main__':
    unittest.main()
