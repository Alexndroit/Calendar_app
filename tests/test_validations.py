from calendar_crud_app.schemas.customer import CustomerCreate
from calendar_crud_app.schemas.address import AddressCreate
from pydantic import ValidationError


def test_customer_email_validation():
    try:
        # Invalid email format
        CustomerCreate(name="John Doe", email="invalid-email", age=25)
    except ValidationError as e:
        # Check if the error message contains the expected substring
        assert "value is not a valid email address" in str(e), f"Unexpected error: {e}"


def test_address_zip_validation():
    try:
        # Invalid ZIP code (not numeric)
        AddressCreate(street="123 Main St", city="New York", zip_code="ABCDE")
    except ValidationError as e:
        # Check if the error message contains the expected substring
        assert "String should match pattern" in str(e), f"Unexpected error: {e}"


def test_valid_customer_creation():
    customer = CustomerCreate(name="John Doe", email="johndoe@example.com", age=25)
    assert customer.name == "John Doe"
    assert customer.email == "johndoe@example.com"
    assert customer.age == 25


def test_valid_address_creation():
    address = AddressCreate(street="123 Main St", city="New York", zip_code="10001")
    assert address.street == "123 Main St"
    assert address.city == "New York"
    assert address.zip_code == "10001"
