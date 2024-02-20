from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        'question': '1. Which of the following is a programming language?',
        'choices': ['HTML', ' JPEG', 'PNG', 'XML'],
        'answer': 'HTML'
    },
    {
        'question': '2. Which programming language is used for developing Android applications?',
        'choices': ['Java', 'Python', 'C#', 'Ruby'],
        'answer': 'Java'
    },
    {
        'question': '3. What is the output of the following code snippet?',
        'choices': ['10', '5', '2', '0'],
        'answer': '2'
    },
    {
        'question': '4. Which data structure uses the Last-In-First-Out (LIFO) principle?',
        'choices': ['Queue', 'stack', 'Heap', 'Linked list'],
        'answer': 'Stack'
    },
    {
        'question': '5. What does SQL stand for?',
        'choices': [' Standard Query Language', 'Structured Query Language', 'Simple Query Language', 'Secondary Query Language'],
        'answer': 'Structured Query Language'
    },
    {
         'question': '6. Which of the following is not a valid control structure in most programming languages?',
        'choices': ['If-else ', 'For loop', 'Switch statement', ' Stop statement'],
        'answer': 'Stop statement'
    },
    {
         'question': '7. What does the acronym "API" stand for?',
        'choices': [' Application Programming Interface', 'Advanced Programming Interface', 'Automatic Programming Interface', 'Application Protocol Interface'],
        'answer': 'Application Protocol Interface'
    },
    {
          'question': '8. In Python, which of the following is a mutable data type?',
        'choices': ['  String', ' Tuple', 'List', ' Dictionary'],
        'answer': 'List'
    },
    {
         'question': '9. What is the purpose of version control systems (VCS)?',
        'choices': ['To manage and track changes to source code ', 'To compile and execute programs', 'To test software applications', 'To design user interfaces '],
        'answer': 'To manage and track changes to source code'
    },
    {
         'question': '10. Which programming language is known for its use in web development?',
        'choices': [' Java ', ' Python', 'JavaScript', ' C++'],
        'answer': ' JavaScript'
    }
    # Add more questions here...
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process registration form data and store in database
        # Redirect to a success page or display an appropriate message
        return "Registration successful"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validate login credentials and redirect to appropriate page
        # or display an error message
        return "Login successful"
    return render_template('login.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Process submitted answers and calculate score
        score = 0
        for question in questions:
            submitted_answer = request.form.get(question['question'])
            if submitted_answer == question['answer']:
                score += 1
        total_questions = len(questions)
        percentage = (score / total_questions) * 100

        if percentage >= 90:
            grade = 'A'
            message = 'Excellent job!'
        elif percentage >= 80:
            grade = 'B'
            message = 'Well done!'
        elif percentage >= 70:
            grade = 'C'
            message = 'Good effort!'
        elif percentage >= 60:
            grade = 'D'
            message = 'You passed!'
        else:
            grade = 'F'
            message = 'You did not pass. Try again.   Better luck next time'
        return render_template('score.html', score=score, grade=grade, message=message)
    return render_template('quiz.html', questions=questions)
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

