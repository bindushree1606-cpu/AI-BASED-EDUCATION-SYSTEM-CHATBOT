from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ---------------- EDUCATION KNOWLEDGE ----------------

knowledge = {
    "education": """Education is the process of gaining knowledge,
skills and values.

Types of education:
1. Formal education
2. Informal education
3. Non-formal education

Education helps students develop their knowledge and future careers.""",

    "school": """School education provides basic knowledge.

Stages:
1. Primary education
2. Middle school
3. Secondary education
4. Higher secondary education""",

    "college": """College education provides higher-level learning.

Popular courses:
1. BCA - Computer Applications
2. BBA - Business Administration
3. BCom - Commerce
4. BA - Arts
5. BSc - Science
6. BTech - Technology
7. BE - Engineering""",

    "course": """Popular educational courses:

1. BCA - Bachelor of Computer Applications
2. BBA - Bachelor of Business Administration
3. BCom - Bachelor of Commerce
4. BA - Bachelor of Arts
5. BSc - Bachelor of Science
6. BTech - Bachelor of Technology
7. MBA - Master of Business Administration
8. MCA - Master of Computer Applications
9. MSc - Master of Science
10. MA - Master of Arts""",

    "admission": """College admission process:

1. Select a suitable college.
2. Check eligibility criteria.
3. Fill out the application form.
4. Submit required documents.
5. Complete the admission procedure.
6. Pay the applicable fees.

Always check the official college website.""",

    "Scholarships": """Scholarships provide financial assistance to students.

Types:
1. Merit-based Scholarships
2. Need-based Scholarships
3. Government Scholarships
4. Minority Scholarships
5. Sports Scholarships

Check official scholarship portals for eligibility.""",

    "exam": """Types of examinations:

1. Internal examinations
2. Semester examinations
3. Annual examinations
4. Entrance examinations
5. Competitive examinations

Prepare a timetable and revise regularly.""",

    "study": """Effective study techniques:

1. Prepare a daily timetable.
2. Set achievable goals.
3. Understand concepts.
4. Prepare short notes.
5. Practise previous question papers.
6. Take regular breaks.
7. Revise important topics.

Consistency is the key to success!""",

    "career": """Popular career opportunities:

1. Software Developer
2. Web Developer
3. Data Analyst
4. Teacher
5. Accountant
6. Business Analyst
7. AI Engineer
8. Cybersecurity Analyst
9. Government Officer
10. Entrepreneur

Choose a career based on your interests and skills.""",

    "competitive": """Popular competitive examinations in India:

1. UPSC
2. SSC
3. Banking examinations
4. Railway examinations
5. CAT
6. GATE
7. NEET
8. JEE

Check official websites for updated information.""",

    "online learning": """Online learning allows students to learn through the internet.

Popular platforms:
1. SWAYAM
2. NPTEL
3. Coursera
4. edX
5. Khan Academy
6. DIKSHA""",

    "higher education": """Higher education includes:

1. Undergraduate degree
2. Postgraduate degree
3. Diploma programmes
4. Professional courses
5. Doctoral programmes (PhD)

Choose a programme according to your future goals.""",

    "programming": """Programming is the process of writing instructions
that tell computers what to do.

Popular programming languages:
1. Python
2. Java
3. C
4. C++
5. JavaScript
6. PHP

Learn variables, conditions, loops and functions first.""",

    "artificial intelligence": """Artificial Intelligence (AI) enables machines
to perform tasks that normally require human intelligence.

Applications:
1. Chatbots
2. Face recognition
3. Voice assistants
4. Language translation
5. Recommendation systems
6. Educational assistants""",

    "machine learning": """Machine Learning is a branch of Artificial Intelligence.

It allows computers to learn patterns from data.

Types:
1. Supervised learning
2. Unsupervised learning
3. Reinforcement learning

Applications include prediction and recommendation systems.""",

    "computer": """Computer science provides knowledge about computers.

Important subjects:
1. Programming
2. Database Management
3. Computer Networks
4. Operating Systems
5. Artificial Intelligence
6. Machine Learning
7. Cybersecurity
8. Web Development""",

    "time management": """Time management helps students use their time effectively.

Tips:
1. Create a daily schedule.
2. Prioritise important tasks.
3. Avoid distractions.
4. Complete assignments on time.
5. Set realistic goals.
6. Review your progress.""",

    "internet": """The Internet is a worldwide network connecting computers.

Educational uses:
1. Online classes
2. Digital libraries
3. Research
4. Online examinations
5. Educational videos
6. Communication with teachers.""",

    "resume": """A resume presents a person's education, skills and experience.

Important sections:
1. Personal details
2. Career objective
3. Educational qualifications
4. Technical skills
5. Projects
6. Internship experience
7. Certifications.""",

    "university": """A university is an institution that provides higher education
and awards academic degrees.

Universities offer undergraduate, postgraduate
and research programmes.""",

    "fee": """Educational fees depend on the course,
college and admission category.

Contact the college admission office
or visit its official website for accurate information.""",

    "job": """Popular job opportunities include:

1. Software Developer
2. Web Developer
3. Data Analyst
4. Teacher
5. Accountant
6. Business Analyst
7. AI Engineer
8. Government Officer."""
}


