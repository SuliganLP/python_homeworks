from pydantic import BaseModel, ConfigDict, Field


class CategoryBase(BaseModel):
    name: str = Field(min_length=1, max_length=20)


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class QuestionBase(BaseModel):
    text: str = Field(min_length=1, max_length=100)


class QuestionCreate(QuestionBase):
    category_id: int


class QuestionResponse(QuestionBase):
    id: int
    category_id: int
    category: CategoryResponse | None = None

    model_config = ConfigDict(from_attributes=True)
