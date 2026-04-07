const STORAGE_KEY = "jiporady_state_v1";

const boardEl = document.getElementById("board");
const scoreEl = document.getElementById("score");
const progressEl = document.getElementById("progress");
const finalSectionEl = document.getElementById("finalSection");
const finalCategoryEl = document.getElementById("finalCategory");
const finalQuestionEl = document.getElementById("finalQuestion");
const finalAnswerEl = document.getElementById("finalAnswer");

const round1Btn = document.getElementById("round1Btn");
const round2Btn = document.getElementById("round2Btn");
const finalBtn = document.getElementById("finalBtn");
const newGameBtn = document.getElementById("newGameBtn");
const clearStorageBtn = document.getElementById("clearStorageBtn");
const showFinalAnswerBtn = document.getElementById("showFinalAnswerBtn");

const clueModal = document.getElementById("clueModal");
const closeModalBtn = document.getElementById("closeModalBtn");
const modalCategory = document.getElementById("modalCategory");
const modalValue = document.getElementById("modalValue");
const modalQuestion = document.getElementById("modalQuestion");
const modalAnswer = document.getElementById("modalAnswer");
const answerWrapper = document.getElementById("answerWrapper");
const showAnswerBtn = document.getElementById("showAnswerBtn");
const correctBtn = document.getElementById("correctBtn");
const incorrectBtn = document.getElementById("incorrectBtn");

let gameData = null;
let state = null;
let currentSelection = null;

function defaultState(data) {
    return {
        score: 0,
        activeRound: "round_1",
        usedClues: {
            round_1: {},
            round_2: {},
        },
        finalAnswerShown: false,
    };
}

function loadState(data) {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) {
        return defaultState(data);
    }

    try {
        const parsed = JSON.parse(raw);
        return {
            ...defaultState(data),
            ...parsed,
            usedClues: {
                round_1: parsed.usedClues?.round_1 || {},
                round_2: parsed.usedClues?.round_2 || {},
            },
        };
    } catch {
        return defaultState(data);
    }
}

function saveState() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function money(value) {
    const sign = state.score < 0 ? "-" : "";
    if (typeof value === "number") {
        return `$${Math.abs(value).toLocaleString()}`;
    }
    return `${sign}$${Math.abs(state.score).toLocaleString()}`;
}

function clueKey(categoryIndex, clueIndex) {
    return `${categoryIndex}-${clueIndex}`;
}

function setActiveControlButton() {
    round1Btn.classList.toggle("active", state.activeRound === "round_1");
    round2Btn.classList.toggle("active", state.activeRound === "round_2");
    finalBtn.classList.toggle("active", state.activeRound === "final");
}

function updateScorePanel() {
    scoreEl.textContent = `${state.score < 0 ? "-" : ""}$${Math.abs(state.score).toLocaleString()}`;

    if (state.activeRound === "final") {
        const total = totalCluesAcrossRounds();
        const solved = solvedCluesAcrossRounds();
        progressEl.textContent = `${solved} / ${total}`;
        return;
    }

    const categories = gameData.rounds[state.activeRound].categories;
    const total = categories.reduce((sum, category) => sum + category.clues.length, 0);
    const solved = Object.keys(state.usedClues[state.activeRound] || {}).length;
    progressEl.textContent = `${solved} / ${total}`;
}

function totalCluesAcrossRounds() {
    return Object.values(gameData.rounds).reduce((sum, round) => {
        return sum + round.categories.reduce((inner, category) => inner + category.clues.length, 0);
    }, 0);
}

function solvedCluesAcrossRounds() {
    return Object.values(state.usedClues).reduce((sum, roundMap) => sum + Object.keys(roundMap).length, 0);
}

