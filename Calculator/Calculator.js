let currentNumber = '0';
let previousNumber = '';
let operator = '';
let shouldResetScreen= false;

const resultDisplay = document.getElementById('result');
const expressionDisplay = document.getElementById('expression');

function updateDisplay() {
    resultDisplay.textContent = currentNumber;
}

function inputNumber(value) {
    if (currentNumber.length >= 12 && !shouldResetScreen) return;

    if (shouldResetScreen) {
        currentNumber = value;
        shouldResetScreen = false;
    } else {
        currentNumber = currentNumber === '0' ? value : currentNumber + value;
    }
    
    updateDisplay();
}

function inputDecimal() {
    if (shouldResetScreen) {
        currentNumber = '0.';
        shouldResetScreen = false;
        updateDisplay();
        return;
    }

    if (currentNumber.includes('.')) return;

    currentNumber += '.'
    updateDisplay();
}
function selectOperater(value) {

    if (operator && !shouldResetScreen) {
        calculate();
    }

    previousNumber = currentNumber;
    operator = value;
    shouldResetScreen = true;

    expressionDisplay.textContent = '${previousNumber} ${operator}';
}

function calculate() {
    if (!operator || !previousNumber) return;

    const prev = parseFloat(previousNumber);
    const curr = parseFloat(currentNumber);
    let result;

    switch (operator) {
        case '+': result = prev + curr; break;
        case '-': result = prev - curr; break;
        case 'x': result = prev * curr; break;
        case '/':
            if (curr === 0) {
                currentNumber = 'Error'
                expressionDisplay.textContent = '';
                operator = '';
                previousNumber = '';
                updateDisplay();
                return;
            }
        }
}