$.ajax({
    dataType:'jsonp',
    url:'http://123.206.194.97'+'/test.php',
    data:{
        msg:'hello'
    },
    success:function(res){
        var p = document.createElement('p');
        p.textContent = res.msg;
        document.body.appendChild(p);
    }
});