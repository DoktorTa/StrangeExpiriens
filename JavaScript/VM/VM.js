function VMNokStart(){
  debugger
  let text_program =
    "input a 12\n" +
    "input b 5\n" +
    "input zero 0\n" +
    "input m 0\n" +

    "mul ab a b\n" +

    "m while\n" +

    "mov nod b\n" +
    "mod m a b\n" +
    "if= m zero\n" +
    "goto ret\n" +

    "mov nod a\n" +
    "mod m b a\n" +
    "if= m zero\n" +
    "goto ret\n" +

    "if> a b 2\n" +
    "mod a a b\n" +
    "goto while\n" +

    "if> b a\n" +
    "mod b b a\n" +

    "goto while\n" +

    "m ret\n" +
    "div ans ab nod\n" +
    "output ans"
  let elem = "Текст программы: " + text_program;
  document.getElementById('myTextarea').value += elem + "\n";
  z(text_program);
}

function factorialStart(){
  let text_program =
    "input a 4.5\n" +
    // "add a a one\n" +
    "input i 1\n" +
    "input j 1\n" +
    "input ans 0\n" +
    "input ansStep 1\n" +
    "input one 1\n" +
    "input zero 0\n" +

    "m while\n" +

    "if= zero a\n" +
    "goto zeroRet\n" +
    "if> i a\n" +
    "goto ret\n" +

    // "add j j one\n" +  // 11 12 22
    "mul ansStep ansStep i\n" +
    "add i i one\n" +
    "goto while\n" +

    "m ret\n" +
    "output ansStep\n" +
    "return\n" +

    "m zeroRet\n" +
    "output one\n" +
    "return\n"

  let elem = "Исходное выражение: " + text_program;
  document.getElementById('myTextarea').value += elem + "\n";
  z(text_program);
}

function buildCommandQueue(text_command){
  return text_command.split("\n")
}


//ASDADSASFDFDDF
function z(program){
  let commandQueue = program.split('\n')
  let prog=[]
  let N = 0
  let mem = []

  while (N !== commandQueue.length )
  {
    prog[N] = commandQueue[N].split(' ')
    N++

    if (prog[N - 1][0] === 'm'){
      mem[prog[N - 1][1]] = N - 1
    }

  }
  debugger

  let flag = false
  for (let n = 0; n < commandQueue.length; n++){
    debugger

    if (flag) break;

    switch (prog[n][0])
    {


      case "mul":// mod answer one two
      {
        mem[prog[n][1]] = (+mem[prog[n][2]]) * (+mem[prog[n][3]])
        break;
      }

      case "div":
      {
        mem[prog[n][1]] = (+mem[prog[n][2]]) / (+mem[prog[n][3]])
        break;
      }
      case "input":{
        mem[prog[n][1]] = (+prog[n][2])
        break
      }

      case "mov":
      {
        mem[prog[n][1]] = mem[prog[n][2]]
        break;
      }

      case "mod":
      {
        mem[prog[n][1]] = mem[prog[n][2]] % mem[prog[n][3]]
        break;
      }

      case "add":
      {
        mem[prog[n][1]] =+ (+mem[prog[n][2]]) + (+mem[prog[n][3]])
        break;
      }

      case "sub":
      {
        mem[prog[n][1]] =+ mem[prog[n][2]] - mem[prog[n][3]]
        break;
      }

      case "output":
      {
        let elem = "Output: " + mem[prog[n][1]];
        document.getElementById('myTextarea').value += elem + "\n";
        break;
      }

      case "if>":
      {
        if (mem[prog[n][1]] > mem[prog[n][2]]) {
          break
        }

        if (prog[n][3] !== undefined){
          n += (+prog[n][3])
        } else {
          n++
        }
        break;
      }

      case "if=":
      {
        //WSH.echo(mem[prog[n][1]])
        if (mem[prog[n][1]] === mem[prog[n][2]]) {
          break;
        }
        n++
        break;
      }

      case "goto":
      {
        n = mem[prog[n][1]]
        break;
      }

      case "m":
      {
        break
      }

      case "return":
      {
        flag = true;
        break;
      }

      default:
      {
        let elem = "Output: " + prog[n][0];
        document.getElementById('myTextarea').value += elem + "\n";
      }
    }
  }
}


