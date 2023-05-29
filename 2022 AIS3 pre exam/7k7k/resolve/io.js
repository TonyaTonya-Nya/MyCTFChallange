


var 正閱 = "data";
var 已閱 = "end";

//const 讀行 = require("readline").createInterface(process.stdin, process.stdout);

var 化言 = 甲 => {
  const _ans2 = 甲.toString();
  return _ans2;
};

var 發生 = 事 => {
  const _ans3 = ((event) => process.stdin.emit(event))(事);
};


var 監聽 = 事件 => 響應 => {
  const _ans4 = ((event) => ((func) => process.stdin.on(event, func)))(事件)(響應);
};

var 聽寫 = 事件 => 響應 => {
  const _ans5 = ((event) => ((func) => 讀行.on(event, func)))(事件)(響應);
};

var 閱止 = () => {
  const _ans6 = (() => process.stdin.end())();
};

var 輸出 = 文 => {
  const _ans7 = ((s) => process.stdout.write(s))(文);
};