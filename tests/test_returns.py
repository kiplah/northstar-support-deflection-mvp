from Backend.services.return_services import check_return_eligibility, load_return_policies


def test_load_return_policies_has_categories():
    policies = load_return_policies()
    assert len(policies) >= 5
    assert all("category" in policy and "return_window_days" in policy for policy in policies)


def test_check_return_eligibility_for_electronics():
    result = check_return_eligibility("Electronics", "Defective")
    assert result["eligible"] is True
    assert "refund" in result["next_step"].lower()


def test_check_return_eligibility_rejects_unsupported_reason():
    result = check_return_eligibility("Software", "Changed mind")
    assert result["eligible"] is False
