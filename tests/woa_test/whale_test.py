

import numpy as np
import pytest

from swarmlib.woa.whale import Whale

# pylint: disable=unused-variable


@pytest.fixture
def test_func():
    return lambda x: np.sum(x)  # pylint: disable=unnecessary-lambda


@pytest.fixture
def test_object(test_func):
    return Whale(
        function=test_func,
        bit_generator=np.random.default_rng(3),
        iteration_number=10)


def describe_whale():
    def describe_constructor():
        def describe_raise_error():
            def if_iteration_number_is_missing(test_func):
                with pytest.raises(KeyError):
                    Whale(function=test_func, bit_generator=np.random.default_rng(3))

        def initializes_correctly(test_object):
            np.testing.assert_array_equal(test_object.position, [0.34259666857449744, 0.9472420263843988])
            np.testing.assert_equal(test_object.value, 1.2898386949588962)

    def describe_step():
        def describe_attack_prey():
            def updates_position_correctly(test_object, test_func):
                best = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(7),
                    iteration_number=10)
                random = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(5),
                    iteration_number=10)
                test_object = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(3),  # rng with start 3 triggers attacking
                    iteration_number=10,
                    b=-1)
                # rng with start 3 triggers attacking
                test_object.step(best, random)

                np.testing.assert_array_equal(test_object.position, [0.4808914501845343, 1.494525117648736])
                np.testing.assert_equal(test_object.value, 1.9754165678332702)

        def describe_encircle_prey():
            def updates_position_correctly(test_object, test_func):
                best = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(6),
                    iteration_number=10)
                random = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(5),
                    iteration_number=10)
                test_object = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(1),  # rng with start 1 triggers searching
                    iteration_number=10,
                    a=0.1)

                test_object.step(best, random)

                np.testing.assert_array_equal(test_object.position, [1.8313140463093407, 1.5078584439028677])
                np.testing.assert_equal(test_object.value, 3.339172490212208)


        def describe_search_prey():
            def updates_position_correctly(test_object, test_func):
                best = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(6),
                    iteration_number=10)
                random = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(2),
                    iteration_number=10)
                test_object = Whale(
                    function=test_func,
                    bit_generator=np.random.default_rng(0),  # rng with start 0 triggers searching (in combination with a=1)
                    iteration_number=10,
                    lower_boundary=-1,
                    a=1)

                test_object.step(best, random)

                np.testing.assert_array_equal(test_object.position, [3.634068919497446, -0.4827071779367993])
                np.testing.assert_equal(test_object.value, 3.1513617415606463)
