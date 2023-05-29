var 正閱 = "data";
var 已閱 = "end";

var 始碼  = 字 => {
    return  String.fromCharCode(字);
};

var 字址  = 字 => 址 => {
    return ((target) => ((idx) => target.charCodeAt(idx)))(字)(址);
   
};

var 始於 = 字 => 符 => {
    return ((target) => ((label) => target.startsWith(label)))(字)(符);

};

/**
 * 去頭
 */
var 字子 = 字 => 址 => {
    return ((target) => ((idx) => target.substring(idx)))(字)(址);
};

/** 
 * 抓子字串=>子字(123456)(1)(3)=>234
*/
var 子字  = 字 => 始 => 末 => {
    return ((target) => ((s) => ((e) => target.substring(s, e))))(字)(始)(末);
};