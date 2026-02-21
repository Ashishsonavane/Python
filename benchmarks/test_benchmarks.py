"""Benchmarks for sorting and searching algorithms using pytest-codspeed."""

import random

import pytest

from searches.binary_search import binary_search, binary_search_by_recursion
from sorts.bubble_sort import bubble_sort_iterative
from sorts.heap_sort import heap_sort
from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.selection_sort import selection_sort


def _random_list(size: int, seed: int = 42) -> list[int]:
    rng = random.Random(seed)
    return rng.sample(range(-size, size), size)


# -- Sorting benchmarks --


@pytest.mark.benchmark
def test_bubble_sort() -> None:
    data = _random_list(500)
    bubble_sort_iterative(data)


@pytest.mark.benchmark
def test_heap_sort() -> None:
    data = _random_list(5000)
    heap_sort(data)


@pytest.mark.benchmark
def test_insertion_sort() -> None:
    data = _random_list(500)
    insertion_sort(data)


@pytest.mark.benchmark
def test_merge_sort() -> None:
    data = _random_list(5000)
    merge_sort(data)


@pytest.mark.benchmark
def test_quick_sort() -> None:
    data = _random_list(5000)
    quick_sort(data)


@pytest.mark.benchmark
def test_selection_sort() -> None:
    data = _random_list(500)
    selection_sort(data)


# -- Search benchmarks --


@pytest.mark.benchmark
def test_binary_search() -> None:
    data = sorted(range(10000))
    binary_search(data, 4999)


@pytest.mark.benchmark
def test_binary_search_recursive() -> None:
    data = sorted(range(10000))
    binary_search_by_recursion(data, 4999, 0, len(data) - 1)
