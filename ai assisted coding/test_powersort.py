import pytest

from powersort import powersort


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([3, 1, 2, 1], [1, 1, 2, 3]),
        ([-10, -1, -5, -3], [-10, -5, -3, -1]),
        (["banana", "apple", "cherry"], ["apple", "banana", "cherry"]),
    ],
)
def test_powersort_values(values, expected):
    result = powersort(values)

    assert result is values
    assert values == expected
    assert result == expected


def test_powersort_reverse():
    values = [3, 1, 4, 2]

    result = powersort(values, reverse=True)

    assert result == [4, 3, 2, 1]


def test_powersort_with_key():
    values = [{"name": "Banana", "size": 3}, {"name": "Apple", "size": 1}, {"name": "Cherry", "size": 2}]

    powersort(values, key=lambda item: item["size"])

    assert [item["name"] for item in values] == ["Apple", "Cherry", "Banana"]


def test_powersort_is_stable():
    values = [
        {"value": 2, "order": 1},
        {"value": 1, "order": 2},
        {"value": 2, "order": 3},
    ]

    powersort(values, key=lambda item: item["value"])

    assert [item["order"] for item in values] == [2, 1, 3]
