 $(document).ready(function() {
    $('#changeStatus').change(function(){
        var category = $('#changeStatus').val();
         $.ajax({
              type: 'POST',
              url: '/list',
              data: {'category': category},
              dataType: "json",
              success: function(response){
                    var text = '<br>';
                    data = response.data;
                    var len = data.length;
                    for (i = 0; i < len; i++) {
                        text += '<div class="list-group-item list-group-item-action pop" title="'+ data[i][0] +'">' + data[i][3] + '</div>';
                    }
                    clicks_count(category);
                    $('#clickable').html(text);
                    $('div.pop').click(function() {
                        var data = $(this).attr('title');
                         $.ajax({
                              type: 'POST',
                              url: '/click',
                              data: {'id': data},
                              dataType: "json",
                              success: function(response){
                                    clicks_count(category);
                                    console.log(response);
                              },
                              error: function(error){
                                    console.log(error);
                                }
                         });
                      });
              },
              error: function(error){
                    console.log(error);
                }
         });
    });
    function clicks_count(category) {
        $.ajax({
              type: 'POST',
              url: '/sorted_data',
              data: {'category': category},
              dataType: "json",
              success: function(response){
                    var data = response.data;
                    var len = data.length;
                    var text = "<br>";
                    for (i = 0; i < len; i++) {
                        text += '<li class="list-group-item d-flex justify-content-between align-items-center">' + data[i][3] + '<span class="badge badge-primary badge-pill">' + data[i][2] + '</span> </li>'
                    }
                     $('#show').html(text);
              },
              error: function(error){
                    console.log(error);
                }
         });
    }
 });
