from flask import Blueprint, jsonify, request

from ..po.recommendation_po import RecommendationPo
from ..services.recommendation_service import RecommendationService
from ..services.request_validation_service import RequestValidationService

controller = Blueprint('controller', __name__)


@controller.route('/recommend', methods=['POST'])
def recommend():

    valid_data = RequestValidationService(request=request).validate_data()

    recommendation_po = RecommendationPo(**valid_data)

    recommendations = RecommendationService(recommendation_po=recommendation_po). \
        get_recommendations()

    return jsonify(recommendations.to_dict(orient='records')), 200

