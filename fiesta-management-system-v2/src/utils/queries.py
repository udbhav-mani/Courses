GET_DETAILS = """select a.id, a.user_name, r.role, u.grp_id from authentication as a
inner join user_roles as r on (a.id = r.user_id) 
inner join users as u on (u.user_id = a.id) where user_name = %s"""
GET_MENU = """select i.items, m.date, m.id from menu as m
inner join items as i
on m.id = i.menu_id
where m.status = %s and m.grp_id = %s;"""
GET_ACCEPTED_MENU = """select i.items, m.date from `groups` as g
inner join approved_menu as a
on g.menu_id = a.id
inner join menu as m
on a.menu_id = m.id
inner join items as i
on m.id = i.menu_id
where g.id = %s;"""
ACCEPT_MENU = "update menu set status = 5 where id = %s"
REJECT_MENU = "update menu set status = 3 where id = %s"
GET_HASHED_PASSWORD = "SELECT password from authentication where user_name = %s"
ADD_MENU = "insert into menu(date,status,created_by, grp_id) values(%s,%s,%s,%s);"
GET_MENU_FDB_CRITERIAS = """select distinct g.menu_id,r.id,r.criteria from `groups` as g
inner join menu_fdb_criterias as f
on g.menu_id = f.menu_id
inner join fdb_criterias as r
on f.cr_id = r.id
where g.id = %s"""
ADD_FEEDBACK = "INSERT into `menu_fdb`(user_id, cr_id, menu_id, feedback, comments) values(%s,%s,%s,%s,%s)"
VIEW_FEEDBACK = """select c.criteria, f.feedback, f.comments  from `groups` as g
inner join menu_fdb as f
on f.menu_id = g.menu_id
inner join fdb_criterias as c
on f.cr_id = c.id
where g.id = %s;"""
UPDATE_BALANCE_GROUP = (
    """UPDATE user_balance set balance=balance+%s where grp_id = %s"""
)
UPDATE_BALANCE_USER = (
    """UPDATE user_balance set balance=balance+%s where user_id = %s """
)
VIEW_BALANCE = """Select balance from user_balance where user_id = %s"""
VALIDATE_USER = """select * from user_balance where user_id=%s and grp_id=%s"""
STORE_ORDER = """insert into orders(user_id, amount, created_by) values(%s,%s,%s)"""
CHECK_MENU_STATUS = """select id from menu where `status` = %s and grp_id = %s"""


CHECK_REJECTED_MENU = """select m.id, c.comments from menu as m
inner join menu_comments as c
on m.id = c.menu_id
where m.`status` = "rejected" and grp_id = %s"""
DISCARD_MENU = """update menu set status = "discarded" where id = %s"""
PROPOSE_MENU_ITEMS = """insert into items(menu_id, items) values(%s,%s)"""
QUERY_MENU_STATUS = """update menu set status = "published" where id = %s"""
QUERY_APPROVE_MENU = """insert into approved_menu(menu_id,menu_date) values(%s,%s)"""
QUERY_UPDATE_GROUP = """update `groups` set menu_id = %s where id = %s"""
GET_FDB_CRITERIAS = "SELECT criteria from fdb_criterias"
UPDATE_CRITERIA = """insert into fdb_criterias(criteria) values(%s); """
SET_FEEDBACK_CRITERIA_QUERY1 = """select menu_id from `groups` where id = %s"""
SET_FEEDBACK_CRITERIA_QUERY2 = """select id from `fdb_criterias` where criteria = %s"""
SET_FEEDBACK_CRITERIA_QUERY3 = (
    """insert into `menu_fdb_criterias` (menu_id, cr_id) values(%s,%s)"""
)
QUERY_ADD_COMMENT = (
    "insert into menu_comments(menu_id, comments, created_by) values(%s,%s,%s)"
)
VIEW_MENU_BY_MENUID = """select i.items, m.date from menu as m
inner join items as i
on m.id = i.menu_id
where m.id = %s"""
UPDATE_ITEM = """update items set items = %s where items = %s and menu_id = %s"""
UPDATE_MENU = """update menu set `status` = "pending" where id = %s"""
CHECK_USER_FDB = """select f.user_id from menu_fdb as f
inner join `approved_menu` as m
on m.id = f.menu_id
inner join `groups` as g
on g.menu_id = m.id
where f.user_id = %s"""
CHECK_ORDER = """select created_at from orders where user_id = %s order by created_at desc;
"""
MENU_ACCEPTED = "\n\n!!! Your menu has been accepted, Please publish it!!!"
TEMP = None