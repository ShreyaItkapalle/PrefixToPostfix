document.getElementById('evaluate').addEventListener('click', function() {
  const expression = document.getElementById('expression').value.trim();
  if (!expression) {
      alert('Please enter a valid prefix expression.');
      return;
  }

  try {
      const postfix = prefixToPostfix(expression);
      document.getElementById('output').textContent = postfix;
  } catch (error) {
      document.getElementById('output').textContent = 'Invalid expression';
  }
});

/**
 * Converts a prefix expression to postfix.
 * Supports both numbers and alphabetic variables as operands.
 */
function prefixToPostfix(expression) {
  const stack = [];
  const tokens = expression.split(' ').reverse();

  for (const token of tokens) {
      if (isOperator(token)) {
          const operand1 = stack.pop();
          const operand2 = stack.pop();
          stack.push(`${operand1} ${operand2} ${token}`);
      } else {
          stack.push(token);
      }
  }

  if (stack.length !== 1) {
      throw new Error('Invalid prefix expression');
  }

  return stack.pop();
}

function isOperator(token) {
  return ['+', '-', '*', '/', '^'].includes(token) && token.length === 1;
}
