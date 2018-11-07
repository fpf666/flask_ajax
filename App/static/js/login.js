$(function () {
    $('#button').click(function () {
        var name = $('#name').val()
        var password = $('#password').val()
        $.ajax({
            url : '/login/',
            type : 'POST',
            data: {
                'name': name,
                'password': password
            },
            success: function (data) {
                if(data.code == 400||data.code==401){
                    alert('密码或者用户名错误')
                }
                if(data.code==200){
                    window.location.href='base.html'
                }
            }
        })
    })
})