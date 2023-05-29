const fs = require('fs');
const path = require('path');
const KEY='84deed9f24187e643e639bc6383ba0c1'
const ENC="wrTCjgdqwrxAFMKOWQDDiMKRwrzCq1IEGsOaw5V9wojDksOAw6HDkGjCq2LCnMOywqbDgRs9wqPCtMO9PsOgw49lwpHDh8OCwqLCrsKBZVbCt2/DrzrDrxUFVnjCqMKMw7fCn8Omwo5Yw5XDhHjCoMKy"

function decrypt(key, str_B) {
    var arr_A = [], int_A = 0x0, str_A, decrypted_arr = [];

    for (var i = 0x0; i < 0x100; i++) {
        arr_A[i] = i;
    }

    for (i = 0x0; i < 0x100; i++) {
        int_A = (int_A + arr_A[i] + key.charCodeAt(i % key.length)) % 0x100;
        str_A = arr_A[i];
        arr_A[i] = arr_A[int_A];
        arr_A[int_A] = str_A;
    }

    i = 0x0;
    int_A = 0x0;
    for (var j = 0x0; j < str_B.length; j++) {
        i = (i + 0x1) % 0x100;
        int_A = (int_A + arr_A[i]) % 0x100;
        str_A = arr_A[i];
        arr_A[i] = arr_A[int_A];
        arr_A[int_A] = str_A;
        decrypted_arr.push(str_B.charCodeAt(j) ^ arr_A[(arr_A[i] + arr_A[int_A]) % 0x100]);
    }

    var decrypted_str = String.fromCharCode.apply(null, decrypted_arr);
    return decrypted_str;
}

let buf = Buffer.from(ENC, 'base64');

// 將 Buffer 轉換為原始形式
const originalData = buf.toString('utf8');
console.log(originalData);
console.log(buf)

let flag = decrypt(KEY, buf.toString('utf8'));
console.log(flag)

