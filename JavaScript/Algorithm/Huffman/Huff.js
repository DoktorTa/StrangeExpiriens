let codes_ = {}

function huffStart(){
  debugger;
  let text = document.HuffT.Counted.value;
  let elem = "Исходное выражение: " + text;
  document.getElementById('myTextarea').value += elem + "\n";
  encodeHuff(text);
}

function huffDecodeStart(){
  debugger
  let text = document.HuffT.Counted.value;
  let elem = "Исходное выражение: " + text;
  document.getElementById('myTextarea').value += elem + "\n";
  decodeHuff(text);
}

function decodeHuff(text){
  let codeSymbol = ""
  let out = ""
  let codes = reversedMap(codes_)
  let maxLenCode = getMaxLenCode(codes_)
  let symbol = ""

  debugger
  for (let i = 0; i < text.length; i++){
    debugger
    codeSymbol += text[i]
    if (codeSymbol.length === maxLenCode) {

      for (let j = 0; j < maxLenCode; j++){

        codeSymbol = codeSymbol.slice(j, maxLenCode)
        if (codes[codeSymbol] !== undefined) {
          symbol = codes[codeSymbol]
          codeSymbol = ""
          i -= j
        }
      }

      out += symbol
    }
  }

  let elem = "Закодированный текст (биты): " + out;
  document.getElementById('myTextarea').value += elem + "\n";
}

function getMaxLenCode(rule){
  let maxLen = 0

  let keys = Object.keys(rule);

  keys.forEach(function (key){
    if (key.length > maxLen){
      maxLen = key.length
    }
  })

  return maxLen + 1
}

function reversedMap(rule){
  let rule2 = {};   // empty object to contain reversed key/value paris

  let keys = Object.keys(rule);   // first get all keys in an array

  keys.forEach(function(key){
    let val = rule[key];   // get the value for the current key
    rule2[val] = key;      // reverse is done here
  });

  return rule2;
}

function encodeHuff(text){
  let ferq = getFerq(text);
  debugger;
  let symbols = [];
  for (let i in ferq){
    symbols[i] = "";
  }


  while (1 < ferq.length){
    debugger;

    let ans = popMin(ferq);
    let letter_1 = ans[0];
    let min_1 = ans[1];
    ferq = ans[2];

    let ans_2 = popMin(ferq);
    let letter_2 = ans_2[0];
    let min_2 = ans_2[1];
    ferq = ans_2[2];

    ferq[letter_1 + letter_2] = min_1 + min_2;

    for (let i = 0; i < letter_1.length; i++){
      let lett = letter_1.charAt(i);
      symbols[lett] = symbols[lett] + "1";
    }

    for (let i = 0; i < letter_2.length; i++){
      let lett = letter_2.charAt(i);
      symbols[lett] = symbols[lett] + "0";
    }

  }

  codes_ = symbols
  printCodes(symbols, text);

}

function printCodes(cod, text){
  //Вывод кодов символов
  debugger;
  let alCodes = "Коды символов:\n";
  for (let i in cod){
    alCodes += i + ": " + cod[i] + ",\n";
  }
  document.getElementById('myTextarea').value += alCodes;

  // Вывод закодированного текста
  let encodeText = "";
  for (let i = 0; i < text.length; i++){
    encodeText += cod[text.charAt(i)];
  }

  let elem = "Закодированный текст (биты): " + encodeText;
  document.getElementById('myTextarea').value += elem + "\n";

  text = "";
  for (let i = 0; i < encodeText.length; i = i + 8){
    let code_ch = parseInt(encodeText.slice(i, i + 8), 2);
    text += String.fromCharCode(code_ch);
  }

  elem = "Закодированный текст (символы): '" + text + "'";
  document.getElementById('myTextarea').value += elem + "\n";

}

function popMin(ferq){
  let min = 1000000;
  let letter = "";
  for (let i in ferq){
    if (ferq[i] <= min){
      min = ferq[i];
      letter = i;
    }
  }

  let len = 0;
  let f = [];
  for (let i in ferq){
    len++;
    if (i !== letter){
      f[i] = ferq[i];
    }
  }

  f.length = len;

  return [letter, min, f]
}

function getFerq(text){
  let symbols = [];

  for (let i = 0; i < text.length; i++) {
    if (!symbols[text[i]]) {
      symbols[text[i]] = 0;
    }
    symbols[text[i]]++;
  }

  let table_ferq = "";
  let len = 0;
  for (let i in symbols){
    len++;
    table_ferq += " " + i + ": " + symbols[i] + ",";
  }
  symbols.length = len;

  let elem = "Таблица встречаемости: " + table_ferq;
  document.getElementById('myTextarea').value += elem + "\n";

  return symbols;
}

