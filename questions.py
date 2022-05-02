import requests

ENDPOIND = "https://jservice.io/api/random"

params = {
	"count": 3, # questions_num
}

def get_questions():
    response = requests.get(url=ENDPOIND, params=params)
    response.raise_for_status()
    data = response.json()
    return data

questions_data = get_questions()[0]
question_id = questions_data['id']
answer = questions_data['answer']
question = questions_data['question']
date = questions_data['created_at']
print(question_id, answer, question, date)
