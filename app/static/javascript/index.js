$(function(){
  $('.open').on('click', function(){
    var nameTag = $(this).attr('name');
    console.log(nameTag)
    $.ajax({
      data : {
        title : nameTag
      },
      type : 'POST',
      url : '/set_content'
    })
    .done(function(data){
      console.log(data.error)
      location.href='/content';
    });
  });
});

$(function(){
  $('#new-button').on('mouseover', function(){
    $(this).css({
      'background-color': '#f7d9ab',
    });

    $('#plus').css({
      'color': '#EDAA28',
    });

    $('#new').css({
      'color': '#EDAA28',
    });
  });

  $('#new-button').on('mouseout', function(){
    $(this).css({
      'background-color': '#EDAA28',
    });

    $('#plus').css({
      'color': 'white',
    });

    $('#new').css({
      'color': 'white',
    });
  });
});

//sidemenu
$(function(){
  let duration = 300;
  let $trriger = $('#trigger');
  let $sidemenu = $('#sidemenu');
  let $trriger_close = $('#trigger-close');

  $trriger.on('click', function(){
    if(!$trriger_close.hasClass('open')){
        $sidemenu.stop(true).animate({
          left: 0
        }, duration);
        $trriger_close.addClass('open');
    }
  });

  $trriger_close.on('click', function(){
    $sidemenu.stop(true).animate({
      left: '-300px'
    }, duration);
    $(this).removeClass('open');
  });
});

//close
$(function(){
  $('#trigger-close').on('mouseover', function(){
    $('#left').css({
      'color': '#f7d9ab' 
    });
  });

  $('#trigger-close').on('mouseout', function(){
    $('#left').css({
      'color': '#EDAA28' 
    });
  });
});

//Home
$(function(){
  $('#side-item1').on('click', function(){
    location.reload();
  });
});

//Settings
$(function(){
  $('#side-item2').on('click', function(){
    location.href='/form';
  });
});

//chart
$(function(){
  $('#side-item3').on('click', function(){
    location.href='/chart';
  });
});

//graph
$(function(){
  $('#side-item4').on('click', function(){
    location.href='/graph';
  });
});

//point
$(function(){
  $('#side-item5').on('click', function(){
    location.href='/home';
  });
});