# ---------------- CHATBOT BRAIN ----------------

def get_response(user_message):

    question = user_message.lower().strip()

    if not question:
        return "Please enter your question."

    if any(word in question for word in
           ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! Welcome to EduBot AI! 🎓 How can I help you today?"

    if any(word in question for word in ["bye", "goodbye"]):
        return "Goodbye! Keep learning and achieve your dreams! 💜"

    if "thankyou" in question:
        return "You're welcome! Happy learning! 😊"

    # Direct keyword matching
    if "Scholarships" in question:
        return knowledge["Scholarships"]

    if "admission" in question:
        return knowledge["admission"]

    if "course" in question or "degree" in question:
        return knowledge["course"]

    if "career" in question or "job" in question:
        return knowledge["career"]

    if "exam" in question or "test" in question:
        return knowledge["exam"]

    if "study" in question or "revision" in question:
        return knowledge["study"]

    if "artificial intelligence" in question or "what is ai" in question:
        return knowledge["artificial intelligence"]

    if "machine learning" in question:
        return knowledge["machine learning"]

    if "online learning" in question or "learning platforms" in question:
        return knowledge["online learning"]

    if "higher education" in question:
        return knowledge["higher education"]

    if "programming" in question or "coding" in question:
        return knowledge["programming"]

    if "computer" in question:
        return knowledge["computer"]

    if "competitive" in question or "upsc" in question:
        return knowledge["competitive"]

    if "time management" in question:
        return knowledge["time management"]

    if "resume" in question:
        return knowledge["resume"]

    if "university" in question:
        return knowledge["university"]

    if "fee" in question or "fees" in question:
        return knowledge["fee"]

    if "internet" in question:
        return knowledge["internet"]

    if "school" in question:
        return knowledge["school"]

    if "college" in question:
        return knowledge["college"]

    if "education" in question:
        return knowledge["education"]

    return """I'm still learning about this topic! 😊

You can ask me about:

📚 Education and Courses
🏫 School and College
🎓 Admissions and Scholarships
📝 Examinations
💼 Career Guidance
💻 Programming and Computers
🤖 Artificial Intelligence
📖 Study Tips
🌐 Online Learning
⏰ Time Management

Please try asking another question!"""


# ---------------- HTML + CSS + JAVASCRIPT ----------------

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>EduBot AI | Smart Education Assistant</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #071326, #17264a, #39245f);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 15px;
    color: white;
}

.container {
    width: 100%;
    max-width: 850px;
    background: #101d36;
    border: 1px solid #34476b;
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 15px 50px rgba(0,0,0,0.4);
    animation: appear 0.8s ease;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #34476b;
    padding-bottom: 18px;
}

.logo {
    font-size: 25px;
    font-weight: bold;
    color: #b49aff;
}

.status {
    color: #b9c5db;
    font-size: 13px;
}

.dot {
    display: inline-block;
    width: 9px;
    height: 9px;
    background: #35e89b;
    border-radius: 50%;
    box-shadow: 0 0 10px #35e89b;
}

.welcome {
    text-align: center;
    padding: 25px 10px;
}

.robot {
    font-size: 55px;
    animation: float 2s infinite ease-in-out;
}

@keyframes float {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-10px);
    }
}

.welcome h1 {
    font-size: 27px;
    color: #c2adff;
    margin: 12px 0;
}

.welcome p {
    color: #c1cbe0;
    font-size: 14px;
    line-height: 1.6;
}

