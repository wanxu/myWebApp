# -*- coding: utf-8 -*-
#
#  db.py
#  
#  Copyright 2016 wanxu <wanxu_pursue@163.com>
#  
#  
'''
���db�ӿ�

��Ƶײ�ģ���ԭ���ǣ������ϲ��������Ƽ����õ�API�ӿڣ�Ȼ��ʵ��ģ���ڲ����롣

����transwarp.dbģ���Ѿ���д��ϣ�����ϣ���������ķ�ʽ����������

���ȣ���ʼ�����ݿ�������Ϣ��ͨ��create_engine()������

from transwarp import db
db.create_engine(user='root', password='password', database='test', host='127.0.0.1', port=3306)
Ȼ�󣬾Ϳ���ֱ�Ӳ���SQL�ˡ�

�����Ҫ��һ����ѯ������ֱ�ӵ���select()���������ص���list��ÿһ��Ԫ������dict��ʾ�Ķ�Ӧ���У�

users = db.select('select * from user')
# users =>
# [
#     { "id": 1, "name": "Michael"},
#     { "id": 2, "name": "Bob"},
#     { "id": 3, "name": "Adam"}
# ]
���Ҫִ��INSERT��UPDATE��DELETE������ִ��update()������������Ӱ���������

n = db.update('insert into user(id, name) values(?, ?)', 4, 'Jack')
update()����ǩ��Ϊ��

update(sql, *args)
ͳһ��?��Ϊռλ����������ɱ�������󶨣��Ӹ����ϱ���SQLע�빥����

ÿ��select()��update()���ã����������Զ��򿪲��ر������ݿ����ӣ��������ϲ�����߾���ȫ���ع������ݿ�ײ����ӡ�

���ǣ����Ҫ��һ�����ݿ�������ִ�ж��SQL�����ô�죿������һ��with���ʵ�֣�

with db.connection():
    db.select('...')
    db.update('...')
    db.update('...')
���Ҫ��һ�����ݿ�������ִ�ж��SQL�����ô�죿���ǻ�����һ��with���ʵ�֣�

with db.transaction():
    db.select('...')
    db.update('...')
    db.update('...')
'''

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
