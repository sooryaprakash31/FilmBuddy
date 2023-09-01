from flask import Blueprint, jsonify, request

from ..po.recommendation_po import RecommendationPo
from ..services.recommendation_service import RecommendationService

controller = Blueprint('controller', __name__)


@controller.route('/recommend/<string:title>/<string:year>', methods=['POST'])
def recommend(title, year):

    # todo: Add validation

    data = validate_data(request.form.to_dict())

    recommendation_po = RecommendationPo(**data)

    recommendations = RecommendationService(title=title, year=year, recommendation_po=recommendation_po). \
        get_recommendations()

    return jsonify(recommendations.to_dict(orient='records')), 200


def validate_data(data):
    return {
        "recommendations_count": int(data["recommendations_count"]),
        "rating_filter": float(data["rating_filter"]),
        "popularity_threshold": float(data["popularity_threshold"])
    }

