function Complete()
{
  let not_pol = document.Polish.NotPoland.value;
  let elem = "Исходное выражение: " + not_pol;
  document.getElementById('myTextarea').value += elem + "\n";
  Create_poland(not_pol);
}

function Calculation(){
  debugger;
  let not_pol = document.Polish.NotPoland.value;
  let elem = "Исходное выражение: " + not_pol;
  document.getElementById('myTextarea').value += elem + "\n";
  CalculatorPolish(not_pol);
}

function CalculatorPolish(polish_notation_expr){
  debugger;
  let polish_notation = polish_notation_expr.split(",");
  let stack_num = [];
  let sum = 0;

  for(let i = 0; i < polish_notation.length; i++){
    let symbol = polish_notation[i];
    switch (symbol){
      case '+':
        sum += performOperation(stack_num, "+", sum);
        break;
      case "-":
        sum += performOperation(stack_num, "-", sum);
        break;
      case "*":
        sum += performOperation(stack_num, "*", sum);
        break;
      case "/":
        sum += performOperation(stack_num, "/", sum);
        break;
      case "^":
        sum += performOperation(stack_num, "^", sum);
        break;
      default:
        stack_num.push(symbol);
    }

  }

  let elem = "Ответ: " + stack_num[0];
  document.getElementById('myTextarea').value += elem + "\n";
}

function performOperation(stack_num, oper, sum){
  let first_oper = stack_num.pop();
  let second_oper = stack_num.pop();
  sum = eval(second_oper + oper + first_oper);
  stack_num.push(sum)
  return sum
}

// 8,2,5,+,1,3,2,+,4,-,5,-,9,1,2,+,1,+,3,+ // ( 8 + 2 * 5 ) / ( 1 + 3 * 2 - 4 ) - 5 + ( 9 / ( 1 + 2 ) + 1 ) * 3

// 3 + 4 * 2 / ( 1 - 5 ) ^ 2 // ( 6 + 10 - 4 ) / ( 1 + 1 * 2 ) + 1  // ( 8 + 2 * 5 ) / ( 1 + 3 * 2 - 4 ) - 5 + ( 9 / ( 1 + 2 ) + 1 ) * 3
// 3,4,2,*,1,5,-,2,^,/,+     // 6,10,+,4,-,1,1,2,*,+,/,1,+          // 8,2,5,*,+,1,3,2,*,+,4,-,/,5,-,9,1,2,+,/,1,+,3,*,+
// 3 4 2 * 1 5 - 2 ^ / +     // 6,10,+,4,-,1,1,2,*,+,/,1,+.         // 8 2 5 * + 1 3 2 * + 4 - / 5 - 9 1 2 + / 1 + 3 * +

function Create_poland(not_poland)
{
  debugger;
  let sumbols = not_poland.split(" ");
  let poland = "";
  let out_array = [];
  let stack_operation = [];
  for (let i = 0; i < sumbols.length; i++)
  {
    let sumbol = sumbols[i];
    switch (sumbol)
    {
      case '^':
        if (stack_operation.length !== 0)
        {
          let out = right(sumbol, stack_operation, out_array);
        }
        else {
          stack_operation.push(sumbol)
        }
        break;
      case '*':
        stack_operation, out_array = left(sumbol, stack_operation, out_array);
        break;
      case '/':
        stack_operation, out_array = left(sumbol, stack_operation, out_array);
        break;
      case '+':
        if (stack_operation.length !== 0)
        {
          let out = right(sumbol, stack_operation, out_array);
        }
        else {
          stack_operation.push(sumbol)
        }
        break;
      case '-':
        if (stack_operation.length !== 0)
        {
          let out = right(sumbol, stack_operation, out_array);
        }
        else {
          stack_operation.push(sumbol)
        }
        break;
      case '(':
        stack_operation.push(sumbol);
        break;
      case ')':
        stack_operation, out_array = close_sc(stack_operation, out_array);
        break;
      default:
        out_array.push(sumbol);
    }
  }

  let inc = 0;
  let len_stack = stack_operation.length;
  while (len_stack !== inc)
  {
    out_array.push(stack_operation.pop());
    inc ++;
  }

  let elem = "Выражение в польской нотации: " + out_array;
  document.getElementById('myTextarea').value += elem + "\n";
}

