import pytest
from delivery_cost import delivery_cost

table = [
    (0, 1.6, 'Big', True, "Invalid 'km' value!"),
    (0, 1.4, 'Small', False, "Invalid 'km' value!"),
    (0, 1.2, 'Big', True, "Invalid 'km' value!"),
    (0, 1, 'Small', False, "Invalid 'km' value!"),
    (1, 1.4, 'Small', True, 630),
    (1, 1.2, 'Big', False, 400),
    (1, 1, 'Small', True, 450),
    (1, 1.6, 'Big', False, 400),
    (2, 1.2, 'Big', True, 660),
    (2, 1, 'Small', False, 400),
    (2, 1.6, 'Big', True, 880),
    (2, 1.4, 'Small', False, 400),
    (3, 1, 'Small', True, 500),
    (3, 1.6, 'Big', False, 480),
    (3, 1.4, 'Small', True, 700),
    (3, 1.2, 'Big', False, 400),
    (10, 1.6, 'Big', True, 960),
    (10, 1.4, 'Small', False, 400),
    (10, 1.2, 'Big', True, 720),
    (10, 1, 'Small', False, 400),
    (11, 1.4, 'Small', True, 840),
    (11, 1.2, 'Big', False, 480),
    (11, 1, 'Small', True, 600),
    (11, 1.6, 'Big', False, 640),
    (30, 1.2, 'Big', True, 840),
    (30, 1, 'Small', False, 400),
    (30, 1.6, 'Big', True, 1120),
    (30, 1.4, 'Small', False, 420),
    (31, 1, 'Small', True, "Can't deliver fragile orders more than 30 km"),
    (31, 1.6, 'Big', False, 800),
    (31, 1.4, 'Small', True, "Can't deliver fragile orders more than 30 km"),
    (31, 1.2, 'Big', False, 600)
]


class TestDeliveryCost:
    @pytest.mark.parametrize("km, sur, size, frag, result", table)
    def test_delivery_cost(self, km, sur, size, frag, result):
        assert delivery_cost(km, sur, size, frag) == result
