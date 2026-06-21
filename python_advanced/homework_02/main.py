from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator, model_validator


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., gt=0)


class User(BaseModel):
    name: str = Field(..., min_length=2)
    age: int
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty")

        parts = value.split()

        if not all(part.isalpha() for part in parts):
            raise ValueError("Name must contain only letters and spaces")

        return " ".join(parts)

    @field_validator("age")
    @classmethod
    def validate_age(cls, age: int) -> int:
        if not 0 < age <= 120:
            raise ValueError("Age must be in range 0 and 120")

        return age

    @model_validator(mode="after")
    def validate_employment_age(self):
        if self.is_employed and not 18 <= self.age <= 65:
            raise ValueError("If user is employed, age must be between 18 and 65")

        return self


json_file = """{
    "name": "John Doe",
    "age": 54,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""


def validate_user_json(json_input: str) -> str | None:
    try:
        user = User.model_validate_json(json_input, strict=True)
        return user.model_dump_json()
    except ValidationError as e:
        print("Validation error:", e)
        return None


valid_user = """{
    "name": "John Doe",
    "age": 54,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""

invalid_age_employed = """{
    "name": "John Doe",
    "age": 17,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""

invalid_email = """{
    "name": "John Doe",
    "age": 25,
    "email": "wrong-email",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""

invalid_house_number = """{
    "name": "John Doe",
    "age": 25,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": -5
    }
}"""

invalid_name = """{
    "name": "John123",
    "age": 25,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""

test_jsons = [
    valid_user,
    invalid_age_employed,
    invalid_email,
    invalid_house_number,
    invalid_name,
]

for test in test_jsons:
    print(validate_user_json(test))
    print("-" * 50)
