import numpy as np
import pytest

from diffpy.snmf.containers import ComponentSignal

tas = [
    (
        [np.arange(10), 3, 0, [6.55, 0.357, 8.49, 9.33, 6.78, 7.57, 7.43, 3.92, 6.55, 1.71], 0.25],
        [
            [6.55, 6.78, 6.55, 0, 0, 0, 0, 0, 0, 0],
            [0, 14.07893122, 35.36478086, 0, 0, 0, 0, 0, 0, 0],
            [0, -19.92049156, 11.6931482, 0, 0, 0, 0, 0, 0, 0],
        ],
    ),
    (
        [np.arange(5), 10, 0, [-11.47, -10.688, -8.095, -29.44, 14.38], 1.25],
        [
            [-11.47, -10.8444, -9.1322, -16.633, -20.6760],
            [0, -0.50048, -3.31904, 40.9824, -112.1792],
            [0, 0.800768, 5.310464, -65.57184, 179.48672],
        ],
    ),
    (
        [np.arange(5), 2, 0, [-11.47, -10.688, -8.095, -29.44, 14.38], 0.88],
        [
            [-11.47, -10.3344, -13.9164, -11.5136, 0],
            [0, -3.3484, 55.1265, -169.7572, 0],
            [0, 7.609997, -125.2876, 385.81189, 0],
        ],
    ),
    (
        [np.arange(10), 1, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0.88],
        [
            [1, 2.1364, 3.2727, 4.4091, 5.5455, 6.6818, 7.8182, 8.9545, 0, 0],
            [0, -1.29, -2.58, -3.87, -5.165, -6.45, -7.74, -9.039, 0, 0],
            [0, 2.93, 5.869, 8.084, 11.739, 14.674, 17.608, 20.5437, 0, 0],
        ],
    ),
    (
        [
            np.arange(14),
            100,
            3,
            [
                -2.9384,
                -1.4623,
                -2.0913,
                4.6304,
                -1.2127,
                1.4737,
                -0.3791,
                1.7506,
                -1.5068,
                -2.7625,
                0.9617,
                -0.3494,
                -0.3862,
                2.7960,
            ],
            0.55,
        ],
        [
            [-2.9384, -1.9769, 0.9121, 0.6314, 0.8622, -2.4239, -0.2302, 1.9281, 0, 0, 0, 0, 0, 0],
            [0, 2.07933, 38.632, 18.3748, 43.07305, -61.557, 26.005, -73.637, 0, 0, 0, 0, 0, 0],
            [0, -7.56, -140.480, -66.81, -156.6293, 223.84, -94.564, 267.7734, 0, 0, 0, 0, 0, 0],
        ],
    ),
    (
        [np.arange(11), 20, 4, [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5], 0.987],
        [
            [0, 0.2533, 0.5066, 0.7599, 1.0132, 1.2665, 1.5198, 1.7730, 2.0263, 2.2796, 0],
            [0, -0.2566, -0.5132, -0.7699, -1.0265, -1.2831, -1.5398, -1.7964, -2.0530, -2.3097, 0],
            [0, 0.5200, 1.0400, 1.56005, 2.08007, 2.6000, 3.1201, 3.6401, 4.1601, 4.6801, 0],
        ],
    ),
    (
        [np.arange(9), 15, 3, [-1, -2, -3, -4, -5, -6, -7, -8, -9], -0.4],
        [[-1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],
    ),
]


@pytest.mark.parametrize("tas", tas)
def test_apply_stretch(tas):
    component = ComponentSignal(tas[0][0], tas[0][1], tas[0][2])
    component.iq = tas[0][3]
    component.stretching_factors[0] = tas[0][4]
    actual = component.apply_stretch(0)
    expected = tas[1]
    np.testing.assert_allclose(actual, expected, rtol=1e-01)


taw = [
    ([np.arange(5), 2, 0, [0, 1, 2, 3, 4], 0.5], [0, 0.5, 1, 1.5, 2]),
    ([np.arange(5), 20, 2, [0, -1, -2, -3, -4], 0.25], [0, -0.25, -0.5, -0.75, -1]),
    ([np.arange(40), 200, 4, np.arange(0, 10, 0.25), 0.3], np.arange(0, 10, 0.25) * 0.3),
    ([np.arange(1), 10, 2, [10.5, 11.5, -10.5], 0], [0, 0, 0]),
    ([[-12, -10, -15], 5, 2, [-0.5, -1, -1.2], 0.9], [-0.45, -0.9, -1.08]),
    ([[-12, -10, -15], 5, 2, [0, 0, 0], 0.9], [0, 0, 0]),
]


@pytest.mark.parametrize("taw", taw)
def test_apply_weight(taw):
    component = ComponentSignal(taw[0][0], taw[0][1], taw[0][2])
    component.iq = np.array(taw[0][3])
    component.weights[0] = taw[0][4]
    actual = component.apply_weight(0)
    expected = taw[1]
    np.testing.assert_allclose(actual, expected, rtol=1e-01)
