function buttonClick (e){
    nameCheck(e);
  }; //event handler in index.html, there is some code in the button that calls this function
  
function nameCheck(e){
    var name=document.getElementById("name").value; //gets the value of the text box
    // variable declaring
    var nameGood = false;
    var nameLength = name.length
    // badSymbol shortened to BS in some Var
    var badSymbol = ["~", "`", "!", "@", "$", "#", "%", "^", "&", "*", "(", ")",
       "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "+", "=", "{", "[",
        "}", "]", "|", "\\", ":", ";", "\"", "<", ",", ">", ".", "?", "/"]; // array (list) of bad symbols
    var bSArrayLength= badSymbol.length;
    var bSInName = false;
    var placeHyphen = name.indexOf("-")   //for those other symbols
    var placeApostrophe = name.indexOf("'")
    while(nameGood === false){   //to keep repeating untill it works
      if (name === "Your name"){
        alert("Hello Stranger, please enter a name and try again.")
        break;  // breaks while loop if the defualt value is submitted
      }
      for( i=0; i<bSArrayLength; i++){   //for loop to check for the BS
        var characterCheck = badSymbol[i];
        var nameHasBS = name.includes(characterCheck);
        if (nameHasBS === true){
          bSInName = true;
        };
      };
      //alerts for different problems with the names (in if statments)
      if(bSInName === true){
        alert("Name can't have special characters, letters only.");
        break;
      } else if(nameLength === 0){
        alert("Please enter a name.");
        break; 
      } else if(nameLength === 1 || nameLength > 20){  // "||"=OR
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
    }; // alerting with correct name
  };