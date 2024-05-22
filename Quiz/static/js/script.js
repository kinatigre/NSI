const questions = [
    {
        question: "1",
        answers: [
            { text: "1", correct: true },
            { text: "2", correct: false },
            { text: "3", correct: false },
            { text: "4", correct: false }
        ]
    },
    {
        question: "2",
        answers: [
            { text: "1", correct: false },
            { text: "2", correct: false },
            { text: "3", correct: true },
            { text: "4", correct: false }
        ]
    }   
];

let shuffledQuestions, currentQuestionIndex, score;

document.getElementById('next-btn').addEventListener('click', () => {
    currentQuestionIndex++;
    setNextQuestion();
});

function sendResult() {
    const lien = document.querySelector('a[href^="score?nom="]');
    const href = lien.getAttribute('href');
    const nom = href.split('nom=')[1].split('}}')[0];
    const point = score; // Utiliser la variable score existante

    // Créer un objet FormData pour envoyer les données
    const formData = new FormData();
    formData.append('nom', nom);
    formData.append('point', point);

    // Envoyer une requête POST à /add
    fetch('/add', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        // Rediriger vers la page score après l'ajout des données
        window.location.href = `/score?nom=${nom}`;
    })
    .catch(error => {
        console.error('Erreur :', error);
    });
}

function startGame() {
    document.getElementById('home').classList.add('hidden');
    document.getElementById('quiz').classList.remove('hidden');
    document.getElementById('result').classList.add('hidden');
    shuffledQuestions = questions.sort(() => Math.random() - 0.5).slice(0, 10); // formule pour choisir une question trouvée sur internet
    currentQuestionIndex = 0;
    score = 0;
    setNextQuestion();
}

function showHomePage() {
    document.getElementById('home').classList.remove('hidden');
    document.getElementById('quiz').classList.add('hidden');
    document.getElementById('result').classList.add('hidden');
}

function setNextQuestion() {
    resetState();
    if (currentQuestionIndex < shuffledQuestions.length) {
        showQuestion(shuffledQuestions[currentQuestionIndex]);
    } else {
        showResults();
    }
}

function showQuestion(question) {
    const questionContainer = document.getElementById('question-container');
    questionContainer.innerText = question.question;

    question.answers.forEach(answer => {
        const button = document.createElement('button');
        button.innerText = answer.text;
        button.classList.add('btn');
        if (answer.correct) {
            button.dataset.correct = answer.correct;
        }
        button.addEventListener('click', selectAnswer);
        document.getElementById('answer-buttons').appendChild(button);
    });
}

function resetState() {
    document.getElementById('next-btn').classList.add('hidden');
    while (document.getElementById('answer-buttons').firstChild) {
        document.getElementById('answer-buttons').removeChild(document.getElementById('answer-buttons').firstChild);
    }
}

function selectAnswer(e) {
    const selectedButton = e.target;
    const correct = selectedButton.dataset.correct;
    setStatusClass(selectedButton, correct);
    if (correct) {
        score++;
    }
    Array.from(document.getElementById('answer-buttons').children).forEach(button => {
        setStatusClass(button, button.dataset.correct);
    });
    document.getElementById('next-btn').classList.remove('hidden');
}

function setStatusClass(element, correct) {
    clearStatusClass(element);
    if (correct) {
        element.classList.add('correct');
    } else {
        element.classList.add('wrong');
    }
}

function clearStatusClass(element) {
    element.classList.remove('correct');
    element.classList.remove('wrong');
}

function showResults() {
    document.getElementById('quiz').classList.add('hidden');
    document.getElementById('result').classList.remove('hidden');
    document.getElementById('score').innerText = `Votre score est de ${score} sur 10.`;
}
