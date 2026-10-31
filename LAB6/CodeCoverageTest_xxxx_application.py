
import pytest

from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout
)


# ---------------- ANNUAL PREMIUM TESTS ----------------

def test_invalid_car_type():
    with pytest.raises(ValueError, match="unknown car type"):
        annual_premium("truck", 30, 0, False)


def test_driver_below_18():
    with pytest.raises(ValueError, match="driver too young"):
        annual_premium("sedan", 17, 0, False)


def test_young_driver():
    assert annual_premium("hatchback", 20, 1, False) == 12000


def test_middle_aged_driver():
    assert annual_premium("sedan", 30, 1, False) == 12000


def test_senior_driver():
    assert annual_premium("suv", 65, 1, False) == 17000


def test_zero_claims_discount():
    assert annual_premium("sedan", 30, 0, False) == 9600


def test_one_claim():
    assert annual_premium("sedan", 30, 1, False) == 12000


def test_two_claims():
    assert annual_premium("sedan", 30, 2, False) == 12000


def test_more_than_two_claims():
    assert annual_premium("sedan", 30, 3, False) == 24000


def test_anti_theft_discount():
    assert annual_premium("sedan", 30, 1, True) == 11500


def test_anti_theft_with_claim_discount():
    assert annual_premium("sedan", 30, 0, True) == 9100


# ---------------- NO CLAIM BONUS TESTS ----------------

def test_negative_claim_free_years():
    with pytest.raises(ValueError, match="invalid years"):
        no_claim_bonus(-1)


def test_zero_claim_free_years():
    assert no_claim_bonus(0) == 0


def test_one_claim_free_year():
    assert no_claim_bonus(1) == 20


def test_two_claim_free_years():
    assert no_claim_bonus(2) == 20


def test_three_claim_free_years():
    assert no_claim_bonus(3) == 35


def test_four_claim_free_years():
    assert no_claim_bonus(4) == 35


def test_five_claim_free_years():
    assert no_claim_bonus(5) == 50


def test_more_than_five_claim_free_years():
    assert no_claim_bonus(7) == 50


# ---------------- CLAIM PAYOUT TESTS ----------------

def test_negative_damage_cost():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(-100, 50000, 1000, False)


def test_negative_deductible():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(5000, 50000, -1000, False)


def test_total_loss():
    assert claim_payout(40000, 50000, 1000, True) == 50000


def test_damage_equal_to_deductible():
    assert claim_payout(1000, 50000, 1000, False) == 0


def test_damage_below_deductible():
    assert claim_payout(500, 50000, 1000, False) == 0


def test_payout_exceeds_insured_value():
    assert claim_payout(60000, 50000, 1000, False) == 50000


def test_normal_claim_payout():
    assert claim_payout(10000, 50000, 1000, False) == 9000


def test_payout_equal_to_insured_value():
    assert claim_payout(51000, 50000, 1000, False) == 50000
