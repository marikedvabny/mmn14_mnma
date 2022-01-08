from unittest import TestCase
from unittest import mock
from unittest.mock import patch

from main import run_sorted, run_unsorted, run_unsorted_unique

test_input_list = ['MakeHeap', 'Insert 8', 'Insert 9', 'Insert -1',
                   'MakeHeap', 'Insert 2', 'Insert 2',
                   'Insert -123123',
                   'Insert 8', 'Insert 9', 'Insert 9999999',
                   'MakeHeap', 'Insert 223', 'Insert -223232', 'Insert 0',
                   'Insert 55555555', 'Insert 123123', 'Insert 123123123',
                   'Insert 7845912', 'Insert 321', 'Insert 123',
                   'Union', 'ExtractMin', 'exit', 'exit'
                   ]

test_input_list_2 = ['MakeHeap', 'Insert -123', 'Insert -122', 'Insert -121',
                     'MakeHeap', 'Insert 2', 'Insert 2',
                     'Insert -123123',
                     'Insert 8', 'Insert 9', 'Insert 9999999',
                     'Union', 'ExtractMin', 'ExtractMin', 'ExtractMin',
                     'MakeHeap', 'Insert 223', 'Insert -223232', 'Insert 0',
                     'Insert 55555555', 'Insert 123123', 'Insert 123123123',
                     'Insert 7845912', 'Insert 321', 'Insert 123',
                     'MakeHeap', 'Insert 223', 'Insert -223232', 'Insert 0',
                     'Insert 55555555', 'Insert 123123', 'Insert 123123123',
                     'Insert 7845912', 'Insert 321', 'Insert 123',
                     'Insert 223', 'Insert -223232', 'Insert 0',
                     'Insert 55555555', 'Insert 123123', 'Insert 123123123',
                     'Insert 7845912', 'Insert 321', 'Insert 123',
                     'Union',
                     'ExtractMin', 'exit', 'exit'
                     ]


class Test(TestCase):
    @patch('main.input', create=True)
    def test_run_sorted(self, mocked_input):
        mocked_input.side_effect = test_input_list
        result = run_sorted()

    @patch('main.input', create=True)
    def test_run_unsorted(self, mocked_input):
        mocked_input.side_effect = test_input_list
        result = run_unsorted()

    @patch('main.input', create=True)
    def test_run_unsorted_unique(self, mocked_input):
        mocked_input.side_effect = test_input_list
        result = run_unsorted_unique()

    @patch('main.input', create=True)
    def test_run_sorted_2(self, mocked_input):
        mocked_input.side_effect = test_input_list_2
        result = run_sorted()

    @patch('main.input', create=True)
    def test_run_unsorted_2(self, mocked_input):
        mocked_input.side_effect = test_input_list_2
        result = run_unsorted()

    @patch('main.input', create=True)
    def test_run_unsorted_unique_2(self, mocked_input):
        mocked_input.side_effect = test_input_list_2
        result = run_unsorted_unique()
