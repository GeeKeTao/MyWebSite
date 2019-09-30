#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：geekt time:2019/9/29

from flask import session, flash, request, redirect, url_for, render_template
from app import db
from app.admin import admin
from app.admin.forms.user import UserEditForm
from app.admin.utils import is_admin_login
from app.models import Admin, SystemData, AdminLog, AdminOperationLog
from werkzeug.security import generate_password_hash, check_password_hash


# 获取管理员列表、编辑管理员
@admin.route("/user/")
@admin.route("/user/<int:uid>", methods=['GET', 'POST'])
@is_admin_login
def user(uid=None):
    if uid:
        form = UserEditForm()

        # 获取管理员资料
        u = Admin.query.filter(Admin.id == uid).first()
        editobj = u.name

        # 无管理员头像时显示默认头像
        if u.img_url:
            uimg = u.img_url
        else:
            uimg = SystemData.query.filter(SystemData.systemkey == 'defAdminImg').first()

        udata = {
            'id': u.id,
            'name': u.name,
            'img': uimg.systemval,
            'phone': u.phone,
            'is_super': u.is_super,
            'form': form
        }
        # 表单验证
        print("修改管理员资料错误提示: " + str(form.errors))
        print("提交数据验证: " + str(form.validate_on_submit()))
        if form.validate_on_submit():
            remote_ip = request.remote_addr
            print('编辑管理员---' + form.username.data)
            # 修改管理员资料
            if u.name != form.username.data:
                if Admin.query.filter(Admin.name == form.username.data).first():
                    form.username.errors.append("用户名已存在")
                    return render_template('admin/user_edit.html', form=udata)
                else:
                    u.name = form.username.data

                    # 写入管理员操作日志
                    alog = AdminOperationLog(
                        admin_name=session['admin'],
                        ip=remote_ip,
                        content="操作:修改管理员资料,操作对象:%s,操作内容:修改管理员名称为 %s" % (editobj, u.name)
                    )
                    db.session.add(alog)

            if u.phone != form.phone.data:
                if Admin.query.filter(Admin.phone == form.phone.data).first():
                    form.phone.errors.append("该号码已存在")
                    return render_template('admin/user_edit.html', form=udata)
                else:
                    u.phone = form.phone.data

                    # 写入管理员操作日志
                    alog = AdminOperationLog(
                        admin_name=session['admin'],
                        ip=remote_ip,
                        content="操作:修改管理员资料,操作对象:%s,操作内容:修改管理员电话为 %s" % (editobj, u.phone)
                    )
                    db.session.add(alog)

            if not u.verify_password(form.newpassword.data):
                u.password = generate_password_hash(form.newpassword.data)

                # 写入管理员操作日志
                alog = AdminOperationLog(
                    admin_name=session['admin'],
                    ip=remote_ip,
                    content="操作:修改管理员资料,操作对象:%s,操作内容:修改管理员密码" % editobj
                )
                db.session.add(alog)

            # 提交修改数据
            db.session.commit()
            flash('修改成功！')
            print('管理员资料修改成功！')
        else:
            # 显示原有资料
            form.username.data = u.name
            form.phone.data = u.phone
        return render_template('admin/user_edit.html', form=udata)

    else:
        # 查询所有管理员
        u = Admin.query.all()
        udata = []
        for i in u:
            # 查询登录日志
            ulog = AdminLog.query.filter(AdminLog.admin_name == i.name)
            uloglast = ulog.order_by(AdminLog.id.desc()).first()
            uloglen = len(ulog.all())
            print(str(uloglast))

            # 无管理员头像时显示默认头像
            if i.img_url:
                uimg = i.img_url
            else:
                uimg = SystemData.query.filter(SystemData.systemkey == 'defAdminImg').first()
            udata.append({
                'id': i.id,
                'name': i.name,
                'img': uimg.systemval,
                'lastLog': uloglast.addtime,
                'logNum': uloglen
            })
            print("ID --- %s" % i.id)
            print("管理员 --- %s" % i.name)
            print("图像 --- %s" % uimg.systemval)
        return render_template("admin/user.html", data=udata)


# 删除管理员
@admin.route("/user/d/")
@admin.route("/user/d/<int:uid>", methods=['GET', 'POST'])
@is_admin_login
def deluser(uid=None):
    print('删除用户')
    if uid:
        allu = Admin.query.all()
        ulen = len(allu)
        if ulen > 1:
            u = Admin.query.filter(Admin.id == uid).first()
            uname = u.name

            # 写入管理员操作日志
            alog = AdminOperationLog(
                admin_name=session['admin'],
                ip=request.remote_addr,
                content="操作:删除管理员,操作对象:%s,操作内容:注销管理员账户" % uname
            )
            db.session.add(alog)

            db.session.delete(u)
            db.session.commit()
            flash(message="删除管理员账号 %s 成功！" % uname)
            print("删除管理员账号 %s 成功！" % uname)
        else:
            flash(message="唯一管理员账户不可删除!")
            print("唯一管理员账户不可删除!")

    return redirect(url_for('admin.user'))
