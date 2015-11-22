var Handlebars = require('handlebars');


$('#search').keyup(function(e){
    e.preventDefault();
    var val = $('#search').html();
    var code = e.keyCode || e.which;
    if(code == 13) { //Enter keycode
        $('#search').html(val.trim());
        $.getJSON('qasis', {
            query: $('#search').html()
        }, function(data) {
             console.log(data);
             render_results(data)
        });
    }
})

var render_results = function(data){
    var source   = $("#results_item").html();
    var template = Handlebars.compile(source);
    $("#results").html(template(data));
    new AnimOnScroll( document.getElementById( 'grid' ), {
        minDuration : 0.4,
        maxDuration : 0.7,
        viewportFactor : 0.2
    } );
        
}

