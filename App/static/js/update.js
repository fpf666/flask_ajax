$(function () {
    $.ajax({
        url : '/update/',
        type: 'GET',
        success:function (data) {
            // alert(data.user.name)
            $('#id').val(data.user.id);
            $('#name').val(data.user.name);
            $('#age').val(data.user.age);
            $("input:radio[name='sex']").eq(data.user.sex).attr("checked",true);
        }
    })
    $('#update').click(function () {

        var name = $('#name').val();
        var age = $('#age').val();
        var sex = $("input:radio[name='sex']:checked").val();
        alert(sex)
        $.ajax({
            url : '/update/',
            type:'PUT',
            data:{
                'name':name,
                'age':age,
                'sex':sex,
            },
            success:function (data) {
                if(data.code==200){
                    window.location.href='base.html'
                }
                if(data.code==400){
                    alert('请输入值')
                }
            }
        })
    })
})