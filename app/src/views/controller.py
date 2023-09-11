from flask import Blueprint, jsonify, request

from ..po.recommendation_po import RecommendationPo
from ..po.search_po import SearchPo
from ..services.recommendation_service import RecommendationService
from ..services.request_validation_service import RequestValidationService
from ..services.search_service import SearchService

controller = Blueprint('controller', __name__)


@controller.route('/recommend', methods=['POST'])
def recommend():
    data = RequestValidationService(request=request).validate_data()

    recommendation_po = RecommendationPo(**data)

    recommendations = RecommendationService(recommendation_po=recommendation_po). \
        get_recommendations()

    return jsonify(recommendations.to_dict(orient='records')), 200


@controller.route("/search", methods=['GET'])
def search():
    data = RequestValidationService(request=request).validate_data()
    search_po = SearchPo(**data)

    search_results = SearchService(search_po=search_po).get_results()

    return jsonify(search_results.to_dict(orient='records')), 200
