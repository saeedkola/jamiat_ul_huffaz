# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Participant Group",
					"label": "Participant Groups"
				},
				{
					"type": "doctype",
					"name": "Participant"					
				},
				{
					"type": "doctype",
					"name": "Question Group"
				},
				{
					"type": "doctype",
					"name": "Question"
				},
				{
					"type": "doctype",
					"name": "JUH Settings"
				}
			]
		},
		{
			"label": _("Scoring"),
			"items":[
				{
					"type": "doctype",
					"name": "Scorecard"
				}
			]
		},
		{
			"label": _("Pages"),
			"items":[
				{
					"type" : "page",
					"name" : "question-selection"
				},
				{
					"type" : "page",
					"name" : "participant-selection"
				}
			]
		}

	]