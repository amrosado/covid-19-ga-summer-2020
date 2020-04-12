import json
from flask import Blueprint, request, session, redirect, flash, Response

from flask_back_end.api.MongoHelper import MongoHelper

mongo_helper = MongoHelper()

api_blueprint = Blueprint('api', __name__, url_prefix="/api")

@api_blueprint.route('/<string:source>/<string:data_type>', methods=['GET'])
def retrieve_dataset_items(source, data_type):
	if request.method == "GET":
		key_list = request.args.keys()
		filter_dict = {}
		for key in key_list:
			filter_dict[key] = request.args.get(key)

		items = mongo_helper.find_all_csv_items(source, data_type, filter_dict)

		return Response(json.dumps(items), mimetype='application/javascript')

