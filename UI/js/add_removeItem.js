function addElement(){
    var total_text=document.getElementsByClassName("input_text");
    total_text=total_text.length+1;
    document.getElementById("field_div").innerHTML=document.getElementById("field_div").innerHTML+
    "<p id='input_text"+total_text+"_wrapper'><input type='text' class='input_text' id='input_text"+total_text+"' placeholder='Enter bucketlist item'>&nbsp<input class ='removeBtn' type='button' value='remove' onclick=remove_field('input_text"+total_text+"');></p>";
  }

function remove_field(id){ 
  document.getElementById("field_div").removeChild(document.getElementById(id+"_wrapper"));

}
