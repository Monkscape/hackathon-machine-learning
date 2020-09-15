import requests

prospect = {
    'prospect_id': '14a1acd6-4ac1-47eb-84d8-6b1936dfd625',
    'lead_number': 653930,
    'lead_origin': 'api',
    'lead_source': 'olark_chat',
    'do_not_email': 'no',
    'do_not_call': 'no',
    'converted': 0,
    'totalvisits': 0.0,
    'total_time_spent_on_website': 0,
    'page_views_per_visit': 0.0,
    'last_activity': 'email_opened',
    'country': 'not_answered',
    'specialization': 'not_answered',
    'how_did_you_hear_about_x_education': 'not_answered',
    'what_is_your_current_occupation': 'unemployed',
    'what_matters_most_to_you_in_choosing_a_course': 'better_career_prospects',
    'search': 'no',
    'magazine': 'no',
    'newspaper_article': 'no',
    'x_education_forums': 'no',
    'newspaper': 'no',
    'digital_advertisement': 'no',
    'through_recommendations': 'no',
    'receive_more_updates_about_our_courses': 'no',
    'tags': 'busy',
    'lead_quality': 'not_answered',
    'update_me_on_supply_chain_content': 'no',
    'get_updates_on_dm_content': 'no',
    'lead_profile': 'not_answered',
    'city': 'not_answered',
    'asymmetrique_activity_index': '02_medium',
    'asymmetrique_profile_index': '02_medium',
    'asymmetrique_activity_score': 14.0,
    'asymmetrique_profile_score': 15.0,
    'i_agree_to_pay_the_amount_through_cheque': 'no',
    'a_free_copy_of_mastering_the_interview': 'no',
    'last_notable_activity': 'email_opened'
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=prospect)
print(response.json())