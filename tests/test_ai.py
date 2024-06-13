import pytest
import ai


def test_activation_functions():
    a = ai.ActivationFunction

    assert a.relu(2) == 2
    assert a.relu(-1) == 0
    assert a.relu(0) == 0

    assert a.sigmoid(0) == 0.5
    assert 0 < a.sigmoid(-1) < 0.5
    assert 0.5 < a.sigmoid(1) < 1

    assert a.tanh(0) == 0
    assert -1 < a.tanh(-1) < 0
    assert 0 < a.tanh(1) < 1
