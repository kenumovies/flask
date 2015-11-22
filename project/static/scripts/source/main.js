var Handlebars = require('handlebars');

$('#search').keyup(function(e){
    e.preventDefault();
    var val = $('#search').html();
    var code = e.keyCode || e.which;
    if(code == 13) { //Enter keycode
        $("#results").html($('#spinner').html())
        $.getJSON('qasis', {
            query: $('#search').html()
        }, function(data) {
             render_results(data)
        });
    }
})

$('#info').click(function(e){
    var source   = $("#info_modal").html();
    var template = Handlebars.compile(source);
    $("#myModal").html(template());
})

var render_results = function(data){
    var data_dict = {};
    [].forEach.call(data.results, function(row){
        data_dict[row.id] = row;
    });

    var source   = $("#results_item").html();
    var template = Handlebars.compile(source);
    $("#results").html(template(data));
    new AnimOnScroll( document.getElementById( 'grid' ), {
        minDuration : 0.4,
        maxDuration : 0.7,
        viewportFactor : 0.2
    });

    $('.movie_card').click(function(e){
        var id = $(this).data("id");
        var movie_data = data_dict[id];
        var source   = $("#movie_modal").html();
        var template = Handlebars.compile(source);
        $("#myModal").html(template(movie_data));
    })
}

$('#myModal').on('shown.bs.modal', function (e) {
  $(".plot").dotdotdot();
})

/* center modal */
function centerModals($element) {
  var $modals;
  if ($element.length) {
    $modals = $element;
  } else {
    $modals = $('.modal-vcenter:visible');
  }
  $modals.each( function(i) {
    var $clone = $(this).clone().css('display', 'block').appendTo('body');
    var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
    top = top > 0 ? top : 0;
    $clone.remove();
    $(this).find('.modal-content').css("margin-top", top);
  });
}
$('.modal-vcenter').on('show.bs.modal', function(e) {
  centerModals($(this));
});

$(window).on('resize', centerModals);