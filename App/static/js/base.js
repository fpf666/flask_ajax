$(function () {
    alert('^^^^^^^^^^')
    //加载数据
    $.ajax({
        url :'/base/',
        type: 'GET',
        success: function (data) {
            // alert(data.users)
            //添加表格数据
            for(var i = 0;i< data.users.length;i++){
                // alert(i)
                var id = '<td>'+data.users[i].id+'</td>';
                var name = '<td>'+data.users[i].name+'</td>';
                var age = '<td>'+data.users[i].age+'</td>';
                var sex = '<td>'+data.users[i].sex+'</td>';
                var up = '<td><button class="update" value="'+data.users[i].id+'">修改</button></td>';
                var de = '<td><button class="delete" value="'+data.users[i].id+'">删除</button></td>';
                var trHtml = '<tr id="'+data.users[i].id+'">'+id+name+age+sex+up+de+'</tr>';
                $('#table').append(trHtml);
            }

            //添加页码
            var prev='<button value="prev">上页</button>';
            var next='<button value="next">下页</button>';
            $('#page').append(prev)
            for(var j = 1;j <= data.pages; j++){
                var page = '<button value="'+j+'">'+j+'</button>';
                $('#page').append(page);
            }
            $('#page').append(next);
        }
    });
    //实现根据页码跳转页面
    $('#page').on('click','button',function () {
        // alert('1111');
        var page = $(this).val();
        // alert(page);
        $.ajax({
            url:'/base/',
            type: 'PUT',
            data: {
                'page':page
            },
            success: function (data) {
                if(data.code == 200){
                    window.location.href='base.html'
                }
            }
        });
    });
    //跳转到添加页面
    $('#add').click(function () {
        window.location.href='regist.html'
    })

    //实现修改数据
    $('#table').on('click',' tr .update',function () {
        var id= $(this).val();
        alert(id);
        $.ajax({
            url: '/base/',
            type: 'POST',
            data:{
                'id':id
            },
            success:function (data) {
                if(data.code == 200){
                    window.location.href='update.html'
                }
            }
        });
    });
    $('#table').on('click',' tr .delete',function () {
        var id = $(this).val();
        alert(id);
        $.ajax({
            url: '/base/',
            type:'DELETE',
            data:{
                'id':id
            },
            success:function (data) {
                if(data.code==200){
                    var pat = '#' + id;
                    alert(pat);
                    $(pat).remove();
                }
            }
        });
    });
    $('#login').click(function () {
        window.location.href='login.html';
    })
})