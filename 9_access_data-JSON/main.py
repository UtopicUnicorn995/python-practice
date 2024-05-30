import requests

def get_questions():
    try:
        response = requests.get('https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json')
        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print(f'Error fetching questions: {error}')
        return None

def get_answer(quiz_id):
    quizzes_data = get_questions()
    if quizzes_data:
        for quiz in quizzes_data.get('quizzes', []):
            for question in quiz.get('questions', []):
                if str(question.get('id')) == quiz_id:
                    for choice, is_correct in question.get('choices', {}).items():
                            if is_correct:
                                return f'The correct answer is {choice}'
    return "Question not found or no correct answer is provided."


def main():
    quiz_id = input("Enter the question ID: ")
    answer = get_answer(quiz_id)
    print(answer)
    
if __name__ == '__main__':
    main()