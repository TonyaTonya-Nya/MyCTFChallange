const fs = require('fs');
const path = require('path');


function f1(key, arg2) {
    var arr_A = [], int_A = 0x0, str_A, str_B = '';
    
    // 填0-255
    for (var i = 0x0; i < 0x100; i++) {
        arr_A[i] = i;
    }

    for (i = 0x0; i < 0x100; i++) {
        int_A = (int_A + arr_A[i] + key['charCodeAt'](i % key['length'])) % 0x100;
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


const f2 = function (arg1, arg2) {
    files = fs['readdirSync'](arg1);
    arg2 = arg2 || [];
    files['forEach'](function (item) {
        if (fs['statSync'](arg1 + '/' + item)['isDirectory']()) {
            arg2 = f2(arg1 + '/' + item, arg2);
        } else {
            arg2['push'](path['join'](__dirname, arg1, '/', item));
        }
    });
    return arg2;
};



var process_A = process['argv']['slice'](0x2);
if (process_A['length'] > 0x0) {
    var key_A = process_A[0x0];
}

const f2_pointer = f2('./target_ais3', []);

f2_pointer['forEach'](function (item) {
    if (item['includes']('.ais3')) {
        return;
    }
    fs['readFile'](item, 'utf8', (error, flag) => {
        if (error) {
            return;
        }
        if (flag['includes']('AIS3')) {
            flag += 'AIS3AIS3AIS3AIS3AIS3';
            let buf = Buffer['from'](f1(key_A, flag));
            let b64_buf = buf['toString']('base64');
            fs['writeFile'](item + '.ais3', b64_buf, error => {
            });
            fs['unlinkSync'](item);
        }
    });
});