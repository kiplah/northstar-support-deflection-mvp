import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "return_policies.json"


def load_return_policies():
    """Load return policies from the JSON dataset."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def check_return_eligibility(category, reason):
    """
    Check whether an item is eligible for return.

    Returns:
        A dictionary containing eligibility and the next step.
    """

    policies = load_return_policies()

    category = category.strip().lower()
    reason = reason.strip().lower()

    for policy in policies:

        if policy["category"].lower() == category:

            allowed_reasons = [
                item.lower()
                for item in policy["reasons_allowed"]
            ]

            if reason in allowed_reasons:
                return {
                    "eligible": True,
                    "message": "Item is eligible for return.",
                    "next_step": (
                        "Start the return process. "
                        f"Refund will be issued through "
                        f"{policy['refund_method']}."
                    )
                }

            return {
                "eligible": False,
                "message": "This reason is not covered by the return policy.",
                "next_step": "Contact Northstar Support for assistance."
            }

    return {
        "eligible": False,
        "message": "We could not find a return policy for this category.",
        "next_step": "Contact Northstar Support for assistance."
    }