from os import path
from datetime import date, datetime
import requests
from pymongo import MongoClient
import gridfs
from bson import ObjectId

class MongoHelper:
	def download_and_save_csv(self, source, csv_type, url):
		result = requests.get(url)
		download_datetime = datetime.now()
		download_date = date(year= download_datetime.year, month= download_datetime.month, day=download_datetime.day)
		self.save_csv(source, csv_type, download_date, result.content)

	def save_csv(self, source, csv_type, file_date, file_contents):
		if isinstance(file_date, date):
			date_string = "{}_{}_{}".format(file_date.year, file_date.month, file_date.day)
			filename = "{}_{}_{}.csv".format(source, date_string, csv_type)
			put_result = self.covid_csv_fs.put(file_contents, filename=filename, mimetype='text/csv', metadata={'date': date_string, 'type': csv_type, 'source': source})
			print(put_result)

	def find_all_csv_items(self, source, csv_type, filter=None):
		csv_collection = self.covid_db['{}_{}'.format(source, csv_type)]
		query = csv_collection.find(filter)

		items = []

		for item in query:
			item['id'] = str(item['_id'])
			del item['_id']
			items.append(item)

		return items


	def parse_and_push_csv_data(self, csv_id):
		csv_headers = []
		filter = {'_id': ObjectId(csv_id)}
		query_count = self.covid_db.get_collection('fs.files').count_documents(filter)
		if query_count == 1:
			query = self.covid_csv_fs.find(filter)
			csv_meta_info = query[0].metadata
			csv_file_contents = query[0].read().decode('utf-8')
			csv_lines = csv_file_contents.split('\n')

			csv_collection = self.covid_db['{}_{}'.format(csv_meta_info['source'], csv_meta_info['type'])]

			csv_header = csv_lines[0]
			csv_data_lines = csv_lines[1:]

			for csv_header_label in csv_header.split(','):
				csv_headers.append(csv_header_label)

			for csv_data_line in csv_data_lines:
				data_dict = {}
				csv_data_line_items = csv_data_line.split(',')
				for i in range(len(csv_data_line_items)):
					data_dict[csv_headers[i]] = csv_data_line_items[i]
				count = csv_collection.count_documents(data_dict)

				if count == 0:
					csv_collection.insert_one(data_dict)

	def __init__(self):
		self.mongo_client = MongoClient()
		self.covid_db = self.mongo_client['covid_19']
		self.covid_csv_fs = gridfs.GridFS(self.covid_db)


test = MongoHelper()

# test.download_and_save_csv('ny_times', 'us_states', 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
# test.parse_and_push_csv_data('5e921ebb9ba543b49af1e12a')
# test.find_all_csv_items('ny_times', 'us_states', {'state': 'Washington'})