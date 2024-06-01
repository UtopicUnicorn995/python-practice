from tkinter import Tk, Label, Entry, Button, Text
import requests

window = Tk()
window.title("Quiz Application")
window.geometry('400x400+50+50')
window.resizable(False, False)


label = Label(window, text='Select a Quiz')
label.pack(ipadx=20, ipady=50)

text = Text(font="BOLD")


def get_data():
    try:
        quizzes = requests.get(
            'https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json')
        quizzes.raise_for_status()
        return quizzes.json()
    except requests.RequestException as error:
        label = Label(window, text=f"Sorry we could not fetch the request: {error}")
        label.pack(ipadx=20, ipady=20)
    
def get_questions():
    label = Label(window, text='Shit')
    label.pack(ipadx=20, ipady=20)
    
def get_choices():
    pass

def get_topic():
    topics = get_data().get('quizzes', [])
    get_questions()
    for topic in topics:
        button = Button(window, text=topic.get(
            'quizTitle', {}), command=print('pass'))
        button.pack(pady=8)



def main():
    score = 0
    get_topic()

if __name__ == "__main__":
    main()

window.mainloop()
