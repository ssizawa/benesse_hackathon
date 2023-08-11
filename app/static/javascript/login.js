$("#login").click(function(){
  var json = {
    username : $('#name').val(),
    password : $('#password').val()
  };
  console.log(json.username);
  $.ajax({
    data : {
      username : $('#name').val(),
      password : $('#password').val()
    },
    type : 'POST',
    url : '/verify'
  })
  .done(function(data){
    if(data.user_name=='0'){
      alert(data.error)
      location.reload();
    }else{
      // alert(data.error)
      location.href='/form';
    }
  });
});