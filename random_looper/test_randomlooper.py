import unittest

from randomlooper import RandomLooper


class RandomLooperTests(unittest.TestCase):

    """Tests for RandomLooper."""

    def test_constructor(self):
        RandomLooper([1, 2, 3, 4])

    def test_empty_iterable(self):
        looper = RandomLooper(())
        self.assertEqual(list(looper), [])

    def test_one_item(self):
        looper = RandomLooper({1})
        self.assertEqual(list(looper), [1])

    def test_loop_once(self):
        looper = RandomLooper([1, 2, 3, 4])
        self.assertEqual(set(looper), {1, 2, 3, 4})

    def test_original_unchanged(self):
        numbers = [1, 2, 3, 4]
        looper = RandomLooper(numbers)
        list(looper)
        self.assertEqual(numbers, [1, 2, 3, 4])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_length(self):
        looper = RandomLooper(range(1000))
        self.assertEqual(len(looper), 1000)
        looper = RandomLooper('hello')
        self.assertEqual(len(looper), 5)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_accepts_multiple_iterables(self):
        self.assertEqual(
            set(RandomLooper([1, 2], 'hey')),
            {1, 2, 'h', 'e', 'y'},
        )
        fives = [5] * 1000
        threes = [3]
        many_first_items = [
            next(iter(RandomLooper(fives, threes)))
            for _ in range(100)
        ]
        three_count = len([
            item
            for item in many_first_items
            if item == 3
        ])
        self.assertLess(three_count, 15)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_looping_multiple_times(self):
        looper = RandomLooper(range(1000))
        loop1, loop2 = list(looper), list(looper)
        self.assertNotEqual(loop1, loop2)
        looper3 = RandomLooper([1, 2, 3])
        orders = {
            tuple(looper3)
            for _ in range(100)
        }
        self.assertEqual(orders, {
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
        })


if __name__ == "__main__":
    unittest.main(verbosity=2)
