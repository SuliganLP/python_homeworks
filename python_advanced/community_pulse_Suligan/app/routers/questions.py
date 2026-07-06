from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from sqlalchemy import select

from app.models import db
from app.models.categories import Category
from app.models.questions import Question
from app.schemas.question import QuestionCreate, QuestionResponse


questions_bp = Blueprint("questions", __name__)


@questions_bp.route("", methods=["GET"])
def get_questions():
    statement = select(Question)
    questions = db.session.execute(statement).scalars().all()

    result = [QuestionResponse.model_validate(question).model_dump() for question in questions]

    return jsonify(result), 200


@questions_bp.route("", methods=["POST"])
def create_question():
    try:
        question_data = QuestionCreate.model_validate(request.get_json())
    except ValidationError as error:
        return jsonify({"errors": error.errors()}), 400

    category = db.session.get(Category, question_data.category_id)

    if category is None:
        return jsonify({"error": "Category not found"}), 404

    question = Question(text=question_data.text, category_id=question_data.category_id)

    db.session.add(question)
    db.session.commit()

    return jsonify(QuestionResponse.model_validate(question).model_dump()), 201


@questions_bp.route("/<int:question_id>", methods=["GET"])
def get_question(question_id: int):
    question = db.session.get(Question, question_id)

    if question is None:
        return jsonify({"error": "Question not found"}), 404

    return jsonify(QuestionResponse.model_validate(question).model_dump()), 200


@questions_bp.route("/<int:question_id>", methods=["PUT"])
def update_question(question_id: int):
    question = db.session.get(Question, question_id)

    if question is None:
        return jsonify({"error": "Question not found"}), 404

    try:
        question_data = QuestionCreate.model_validate(request.get_json())
    except ValidationError as error:
        return jsonify({"errors": error.errors()}), 400

    category = db.session.get(Category, question_data.category_id)

    if category is None:
        return jsonify({"error": "Category not found"}), 404

    question.text = question_data.text
    question.category_id = question_data.category_id

    db.session.commit()

    return jsonify(QuestionResponse.model_validate(question).model_dump()), 200


@questions_bp.route("/<int:question_id>", methods=["DELETE"])
def delete_question(question_id: int):
    question = db.session.get(Question, question_id)

    if question is None:
        return jsonify({"error": "Question not found"}), 404

    db.session.delete(question)
    db.session.commit()

    return jsonify({"message": "Question deleted"}), 200
