# Copyright (c) 2022, Element Labs and contributors
# For license information, please see license.txt

import frappe,requests
from frappe.model.document import Document

class Question(Document):
	def validate(self):
		if not self.override_ayah:
			ayahs = self.ayah
			surah = self.surah
			ayah_from = self.ayah_from
			ayah_to = self.ayah_to
			text_indopak = ""
			text_arabic = ""
			if ayahs:
				for ayah in ayahs.split(','):
					if ayah:
						url = "https://api.quran.com/api/v4/quran/verses/indopak?verse_key={}".format(ayah)
						response = requests.request("GET", url, headers={}, data={})

						json_response = response.json()
						if json_response['verses']:
							for verse in json_response['verses']:
								text_indopak += verse['text_indopak']
								text_indopak += '<span class=endayah> \u06DD </span>'
						else:
							frappe.throw("Ayahs Not valid")
						
			elif surah and ayah_from and ayah_to:
				if ayah_to<ayah_from:
					frappe.throw("Ayah To cant be smaller than Ayah From")
				if (ayah_to-ayah_from) > 30:
					frappe.throw("Too Many Ayahs")
				for x in range(ayah_from,ayah_to+1):
					url = "https://api.quran.com/api/v4/quran/verses/indopak?verse_key={}:{}".format(surah,x)

					response = requests.request("GET", url, headers={}, data={})

					json_response = response.json()
					if json_response['verses']:
						for verse in json_response['verses']:
							text_indopak += verse['text_indopak']
							text_indopak += '<span class=endayah> \u06DD </span>'
					else:
						frappe.throw("Ayahs Not valid")
			else:
				frappe.throw("Enter Ayah Numbers")

			self.text_indopak = text_indopak


						






