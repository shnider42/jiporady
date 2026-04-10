const boardElement = document.getElementById("board");
const newBoardBtn = document.getElementById("newBoardBtn");
const resetUsedBtn = document.getElementById("resetUsedBtn");
const categoryCountSelect = document.getElementById("categoryCount");

const clueModal = document.getElementById("clueModal");
const closeModalBtn = document.getElementById("closeModalBtn");
const showAnswerBtn = document.getElementById("showAnswerBtn");
const markUsedBtn = document.getElementById("markUsedBtn");

const modalCategory = document.getElementById("modalCategory");
const modalValue = document.getElementById("modalValue");
const modalPrompt = document.getElementById("modalPrompt");
const modalAnswer = document.getElementById("modalAnswer");

let currentBoard = [];
let currentClue = null;
let usedClues = new Set();

function getInitialBoard() {
    const dataTag = document.getElementById("initialBoardData");
    if (!dataTag) return [];
    return JSON.parse(dataTag.textContent);
}

function renderBoard(board) {
    currentBoard = board;
    usedClues = new Set();

    if (!boardElement) return;

    boardElement.style.setProperty("--board-columns", String(board.length));
    boardElement.innerHTML = "";

    board.forEach((category) => {
        const categoryCell = document.createElement("div");
        categoryCell.className = "category-cell";
        categoryCell.textContent = category.category;
        boardElement.appendChild(categoryCell);
    });

    const clueRows = Math.max(...board.map((category) => category.clues.length));

    for (let row = 0; row < clueRows; row += 1) {
        board.forEach((category, categoryIndex) => {
            const clue = category.clues[row];
            const clueButton = document.createElement("button");
            clueButton.className = "clue-cell";
            clueButton.type = "button";

            if (!clue) {
                clueButton.disabled = true;
                clueButton.classList.add("used");
                clueButton.textContent = "—";
                boardElement.appendChild(clueButton);
                return;
            }

            const clueId = `${categoryIndex}-${row}`;
            clueButton.dataset.clueId = clueId;
            clueButton.dataset.category = category.category;
            clueButton.dataset.value = clue.value;
            clueButton.dataset.question = clue.question;
            clueButton.dataset.answer = clue.answer;
            clueButton.textContent = `$${clue.value}`;

            clueButton.addEventListener("click", () => openClue(clueButton));
            boardElement.appendChild(clueButton);
        });
    }
}

function openClue(clueButton) {
    if (clueButton.classList.contains("used")) return;

    currentClue = clueButton;
    modalCategory.textContent = clueButton.dataset.category;
    modalValue.textContent = `$${clueButton.dataset.value}`;
    modalPrompt.textContent = clueButton.dataset.question;
    modalAnswer.textContent = clueButton.dataset.answer;
    modalAnswer.classList.add("hidden");
    clueModal.classList.remove("hidden");
}

function closeClue(markUsed = true) {
    if (currentClue && markUsed) {
        usedClues.add(currentClue.dataset.clueId);
        currentClue.classList.add("used");
        currentClue.setAttribute("aria-disabled", "true");
    }

    currentClue = null;
    clueModal.classList.add("hidden");
    modalAnswer.classList.add("hidden");
}

async function fetchNewBoard() {
    const categoryCount = categoryCountSelect ? categoryCountSelect.value : 6;
    const response = await fetch(`/api/board?categories=${encodeURIComponent(categoryCount)}`);
    const data = await response.json();
    renderBoard(data.board);
}

function resetUsedClues() {
    usedClues.clear();
    document.querySelectorAll(".clue-cell.used").forEach((clue) => {
        clue.classList.remove("used");
        clue.removeAttribute("aria-disabled");
    });
}

if (newBoardBtn) {
    newBoardBtn.addEventListener("click", fetchNewBoard);
}

if (resetUsedBtn) {
    resetUsedBtn.addEventListener("click", resetUsedClues);
}

if (showAnswerBtn) {
    showAnswerBtn.addEventListener("click", () => {
        modalAnswer.classList.remove("hidden");
    });
}

if (markUsedBtn) {
    markUsedBtn.addEventListener("click", () => closeClue(true));
}

if (closeModalBtn) {
    closeModalBtn.addEventListener("click", () => closeClue(true));
}

if (clueModal) {
    clueModal.addEventListener("click", (event) => {
        if (event.target === clueModal) {
            closeClue(true);
        }
    });
}

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && clueModal && !clueModal.classList.contains("hidden")) {
        closeClue(true);
    }
});

renderBoard(getInitialBoard());
