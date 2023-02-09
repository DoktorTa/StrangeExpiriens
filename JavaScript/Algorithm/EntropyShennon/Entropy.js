function entropyStartCount(){
  let no_entropy_string = document.Entropy.Counted.value;
  let elem = "Исходное выражение: " + no_entropy_string;
  document.getElementById('myTextarea').value += elem + "\n";
  _entropyCount(no_entropy_string);
}


function _entropyCount(no_entropy_string) {
  let str = "";
  let alph = [];
  let entrophy = 0;
  let signature_symbol = [];

// Составляем алфавит, если буквы нет в алфавите то добавим туда обозначив это единицей.
// Если буква уже там есть то инкрементируем число соответствующее букве
  for (let i = 0; i < no_entropy_string.length; i++) {

    if (!alph[no_entropy_string.charAt(i)]) {
      alph[no_entropy_string.charAt(i)] = 1;
      str = str + no_entropy_string.charAt(i);
    }
    else {
      alph[no_entropy_string.charAt(i)]++;
    }
  }

// Считаем H(X).
  for (let i = 0; i < str.length; i++) {
    let p_i = alph[str.charAt(i)] / no_entropy_string.length;
    let symble = -1 * p_i * (Math.log(p_i) / Math.log(str.length));
 
    if (isNaN(symble)){
      symble = 0;
    }
    alert(symble)
    signature_symbol.push("\n" + str.charAt(i)+ " " + p_i);
    entrophy = entrophy + symble;
  }

// Выводим энтропию строки
  let elem = "Сигнатуры символов: " + signature_symbol;
  elem = elem + "\n" + "Энтропия: " + entrophy;
  document.getElementById('myTextarea').value += elem + "\n";
}
