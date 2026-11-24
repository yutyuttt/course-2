import pytest

from function import equal_sum_partitions, two_largest


@pytest.mark.parametrize("lst, expected", [
    ([1, 5, 3, 9, 2], (9, 5)),
    ([100, 40, 75, 75, 20], (100, 75)),
    ([9, 8, 7, 6], (9, 8)),
    ([1, 1, 1], (1, 1)),
    ([5, 5], (5, 5)),
    ([-10, -1, -5, -3], (-1, -3)),
    (["apple", "banana", "cherry", "date"], ("date", "cherry")),
    (["same", "same"], ("same", "same")),
    (["zebra", "ant", "middle", "zebra"], ("zebra", "zebra")),
    (["Zoo", "apple", "Banana"], ("apple", "Zoo")),
    ("hello", ("o", "l")),
    ("abba", ("b", "b")),
])
def test_two_largest(lst, expected):
    assert two_largest(lst) == expected


@pytest.mark.parametrize("lst", [[], [42], ["only"], "z", "", " "])
def test_two_largest_requires_at_least_two_elements(lst):
    assert two_largest(lst) == "List must contain at least two elements."


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([], []),
        ([5], [[[5]]]),
        ([1, 1, 1, 1], [[[1, 1, 1, 1]], [[1, 1], [1, 1]], [[1], [1], [1], [1]]]),
        ([2, -2, 2, -2], [[[2, -2, 2, -2]], [[2, -2], [2, -2]]]),
        ([0, 0], [[[0, 0]], [[0], [0]]]),
        ([1, 0, 1], [[[1, 0, 1]], [[1], [0, 1]], [[1, 0], [1]]]),
        (
            [0, 1, -1, 0],
            [
                [[0, 1, -1, 0]],
                [[0], [1, -1, 0]],
                [[0, 1, -1], [0]],
                [[0], [1, -1], [0]],
            ],
        ),
        ([2, 3], [[[2, 3]]]),
    ],
)
def test_equal_sum_partitions(lst, expected):
    assert equal_sum_partitions(lst) == expected
