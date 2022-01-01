let btn_add_value = $("#btn-add-value")
let container_add_value = $("#container-values")
let form_create_post = $("#form-create-post")
let id_name = $("#id_name")
let id_description = $("#id_description")
let id_symbol = $("#id_symbol")
let id_values =$("#id_values")
let submit_click = $("#submit_click")
let click_detail_graph = $(".click-detail-graph")
let new_chart = false
let myChart

function  array_chart(params) {

    const labels =params;
    
      const data = {
        labels: labels,
        datasets: [{
          label: 'Detalle Movimientos',
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data: params,
        }]
      };
    
      const config = {
        type: 'line',
        data: data,
        options: {}
      };

      return config
    
}

function desencode_base_64(vals){
    
    return decodeURIComponent(escape(window.atob( vals )));
}

function remove_btn(event){
    div_before = $(event).parents('.container-btn-more')
    div_before.remove()
}
function validate_name(){


    if(validate_if_null(id_name.val())&& id_name.val().length<51)return true

    return false


}
function validate_description(){

    if(validate_if_null(id_description.val())&& id_description.val().length<100)return true

}
function validate_symbols(){

    if(validate_if_null(id_symbol.val())&& id_symbol.val().length<11)return true

}
function validate_value(){

    data = container_add_value.find('input:not([type=file]):not([name^=extra]):not([type=checkbox]), select, textarea')
   
    list_data = list_values(data)

    if (list_data){

        encode_base_64 = window.btoa(unescape(encodeURIComponent( list_data )))

        id_values.val(encode_base_64)


        return true
    }else{
        return false
    }
   
    
}
function validate_if_null(element){

    if ( element != "") return true

    return false

}

function input_dom(){
    container_add_value.append("<div class='row container-btn-more'><div class='col-7'><input type='number' class='value-input'></div><div class='col-2'><button id='remove-value' onclick='remove_btn(this)'>Remove</button></div></div>")

}

function  list_values(elements) {

    var list_value=""
    
    var formData = elements.filter(function() {
        if(validate_if_null(this.value))list_value += this.value+",";
      return this.value != ''
    }).serialize()


    return list_value

  }


btn_add_value.click(function() {

    _input = input_dom()
  
  });

  submit_click.click(function(e){
    e.preventDefault();

    if(validate_name() && validate_description() && validate_symbols() && validate_value()){

        form_create_post.submit();
    }else{
        alert("algo salio mal")
    }
    
});


click_detail_graph.click(function(){

    if(new_chart){
       
        myChart.destroy();
    }

    new_chart = true
    
    encode_base = $(this).data("vals")
    data_desencode = desencode_base_64(encode_base)
    array_data=data_desencode.split(','); 
    console.log(array_data)
    config = array_chart(array_data)
   
   
    myChart = new Chart(
    document.getElementById('myChart'),
    config
  );

})

