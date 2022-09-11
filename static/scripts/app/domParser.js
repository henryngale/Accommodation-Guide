const DomParser = require('dom-parser');
const fs = require("fs");

let parser = new DomParser();

export class DomParsing{
    parse(file){
        fs.readFile(file, 'utf8', function(err, html){
          if (!err){
            let dom = parser.parseFromString(html);

            return dom
          }
        })
    }
}



