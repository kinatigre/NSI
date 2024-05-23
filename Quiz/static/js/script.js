const questions = [
    {
        question: "Quel est le nom du monde fictif où se déroule League of Legends ?",
        answers: [
            { text: "Runeterra", correct: true },
            { text: "Azeroth", correct: false },
            { text: "Midgard", correct: false },
            { text: "Tamriel", correct: false }
        ]
    },
    {
        question: "Qui a développé le jeu League of Legends ?",
        answers: [
            { text: "Blizzard Entertainment", correct: false },
            { text: "Riot Games", correct: true },
            { text: "Valve Corporation", correct: false },
            { text: "Electronic Arts", correct: false }
        ]
    },
    {
        question: "Combien de champions étaient disponibles lors de la sortie initiale de LoL en 2009 ?",
        answers: [
            { text: "20", correct: true },
            { text: "40", correct: false },
            { text: "60", correct: false },
            { text: "80", correct: false }
        ]
    },
    {
        question: "Quel champion est connu sous le nom de \"la Fille de la Glace\" ?",
        answers: [
            { text: "Ashe", correct: false },
            { text: "Lissandra", correct: true },
            { text: "Sejuani", correct: false },
            { text: "Anivia", correct: false }
        ]
    },
    {
        question: "Quelle est l'ultime capacité du champion Ezreal ?",
        answers: [
            { text: "Essaim de missiles", correct: false },
            { text: "Tir nourri", correct: false },
            { text: "Trait de feu", correct: false },
            { text: "Traque-éclair", correct: true }
        ]
    },
    {
        question: "De quelle région provient le champion Wukong ?",
        answers: [
            { text: "Ionia", correct: true },
            { text: "Noxus", correct: false },
            { text: "Demacia", correct: false },
            { text: "Freljord", correct: false }
        ]
    },
    {
        question: "Quel est le nom du champ de bataille principal de League of Legends ?",
        answers: [
            { text: "La Faille de l'Invocateur", correct: true },
            { text: "L'Abîme Hurlant", correct: false },
            { text: "Le Tutoriel", correct: false },
            { text: "La Forêt Tourmentée", correct: false }
        ]
    },
    {
        question: "Qui est le champion connu pour être un maître voleur ?",
        answers: [
            { text: "Twisted Fate", correct: true },
            { text: "Graves", correct: false },
            { text: "Jhin", correct: false },
            { text: "Lucian", correct: false }
        ]
    },
    {
        question: "Quel champion est une fusion entre une femme et un serpent ?",
        answers: [
            { text: "Evelynn", correct: false },
            { text: "Elise", correct: false },
            { text: "Cassiopeia", correct: true },
            { text: "Shyvana", correct: false }
        ]
    },
    {
        question: "Quel est le nom du trophée remis aux vainqueurs du Championnat du Monde de LoL ?",
        answers: [
            { text: "La Coupe de Cristal", correct: false },
            { text: "Le Calice de l'Invocateur", correct: false },
            { text: "La Coupe des Conquérants", correct: true },
            { text: "La Coupe des Invocateurs", correct: false }
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

    // Créer un objet FormData pour envoyer les données
    const formData = new FormData();
    formData.append('nom', nom);
    formData.append('point', score);

    // Envoyer une requête POST à /add
    fetch('/add', {
        method: 'POST',
        body: formData
    })
    .then( () => {
        window.location.href = `/score?nom=${nom}`;
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
        element.classList.add('vert');
    } else {
        element.classList.add('wrong');
        element.classList.add('rouge');
    }
}

function clearStatusClass(element) {
    element.classList.remove('correct');
    element.classList.remove('wrong');
    element.classList.remove('vert');
    element.classList.remove('rouge');

}

function showResults() {
    document.getElementById('quiz').classList.add('hidden');
    document.getElementById('result').classList.remove('hidden');
    document.getElementById('score').innerText = `Votre score est de ${score} sur 10.`;
}
