import frappe

@frappe.whitelist()
def get_question_selection_list():
	participant = frappe.db.get_value("JUH Settings","JUH Settings",'active_participant')
	participant_details = frappe.get_doc("Participant",participant)


	existing_scorecards = frappe.get_all('Scorecard', filters={'participant': participant}, fields=['name'])
	if existing_scorecards:
		return "<h1 class='text-center'>Question Selection Successful</h1>"

	group = participant_details.group

	if group:
		sql = """select name from `tabQuestion Group` where name not in (select question_group from `tabScorecard` where question_group is not null) and `participant_group` ='{}'""".format(group)

		questions = frappe.db.sql(sql,as_dict=1)
		data = {
			"participant" : participant_details,
			"question_groups": questions
		}
		html = frappe.render_template('templates/pages/question_selection.html', data)
		return html

@frappe.whitelist()
def set_question(question_group,participant):
	if not frappe.db.exists("Scorecard",participant):
		settings = frappe.get_doc("JUH Settings","JUH Settings")
		if settings.active_judges:
			for judge in settings.active_judges:

				scorecard = frappe.get_doc({
					"doctype": "Scorecard",
					"participant": participant,
					"question_group": question_group,
					"owner": judge.judge,
					"judge": judge.judge
				})
				scorecard.insert()

		frappe.db.set_value("Participant",participant,"question_group",question_group)
	else:
		scorecard = frappe.get_doc("Scorecard",participant)
	return scorecard

@frappe.whitelist()
def get_participant_groups():
	pg = frappe.get_all("Participant Group")
	data ={
	 'pg' : pg
	}
	return frappe.render_template('templates/pages/group_selection.html', data)

@frappe.whitelist()
def get_random_participant(group):
	sql = """select p.* from `tabParticipant` p
			left join `tabScorecard` s on p.name=s.name
			where p.`group`="{}" and s.name is null
			ORDER BY RAND()
			LIMIT 1""".format(group)
	participant = frappe.db.sql(sql,as_dict=1)
	if len(participant):
		frappe.client.set_value("JUH Settings", "JUH Settings", "active_participant", participant[0]['name'])
		return frappe.render_template('templates/pages/participant_modal.html',participant[0])
	else:
		return "<h1 class='text-center'>No More Participants!</h1>"
	




	