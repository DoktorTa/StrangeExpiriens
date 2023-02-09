function rleESCEncodingStart(){
  let text =  document.RLE.RLEString.value;
  let elem = "Исходное выражение (До кодирования): " + text;
  document.getElementById('myTextarea').value += elem + "\n";
  _rleESCEncoding(text);
}

function rleJUMPEncodingStart(){
  let text =  document.RLE.RLEString.value;
  let elem = "Исходное выражение (До кодирования): " + text;
  document.getElementById('myTextarea').value += elem + "\n";
  _rleJUMPEncoding(text);
}

function rleESCDecodingStart(){
  let no_decoding_string = document.RLE.RLEString.value;
  let elem = "Исходное выражение (До декодирования): " + no_decoding_string;
  document.getElementById('myTextarea').value += elem + "\n";
  _rleESCDecoding(no_decoding_string);
}

function rleJUMPDecodingStart(){
  let no_decoding_string = document.RLE.RLEString.value;
  let elem = "Исходное выражение (До декодирования): " + no_decoding_string;
  document.getElementById('myTextarea').value += elem + "\n";
  debugger
  _rleJUMPDecoding(no_decoding_string);
}

function _rleJUMPEncoding(noEncodingString){
  let out = ""
  let rule = 0

  for (let i = 0; i < noEncodingString.length; i++) {
    let symbol = noEncodingString[i]
    let count = 1
    let stringSymbols = ""

    if (symbol === noEncodingString[i + 1]){
      rule = 1
      stringSymbols = symbol

      while (symbol === noEncodingString[i + 1]){
        count++
        i++
      }

      while (count > 127){
        out += String.fromCharCode(127) + symbol
        count -= 127
      }

      out += String.fromCharCode(count) + symbol

    } else {
      rule = 0
      stringSymbols += symbol

      while (symbol !== noEncodingString[i + 1] && noEncodingString[i + 1] !== undefined){

        if (noEncodingString[i + 1] === noEncodingString[i + 2]){
          break
        }

        symbol = noEncodingString[i + 1]
        stringSymbols += symbol
        count++
        i++

      }

      while (count > 128){
        out += String.fromCharCode(256) + stringSymbols
        count -= 128
      }
      out += String.fromCharCode(128 + count) + stringSymbols
    }

  }

  let elem = "Исходное выражение (После кодирования): " + out;
  document.getElementById('myTextarea').value += elem + "\n";
}
// ASASASAS
function _rleJUMPDecoding(noDecodingString){

  let out = ""

  while (noDecodingString.length !== 0) {

    let jump = noDecodingString.charCodeAt(0)

    if (jump < 128) {
      let symbol = noDecodingString[1]

      while (jump !== 0){
        out += symbol
        jump--
      }

      noDecodingString = noDecodingString.slice(2)

    } else if (jump > 127){

      let stringSymbols = noDecodingString.slice(1, jump - 127)
      out += stringSymbols
      noDecodingString = noDecodingString.slice(jump - 127)

    }
  }

  let elem = "Исходное выражение (После кодирования): " + out;
  document.getElementById('myTextarea').value += elem + "\n";
}

function _rleESCEncoding(noEncodingString) {
  let symbol = 0
  let out = ""
  let escSymbol = "#"
  debugger

  for (let i = 0; i < noEncodingString.length; i++){
    let count = 1

    symbol = noEncodingString[i]
    while (symbol === noEncodingString[i + 1]){
      count += 1
      i++
    }

    let escQueue = ""
    if (count > 1){
      while(count > 256){
        out += escSymbol + String.fromCharCode(256) + symbol
        count -= 256
      }
      out += escSymbol + String.fromCharCode(count) + symbol
    } else {
      out += escQueue + symbol
    }
  }

  let elem = "Исходное выражение (После кодирования): " + out;
  document.getElementById('myTextarea').value += elem + "\n";
}

function _rleESCDecoding(noDecodingString){
  let out = ""


  for (let i = 0; i < noDecodingString.length; i++){
    let symbol = noDecodingString[i]

    if (symbol === "#"){

      let count_int = noDecodingString.charCodeAt(i + 1);
      symbol = noDecodingString[i + 2]

      while (count_int !== 0){
        out += symbol
        count_int--
      }

      i += 2

    } else {
      out += symbol
    }
  }

  let elem = "Исходное выражение (После декодирования): " + out;
  document.getElementById('myTextarea').value += elem + "\n";
}