function renderBoard() {
    setActiveControlButton();
    updateScorePanel();

    if (state.activeRound === "final") {
        boardEl.innerHTML = "";
        finalSectionEl.classList.remove("hidden");
        finalCategoryEl.textContent = gameData.final.category;
        finalQuestionEl.textContent = gameData.final.question;
        finalAnswerEl.textContent = gameData.final.answer;
        finalAnswerEl.classList.toggle("hidden", !state.finalAnswerShown);
        return;
    }

    finalSectionEl.classList.add("hidden");
    boardEl.innerHTML = "";

    const round = gameData.rounds[state.activeRound];
    round.categories.forEach((category, categoryIndex) => {
        const column = document.createElement("div");
        column.className = "column";

        const categoryTile = document.createElement("div");
        categoryTile.className = "category-tile";
        categoryTile.textContent = category.title;
        column.appendChild(categoryTile);

        category.clues.forEach((clue, clueIndex) => {
            const button = document.createElement("button");
            const key = clueKey(categoryIndex, clueIndex);
            const isUsed = Boolean(state.usedClues[state.activeRound][key]);

            button.className = `clue-tile ${isUsed ? "used" : ""}`;
            button.type = "button";
            button.textContent = money(clue.value);
            button.disabled = isUsed;
            button.addEventListener("click", () => openClue(state.activeRound, categoryIndex, clueIndex));

            column.appendChild(button);
        });

        boardEl.appendChild(column);
    });
}

function openClue(roundKey, categoryIndex, clueIndex) {
    const round = gameData.rounds[roundKey];
    const category = round.categories[categoryIndex];
    const clue = category.clues[clueIndex];

    currentSelection = { roundKey, categoryIndex, clueIndex, clue };
    modalCategory.textContent = `${round.name} • ${category.title}`;
    modalValue.textContent = money(clue.value);
    modalQuestion.textContent = clue.question;
    modalAnswer.textContent = clue.answer;
    answerWrapper.classList.add("hidden");
    clueModal.classList.remove("hidden");
}

function closeModal() {
    clueModal.classList.add("hidden");
    currentSelection = null;
}

function scoreCurrentClue(correct) {
    if (!currentSelection) {
        return;
    }

    const { roundKey, categoryIndex, clueIndex, clue } = currentSelection;
    const key = clueKey(categoryIndex, clueIndex);

    if (state.usedClues[roundKey][key]) {
        closeModal();
        return;
    }

    state.score += correct ? clue.value : -clue.value;
    state.usedClues[roundKey][key] = {
        result: correct ? "correct" : "incorrect",
        value: clue.value,
        categoryIndex,
        clueIndex,
    };

    saveState();
    closeModal();
    renderBoard();
}

async function init() {
    const response = await fetch("/api/game");
    gameData = await response.json();
    state = loadState(gameData);
    renderBoard();
}

round1Btn.addEventListener("click", () => {
    state.activeRound = "round_1";
    saveState();
    renderBoard();
});

round2Btn.addEventListener("click", () => {
    state.activeRound = "round_2";
    saveState();
    renderBoard();
});

finalBtn.addEventListener("click", () => {
    state.activeRound = "final";
    saveState();
    renderBoard();
});

showFinalAnswerBtn.addEventListener("click", () => {
    state.finalAnswerShown = true;
    saveState();
    renderBoard();
});

newGameBtn.addEventListener("click", () => {
    const confirmed = window.confirm("Start a fresh game and reset the score? This clears all current progress.");
    if (!confirmed) {
        return;
    }
    state = defaultState(gameData);
    saveState();
    renderBoard();
});

clearStorageBtn.addEventListener("click", () => {
    const confirmed = window.confirm("Hard reset everything saved for Jiporady in this browser?");
    if (!confirmed) {
        return;
    }
    localStorage.removeItem(STORAGE_KEY);
    state = defaultState(gameData);
    renderBoard();
});

showAnswerBtn.addEventListener("click", () => {
    answerWrapper.classList.remove("hidden");
});

correctBtn.addEventListener("click", () => scoreCurrentClue(true));
incorrectBtn.addEventListener("click", () => scoreCurrentClue(false));
closeModalBtn.addEventListener("click", closeModal);

clueModal.addEventListener("click", (event) => {
    if (event.target === clueModal) {
        closeModal();
    }
});

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        closeModal();
    }
    if (event.key.toLowerCase() === "a" && !clueModal.classList.contains("hidden")) {
        answerWrapper.classList.remove("hidden");
    }
});

init();
