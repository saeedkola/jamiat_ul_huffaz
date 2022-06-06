# Copyright (c) 2022, Element Labs and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Scorecard(Document):
	def before_insert(self):
		self.set("scores", [])
		question_group = frappe.get_doc("Question Group",self.question_group)
		for q in question_group.questions:
			row = self.append('scores',{})
			row.question = q.question




	def validate(self):
		total_deduction = 0;
		total_score = 0;
		for question in self.scores:
			yaddasht = question.yaddasht.count('1')*10 if question.yaddasht else 0

			lehn_jaly = question.lehn_jaly.count('1')*2 if question.lehn_jaly else 0
			lehn_khafy = question.lehn_khafy.count('1')*2 if question.lehn_khafy else 0
			atak = question.atak.count('1')*0.5 if question.atak else 0
			question.total_deduction = yaddasht+lehn_jaly+lehn_khafy+atak
			total_deduction += question.total_deduction

		self.total_deduction = total_deduction


