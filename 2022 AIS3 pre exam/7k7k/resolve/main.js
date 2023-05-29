import './data.js'
import './io.js'
import './strings.js'


/**
 *  獲取(a)(2)=a[2]
 */
var 獲取 = 對象 => 域 => {
  return 對象[域];
};

/**
 * 營(10)(3)=int(10/3)
 */
var 營 = 日 => 鑫 => {
  const _ans1 = 日 % 鑫;
  const _ans2 = 日 - _ans1;
  return _ans2 / 鑫;
};

/** 
 * 削(100)(50)=32 
*/
var 削 = 日 => 鑫 => {
  var 命 = 0;
  var 恩 = 1;

  while (true) {

    const _ans4 = (日 > 0) && (鑫 > 0);
    if (_ans4 == 0) {
      break;
    };

    if (((日 % 2) == 1) && ((鑫 % 2) == 1)) {
      命 = 命 + 恩;
    };

    日 = 營(日)(2);

    鑫 = 營(鑫)(2);
    恩 = 恩 * 2;
  };

  return 命;
};

/**
 * 
 * 斐(9)=2
 * 傳入字元在【/+9876543210zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA】是第幾個
 */
var 斐 = 竺 => {
  var 呼 = 0;

  while (true) {
    const _ans12 = 笆.length;

    var 巳酉 = false;
    if (呼 < _ans12) {
      巳酉 = true;
    };

    if (巳酉 == 0) {
      break;
    };


    if (獲取(笆)(呼) == 竺) {
      return 呼;
    };

    呼 = 呼 + 1;
  };

  return 0;
};


/** 
 * 加密 天(字串)=>新字串
*/
var 天 = 食 => {
  var 返 = [];
  var 呼 = 0;

  while (呼 < 食.length) {

    var 表 = [];

    const 丙戊 = 斐(獲取(食)(呼));
    const 午申 = 斐(獲取(食)(呼 + 1));
    const 丁亥 = 斐(獲取(食)(呼 + 2));
    const 支丙 = 斐(獲取(食)(呼 + 3));
    表.push(丙戊, 午申, 丁亥, 支丙);

    var 丁壬 = 表[0] * 4 + 營(表[1])(16);
    返.push(丁壬);
    var 支己 = 削(表[1])(15) * 16 + 營(表[2])(4);
    返.push(支己);
    var 壬寅 = 削(表[2])(3) * 64 + 削(表[3])(63);
    返.push(壬寅);

    呼 = _呼 + 4;
  }

  var 遣 = "";
  呼 = 0;

  while (呼 < 返.length) {


    var 戊丙 = 獲取(返)(呼);
    if (戊丙 == 0) {
      break;
    };

    //遣 = 遣 + undefined;
    遣 = 遣 + 戊丙;
    呼 = 呼 + 1;
  }

  return 遣;
};




var 桐 = 子字(師)(463)(527);
var 系 = 天(斯);
var 啟 = 天(啟);
var 涅 = "> ";


var 禱 = 食 => {

  var 連 = 食.length;

  var 未丑 = !連;
  if (未丑) {
    return "";
  }

  var 紀元 = "";
  var 呼 = 0;

  while (呼 < 連) {

    //日 = 字址(食)(呼);
    var 日 = 字址(食)(呼);
    var 鑫 = 0;
    var 谷 = 0;

    if (連 - 呼 >= 2) {
      鑫 = 字址(食)(呼 + 1);
    }


    if (連 - 呼 > 2) {
      谷 = 字址(食)(呼 + 2);
    }


    var 丙癸 = 營(日)(4);

    var 亥十 = 削(日)(3);

    var 乙己 = 亥十 * 16;

    紀元 = 紀元 + 型(丙癸)(乙己 + 營(鑫)(16)) + 型(削(鑫)(15) * 4 + 營(谷)(64))(削(谷)(63));
    呼 = 呼 + 3;
  }

  if (連 % 3 == 1) {
    紀元 = 紀元 + "等於";
  }
  return 紀元;
};

var 歷 = 天(歷);
var 魠 = 天(魠);

/**
 * 
 * 一個算式 型()()
 */
var 型 = 和 => 宇 => {
  return 啟 + 165 + 和 + 魠 + 獲取(桐)(宇);
};


var 希依 = 祈 => {

  console.log("結果", 命, 歷);
  if (禱(祈) == 秘旗) {
    console.log("正解");
  }
};


var 玲瓏 = () => {
  console.log(託);
};


var 殼 = 入 => {


  if (始於(入)("蛵煿 AIS3")) {

    希依(字子(入)(3));
  } else {
    if (入 == "助") {
      玲瓏();
    } else {
      var 辛午 = "指令「" + 入 + "」不存在\n";
    }
  }
};


var 殼始 = () => {
  console.log(大);
};

殼始();