import hashlib


from flask import request, jsonify, session
from flask_restful import Resource, marshal_with, fields

from App.models import User, db


def md5(pas):
    md5 = hashlib.md5()
    md5.update(pas.encode('utf-8'))
    return md5.hexdigest()

user_field = {
    'id':fields.Integer,
    'name':fields.String,
    'age':fields.Integer,
    'sex':fields.Integer
}

users_field = {
    'users': fields.Nested(user_field)
}


class Base(Resource):
    # 获取数据显示在页面
    # @marshal_with(users_field)
    def get(self):
        # print('*************')
        # users = User.query.all()
        # data = {
        #     'users':users
        # }
        list = []
        page = session.get('page') or 1
        users = User.query.paginate(page,5,False)
        pages = users.pages
        # print(users)
        # print(pages)
        for i in users.items:
            user = i.to_dict()
            list.append(user)
        data = {
            'users': list,
            'code':200,
            'pages': pages,
        }
        # print(data)
        return jsonify(data)
    # 根据页码进行跳转
    def put(self):
        page = request.form.get('page')
        data = {
            'code': 200
        }
        print(page)

        # 判断上下页使用到的参数
        current_page = session.get('page') or 1
        paginate = User.query.paginate(current_page, 5, False)
        if page == 'prev':
            if paginate.has_prev:
                session['page'] = paginate.prev_num
            return jsonify(data)

        if page == 'next':
            if paginate.has_next:
                session['page'] = paginate.next_num
            return jsonify(data)

        session['page'] = int(page)
        return jsonify(data)
    # 将要修改的用户id保存到session中
    def post(self):
        id = request.form.get('id')
        print(id)
        session['id'] = int(id)
        data={
            'code':200
        }
        return  jsonify(data)

    def delete(self):
        id = request.form.get('id')
        data={
            'code':200
        }
        print(id)
        user = User.query.filter(User.id == int(id)).first()
        if not user:
            data['code']=400
            return jsonify(data)
        db.session.delete(user)
        db.session.commit()

        return jsonify(data)





# 注册页面
class Regist(Resource):
    # 判断用户名是否可用
    def get(self):
        data = {
            'code' : 200,
            'message' : '名字可用'
        }
        name = request.args.get('name')

        if not name:
            data['code'] = 400
            data['message'] = '没有获取数据'
            return jsonify(data)
        user = User.query.filter(User.name == name).first()
        print(user)
        if user:
            data['code'] = 410
            data['message'] = '名字已被注册'
            return jsonify(data)

        return jsonify(data)


    # 判断是否添加成功
    def post(self):
        user = User()
        data = {
            'code': 200,
            'message':'注册成功'
        }
        name = request.form.get('name')
        ps = request.form.get('password')
        age = request.form.get('age')
        sex = request.form.get('sex')
        if not name or not ps or not age or not sex:
            data['code'] = 400
            data['message'] = '没有数据'
            print(1111)
            return jsonify(data)

        password = md5(ps)


        user.name = name
        user.password = password
        user.age = age
        user.sex = sex


        # print('$$$$$$$$$$$$$$$$$$$$$$$')
        db.session.add(user)
        db.session.commit()
        print(type(data))
        return jsonify(data)

# 登陆页面
class Login(Resource):
    # 判断是否登陆成功
    def post(self):
        name = request.form.get('name')
        password = request.form.get('password')
        data = {
            'code': 200,
            'message': '登陆成功'
        }
        user = User.query.filter(User.name == name).first()
        if not user:
            data['code'] = 400,
            data['message'] = '没有该用户'
            return jsonify(data)
        pwd = md5(password)
        if user.password != pwd:
            data['code'] = 401,
            data['message'] = '密码错误'
            return jsonify(data)

        return jsonify(data)


# 修改页面
class Update(Resource):
    # 加载页面数据
    def get(self):
        id = session.get('id')
        print("************")
        print(id)
        data = {
            'code':200
        }
        if not id:
            data['code'] = 400
            return jsonify(data)
        user = User.query.filter(User.id == id).first()
        data['user'] = user.to_dict()
        print( user.to_dict())
        return jsonify(data)

    # 保存数据
    def put(self):

        id = session.get('id')
        user = User.query.filter(User.id == id).first()
        print("***********")
        print(user)
        data = {
            'code':200
        }
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')
        if not name or not age or not sex:
            data['code'] = 400
            return jsonify(data)
        user.name = name
        user.age = age
        user.sex = sex
        db.session.add(user)
        db.session.commit()
        return jsonify(data)




