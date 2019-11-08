function buttonClick (e){
    nameCheck(e);
  }; //event handler
  //same as other one, only new stuff will be commented
function nameCheck(e){
    var name=document.getElementById("name").value; 
    var nameGood = false;
    var nameLength = name.length
    // badSymbol shortened to BS in some Var
    var badSymbol = ["~", "`", "!", "@", "$", "#", "%", "^", "&", "*", "(", ")",
       "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "+", "=", "{", "[",
        "}", "]", "|", "\\", ":", ";", "\"", "<", ",", ">", ".", "?", "/" ];
    var bSArrayLength= badSymbol.length;
    var bSInName = false;
    var placeSpace = name.includes(" ");  // the regex below won't pick up spaces in the name, just at the start, so this and the if statment that is with it, stop there from being any spaces in the name.
    var placeHyphen = name.indexOf("-")
    var placeApostrophe = name.indexOf("'")
    while(nameGood === false){
      if (name === "Your name"){
        alert("Hello Stranger, please enter a name and try again.")
        break;
      }
      for( i=0; i<bSArrayLength; i++){
        var characterCheck = badSymbol[i];
        var nameHasBS = name.includes(characterCheck);
        if (nameHasBS === true){
          bSInName = true;
        };
      };
      if(bSInName === true){
        alert("Name can't have special characters, letters only.");
        break;
      } else if (/^ +$/.test(name)){ //RegEx to check for just spaces
        alert("Just spaces isn't a name.");
        break;
      }else if (placeSpace === true){
        alert("Please just a single name, too many spaces is weird. (First name maybe?)");
        break;
      }else if(nameLength === 0){
        alert("Please enter a name.");
        break; 
      } else if(nameLength === 1 || nameLength > 20){
        alert("Your name should be between 2 and 20 characters");
        break;
      } else if (placeHyphen === 0 || placeApostrophe === 0 || 
          placeHyphen === (nameLength-1) || placeApostrophe === (nameLength-1)){
        alert("Names can have hyphens and apostrophes, but not at the start and the end.");
        break;
      } else{
        nameGood = true;
      };
    };
    if (nameGood === true){
      alert("Hello " + name +". Thanks for visting this webpage on Web Design");
    };
  };