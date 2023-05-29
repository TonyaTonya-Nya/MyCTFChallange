const fs = require('fs');


function reverseF1(arg1, arg2) {
  var arr_A = [], int_A = 0x0, str_A, str_B = '';

  // 填0-255
  for (var i = 0x0; i < 0x100; i++) {
      arr_A[i] = i;
  }

  for (i = 0x0; i < 0x100; i++) {
      int_A = (int_A + arr_A[i] + arg1['charCodeAt'](i % arg1['length'])) % 0x100;
      str_A = arr_A[i];
      arr_A[i] = arr_A[int_A];
      arr_A[int_A] = str_A;
  }

  i = 0x0;
  int_A = 0x0;
  for (var i = 0x0; i < arg2['length']; i++) {
      i = (i + 0x1) % 0x100;
      int_A = (int_A + arr_A[i]) % 0x100;
      str_A = arr_A[i];
      arr_A[i] = arr_A[int_A];
      arr_A[int_A] = str_A;
      str_B += String['fromCharCode'](arg2['charCodeAt'](i) ^ arr_A[(arr_A[i] + arr_A[int_A]) % 0x100]);
  }
  return str_B;
}




const base64Data = fs.readFileSync('C:\\Users\\a0979\\Downloads\\a2\\flag.txt.ais3', 'utf8');

// 將 base64 資料還原為 Buffer 物件
const buf = Buffer.from(base64Data, 'base64');

// 將 Buffer 轉換為原始形式
const originalData = buf.toString('utf8');

console.log(originalData);

// 使用反向還原函式來解碼
var originalText = reverseF1('aaa', originalData);
console.log(originalText);


