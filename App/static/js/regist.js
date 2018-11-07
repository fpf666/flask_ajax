$(function () {
    // alert('111');
    $('#name').blur(function () {
        // alert('2222')
        var name = $(this).val()
        $.ajax({
            url : '/regist/',
            type : 'GET',
            data: {'name' : name},
            success : function (data) {
                if(data.code==400){
                    $('#message').html('请输入姓名').css('color','red');

                }
                if(data.code==410){
                    $('#message').html('名字已被注册').css('color','red');

                }
                if(data.code==200){
                    $('#message').html('名字可用').css('color','green');

                }
            }
        })
    })
    $('#button').click(function () {
        var name = $('#name').val();
        var password = $('#password').val();
        var age = $('#age').val();
        var sex = $('input:radio[name="sex"]:checked').val();
        // alert(sex)
        $.ajax({
            url:'/regist/',
            type:'POST',
            data:{
                'name':name,
                'password':password,
                'age':age,
                'sex':sex,
            },
            success:function (data) {
                // alert(data)
                if(data.code == 400){
                    alert('请输入数据')
                }
                if(data.code == 200){
                    // alert("xxxxx")
                    window.location.href= 'base.html'
                }
            }

        })
    });

})