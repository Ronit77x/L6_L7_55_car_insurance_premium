
import pytest

from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout
)


# ---------------- ANNUAL PREMIUM ----------------

def test_invalid_car_type():
    with pytest.raises(ValueError):
        annual_premium("truck", 30, 1, False)


def test_driver_too_young():
    with pytest.raises(ValueError):
        annual_premium("sedan", 17, 1, False)


def test_age_below_25():
    assert annual_premium("hatchback", 20, 1, False) == 12000


def test_age_between_25_and_59():
    assert annual_premium("sedan", 30, 1, False) == 12000


def test_age_60_or_above():
    assert annual_premium("suv", 60, 1, False) == 17000


def test_zero_claims():
    assert annual_premium("sedan", 30, 0, False) == 9600


def test_claims_one_or_two():
    assert annual_premium("sedan", 30, 2, False) == 12000


def test_claims_more_than_two():
    assert annual_premium("sedan", 30, 3, False) == 24000


def test_anti_theft_enabled():
    assert annual_premium("sedan", 30, 1, True) == 11500


def test_anti_theft_disabled():
    assert annual_premium("sedan", 30, 1, False) == 12000


# ---------------- NO CLAIM BONUS ----------------

def test_negative_years():
    with pytest.raises(ValueError):
        no_claim_bonus(-1)


def test_five_or_more_years():
    assert no_claim_bonus(5) == 50


def test_three_or_four_years():
    assert no_claim_bonus(3) == 35


def test_one_or_two_years():
    assert no_claim_bonus(1) == 20


def test_zero_years():
    assert no_claim_bonus(0) == 0


# ---------------- CLAIM PAYOUT ----------------

def test_negative_damage():
    with pytest.raises(ValueError):
        claim_payout(-100, 50000, 1000, False)


def test_negative_deductible():
    with pytest.raises(ValueError):
        claim_payout(5000, 50000, -1000, False)


def test_valid_amounts():
    assert claim_payout(10000, 50000, 1000, False) == 9000


def test_total_loss():
    assert claim_payout(40000, 50000, 1000, True) == 50000


def test_not_total_loss():
    assert claim_payout(10000, 50000, 1000, False) == 9000


def test_damage_equal_to_deductible():
    assert claim_payout(1000, 50000, 1000, False) == 0


def test_damage_below_deductible():
    assert claim_payout(500, 50000, 1000, False) == 0


def test_payout_exceeds_insured_value():
    assert claim_payout(60000, 50000, 1000, False) == 50000


def test_payout_does_not_exceed_insured_value():
    assert claim_payout(10000, 50000, 1000, False) == 9000
