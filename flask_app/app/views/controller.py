from flask import Blueprint, jsonify

from ..services.recommendation_service import RecommendationService

controller = Blueprint('controller', __name__)


@controller.route('/recommend/<string:title>/<string:year>', methods=['POST'])
def recommend(title, year):
    recommendations = RecommendationService(title=title, year=year).get_recommendations()

    return jsonify(recommendations.to_dict(orient='records')), 200
