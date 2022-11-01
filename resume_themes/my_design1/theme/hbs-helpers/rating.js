const { SafeString } = require('handlebars');

const rating = (level) => {
  

  return new SafeString(`<div style="height:4px;width:100px;background:#eee;border-radius:10px;"><div style="height:100%;background:#ccc;width:${level*100/5}%;border-radius:10px;"></div></div>`);
};




module.exports = { rating};
