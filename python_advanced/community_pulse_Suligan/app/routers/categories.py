from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from sqlalchemy import select
from app.models import db
from app.models.categories import Category
from app.models.questions import Question
from app.schemas.question import CategoryCreate, CategoryResponse


categories_bp = Blueprint("categories", __name__)


@categories_bp.route("", methods=["POST"])
def create_category():
    try:
        category_data = CategoryCreate.model_validate(request.get_json())
    except ValidationError as error:
        return jsonify({"errors": error.errors()}), 400

    category = Category(name=category_data.name)

    db.session.add(category)
    db.session.commit()

    return jsonify(CategoryResponse.model_validate(category).model_dump()), 201


@categories_bp.route("", methods=["GET"])
def get_categories():
    statement = select(Category)
    categories = db.session.execute(statement).scalars().all()

    result = [CategoryResponse.model_validate(category).model_dump() for category in categories]

    return jsonify(result), 200


@categories_bp.route("/<int:category_id>", methods=["PUT"])
def update_category(category_id: int):
    category = db.session.get(Category, category_id)

    if category is None:
        return jsonify({"error": "Category not found"}), 404

    try:
        category_data = CategoryCreate.model_validate(request.get_json())
    except ValidationError as error:
        return jsonify({"errors": error.errors()}), 400

    category.name = category_data.name
    db.session.commit()

    return jsonify(CategoryResponse.model_validate(category).model_dump()), 200


@categories_bp.route("/<int:category_id>", methods=["DELETE"])
def delete_category(category_id: int):
    category = db.session.get(Category, category_id)

    if category is None:
        return jsonify({"error": "Category not found"}), 404

    question_exists_statement = (select(Question.id).where(Question.category_id == category_id).limit(1))

    question_id = db.session.execute(question_exists_statement).scalar_one_or_none()

    if question_id is not None:
        return jsonify({"error": "Cannot delete category because it has questions"}), 409

    db.session.delete(category)
    db.session.commit()

    return jsonify({"message": "Category deleted"}), 200