function left(sumbol, stack_operation, out_array)
{
  let lvl = priority(sumbol);
  let len = stack_operation.length - 1;
  while (lvl <= priority(stack_operation[len]))
  {
    out_array.push(stack_operation.pop());
    len = stack_operation.length - 1;
  }
  stack_operation.push(sumbol);
  return stack_operation, out_array;
}

function right(sumbol, stack_operation, out_array)
{
  let lvl = priority(sumbol);
  let len = stack_operation.length - 1;
  while (lvl <= priority(stack_operation[len]))
  {
    out_array.push(stack_operation.pop());
    len = stack_operation.length - 1;
  }
  stack_operation.push(sumbol);
  return [stack_operation, out_array];
}

function close_sc(stack_operation, out_array)
{
  let element = "";
  while (element !== "(")
  {
    try
    {
      element = stack_operation.pop();
    }
    catch (e)
    {
      let elem = "Скобки раставленны неверно.";
      document.getElementById('myTextarea').value += elem + "\n";
    }
    out_array.push(element);
  }

  out_array.pop();
  // Если после этого шага на вершине стека оказывается символ функции, выталкиваем его в выходную строку.
  return stack_operation, out_array;

}

function priority(x)
{
  if (x === "^"){ return 4 }
  if (x === "*" || x === "/") {return 3}
  if (x === "+" || x === "-") {return 2}
  if (x === "(" || x === ")") {return 1}
}



/*
  ^    высокий       Справа налево. Правоассоц.
  * /  средний       Слева направо. Левоассоц.
  + -  низкий        Справо налево. Правоассоц.
  ( )  самый низкий

    •	Если символ является оператором о1, тогда:
  1) пока…
  … (если оператор o1 право-ассоциированный) приоритет o1 меньше приоритета оператора, находящегося на вершине стека…
  … (если оператор o1 ассоциированный, либо лево-ассоциированный) приоритет o1 меньше либо равен приоритету оператора, находящегося на вершине стека…
  … выталкиваем верхние элементы стека в выходную строку;
  2) помещаем оператор o1 в стек.
  •	Когда входная строка закончилась, выталкиваем все символы из стека в выходную строку. В стеке должны были остаться только символы операторов; если это не так, значит в выражении не согласованы скобки.

*/

/*
Пока есть ещё символы для чтения:
•	Читаем очередной символ.
•	Если символ является числом, добавляем его к выходной строке.
•	Если символ является символом функции, помещаем его в стек.
•	Если символ является открывающей скобкой, помещаем его в стек.
•	Если символ является закрывающей скобкой:
До тех пор, пока верхним элементом стека не станет открывающая скобка, выталкиваем элементы из стека в выходную строку.
 При этом открывающая скобка удаляется из стека, но в выходную строку не добавляется.
 Если после этого шага на вершине стека оказывается символ функции, выталкиваем его в выходную строку.
 Если стек закончился раньше, чем мы встретили открывающую скобку, это означает, что в выражении либо неверно поставлен разделитель, либо не согласованы скобки.

•	Если символ является оператором о1, тогда:
1) пока…
… (если оператор o1 право-ассоциированный) приоритет o1 меньше приоритета оператора, находящегося на вершине стека…
… (если оператор o1 ассоциированный, либо лево-ассоциированный) приоритет o1 меньше либо равен приоритету оператора, находящегося на вершине стека…
… выталкиваем верхние элементы стека в выходную строку;
2) помещаем оператор o1 в стек.
•	Когда входная строка закончилась, выталкиваем все символы из стека в выходную строку.
 В стеке должны были остаться только символы операторов; если это не так, значит в выражении не согласованы скобки.
*/

