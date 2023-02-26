import pytest

from chatgpt import spellout as chatgpt_spellout
from copilot import spellout as copilot_spellout
from spellout import spellout as solution_spellout


TEST_FUNCTIONS = [
    ('chatgpt', chatgpt_spellout),
    ('copilot', copilot_spellout),
    ('solution', solution_spellout)
]

def _good_test(name, spellout, input, expected):
    result = spellout(input)
    assert result == expected, f'Failed for {name}({input}): {result} != {expected}'


@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
def test_spellout_zero(name, spellout):
    assert spellout(0) == 'zero'


@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (1, 'one'),
    (5, 'five'),
    (7, 'seven'),
])
def test_spellout_single_digit(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)


@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (10, 'ten'),
    (11, 'eleven'),
    (17, 'seventeen'),
])
def test_spellout_two_digit_const(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)


@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (20, 'twenty'),
    (30, 'thirty'),
    (90, 'ninety'),
])
def test_spellout_two_digit_multiples_of_ten(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)


@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (22, 'twenty-two'),
    (45, 'forty-five'),
    (88, 'eighty-eight'),
])
def test_spellout_two_digits(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)


@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (100, 'one hundred'),
    (101, 'one hundred one'),
    (234, 'two hundred thirty-four'),
    (789, 'seven hundred eighty-nine'),
])
def test_spellout_three_digits(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)

@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (10**0, 'one'),
    (10**3, 'one thousand'),
    (10**6, 'one million'),
    (10**9, 'one billion'),
])
def test_spellout_large_numbers(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)

@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (10**12 - 1, 'nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine'),
])
def test_spellout_edge(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)


@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (4, 'four'),
    (42, 'forty-two'),
    (123, 'one hundred twenty-three'),
    (1024, 'one thousand twenty-four'),
    (54783, 'fifty-four thousand seven hundred eighty-three'),
    (672824, 'six hundred seventy-two thousand eight hundred twenty-four'),
    (2498403, 'two million four hundred ninety-eight thousand four hundred three'),
    (19056205, 'nineteen million fifty-six thousand two hundred five'),
    (887200572, 'eight hundred eighty-seven million two hundred thousand five hundred seventy-two'),
    (7942065119, 'seven billion nine hundred forty-two million sixty-five thousand one hundred nineteen'),
    (36014751056, 'thirty-six billion fourteen million seven hundred fifty-one thousand fifty-six'),
    (117842886724, 'one hundred seventeen billion eight hundred forty-two million eight hundred eighty-six thousand seven hundred twenty-four'),
])
def test_spellout_random_numbers(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)

@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input,expected', [
    (0, 'zero'),
    (100, 'one hundred'),
    (500, 'five hundred'),
    (1000, 'one thousand'),
    (1100, 'one thousand one hundred'),
    (1000222, 'one million two hundred twenty-two'),
    (1222000, 'one million two hundred twenty-two thousand'),
    (9000000222, 'nine billion two hundred twenty-two'),
    (9000222000, 'nine billion two hundred twenty-two thousand'),
    (9222000000, 'nine billion two hundred twenty-two million'),
])
def test_spellout_empty_chunks(name, spellout, input, expected):
    _good_test(name, spellout, input, expected)


@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input', [
    -1,
    -123,
])
def test_spellout_negative(name, spellout, input):
    with pytest.raises(ValueError):
        spellout(input)

@pytest.mark.parametrize('name,spellout', TEST_FUNCTIONS)
@pytest.mark.parametrize('input', [
    10**12,
    10**12 + 1,
    10 ** 30
])
def test_spellout_out_of_range(name, spellout, input):
    with pytest.raises(ValueError):
        spellout(input)