.chat-box {
    height: 320px;
    overflow-y: auto;
    background: #0a162c;
    border: 1px solid #293e60;
    border-radius: 15px;
    padding: 18px;
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.bot, .user {
    max-width: 85%;
    padding: 13px 16px;
    border-radius: 15px;
    font-size: 14px;
    line-height: 1.7;
    white-space: pre-line;
    overflow-wrap: anywhere;
    animation: appear 0.3s ease;
}

.bot {
    background: #243759;
    color: white;
    align-self: flex-start;
    border-bottom-left-radius: 3px;
}

.user {
    background: linear-gradient(120deg, #7454d8, #a17af8);
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 3px;
}

.suggestions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 18px 0;
    justify-content: center;
}

.suggestions button {
    background: #1c2e4d;
    border: 1px solid #6f5ba8;
    color: #d8cbff;
    padding: 10px 14px;
    border-radius: 20px;
    cursor: pointer;
    transition: 0.3s;
}

.suggestions button:hover {
    background: #7657d9;
    color: white;
    transform: translateY(-3px);
}

.input-area {
    display: flex;
    gap: 10px;
}

.input-area input {
    flex: 1;
    min-width: 0;
    padding: 15px;
    border: 1px solid #415477;
    border-radius: 12px;
    outline: none;
    background: #172742;
    color: white;
    font-size: 14px;
}

.input-area input:focus {
    border-color: #a78bfa;
    box-shadow: 0 0 10px rgba(167,139,250,0.3);
}

.input-area input::placeholder {
    color: #9ba9c2;
}

.send {
    width: 55px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(135deg, #7958df, #a78bfa);
    color: white;
    font-size: 22px;
    cursor: pointer;
    transition: 0.3s;
}

.send:hover {
    transform: scale(1.08);
    box-shadow: 0 0 15px #9474f0;
}

footer {
    text-align: center;
    color: #9caac4;
    font-size: 12px;
    margin-top: 22px;
}

@media(max-width: 600px) {

    .container {
        padding: 15px;
    }

    .welcome h1 {
        font-size: 21px;
    }

    .logo {
        font-size: 20px;
    }

    .chat-box {
        height: 280px;
    }

}

</style>
</head>

<body>

<div class="container">

<header>

    <div class="logo">🎓 EduBot AI</div>

    <div class="status">
        <span class="dot"></span>
        Online Assistant
    </div>

</header>

<section class="welcome">

    <div class="robot">🤖</div>

    <h1>Your Smart Education Assistant</h1>

    <p>
        Learn smarter, explore opportunities and
        discover everything about education.
    </p>

</section>

<div class="chat-box" id="chatBox">

    <div class="bot">
        Hello! 👋 Welcome to EduBot AI.

        I can help you with courses, admissions,
        scholarships, examinations, career guidance
        and much more.

        What would you like to learn today?
    </div>

</div>

<div class="suggestions">

    <button onclick="quickAsk('Tell me about courses')">
        📚 Courses
    </button>

    <button onclick="quickAsk('Tell me about scholarships')">
        🎓 Scholarships
    </button>

    <button onclick="quickAsk('Give me study tips')">
        📖 Study Tips
    </button>

    <button onclick="quickAsk('Tell me about careers')">
        💼 Career
    </button>

    <button onclick="quickAsk('What is artificial intelligence?')">
        🤖 AI
    </button>

</div>

<div class="input-area">

    <input
        type="text"
        id="userInput"
        placeholder="Ask anything about education..."
        autocomplete="off"
        onkeydown="if(event.key === 'Enter') sendMessage()"
    >

    <button class="send" onclick="sendMessage()">
        ➤
    </button>

</div>

<footer>
    EduBot AI | Smart Learning for Everyone ✨
</footer>

</div>

<script>

async function sendMessage() {

    const input = document.getElementById("userInput");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user");

    input.value = "";

    const loading = addMessage("Thinking...", "bot");

    try {

        const response = await fetch("/get_response", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        loading.textContent = data.response;

    } catch (error) {

        loading.textContent =
            "Unable to connect. Please check whether the Python server is running.";

    }

}

function addMessage(message, className) {

    const chatBox = document.getElementById("chatBox");

    const div = document.createElement("div");

    div.className = className;

    div.textContent = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

    return div;

}

function quickAsk(question) {

    document.getElementById("userInput").value = question;

    sendMessage();

}

</script>

</body>
</html>
"""


# ---------------- FLASK ROUTES ----------------

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)


@app.route("/get_response", methods=["POST"])
def chatbot():

    data = request.get_json(silent=True) or {}

    message = data.get("message", "")

    reply = get_response(message)

    return jsonify({"response": reply})


# ---------------- START APPLICATION ----------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)