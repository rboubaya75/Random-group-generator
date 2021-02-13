
function groups()
{  
    let names = prompt("Enter the list of the names, separated by a comma").split(",");

    let groups = document.getElementById("groups").value;
    let PersPerGroup = document.getElementById("per_grp").value;

    let innerText = "<h4>List of names</h4> ";
    for(let i=0; i<names.length; i++) {
        innerText += names[i] + ",";
    }
    innerText += "<br/>\n";            


    names= shuffle(names);

    let finalGroups = new Array();

    for(let i=0; i<groups; i++) {
       
        let nameList= "";
        for(j=0; j< PersPerGroup; j++) {
            nameList += names[0] + ",";
            names.shift();
        }

        grpArr = nameList.substring(0,nameList.length - 1);
        finalGroups[i] = nameList;
    }




    innerText += "<h4>Groups</h4><br/>\n";
    innerText += "<table width='100%' border='1'><tr>\n";           
    for(let i=0; i<groups; i++) {
        // print groups
        let j=i+1;
        let nameList = finalGroups[i].split(",");
        innerText += "<td>Group " +j+"<br>";
        for(let k=0; k < nameList.length; k++){
          innerText += nameList[k] + "<br>";
        }

        innerText += "</td>\n";
    }
    innerText += "</tr></table>\n";

    document.getElementById("FinalGroups").innerHTML = innerText;

} 

function shuffle(array) {
   for ( i = array.length - 1; i > 0; i--) {
       var j = Math.floor(Math.random() * (i + 1));
       var temp = array[i];
       array[i] = array[j];
       array[j] = temp;
   }
   return array;
}
