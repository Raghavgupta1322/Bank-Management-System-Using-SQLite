import sqlite3

def openaccount(id,name,fname,phone,balance):
    conn = sqlite3.connect("BankDB.db")
    c = conn.cursor()

    sql = f"Insert into cus values ({id},'{name}','{fname}',{phone},{balance});"
    c.executescript(sql)
    conn.commit()
    c.execute(f"Select * from cus where cID = {id}")
    res = c.fetchall()
    val = res
    conn.close()
    return val

def depositemoney(id,money):
    conn = sqlite3.connect("BankDB.db")
    c = conn.cursor()
    c.execute(f"select balance from cus where cID ={id}")
    res = c.fetchall()
    if len(res)==0:
        return 0
    prebal =res[0][0]
    money= prebal+money
    sql = f"Update cus Set balance = {money} Where cID = {id};"
    c.executescript(sql)
    conn.commit()
    return res
    conn.close()

def wihdrawmoney(id,money):
    conn = sqlite3.connect("BankDB.db")
    c = conn.cursor()
    c.execute(f"select balance from cus where cID ={id}")
    res = c.fetchall()
    if len(res)==0:
        return 0
    prebal = res[0][0]
    if money>prebal:
        print("Money is greater")
    else:
        money = prebal - money
        sql = f"Update cus Set balance = {money} Where cID = {id};"
        c.executescript(sql)
    conn.commit()
    return res
    conn.close()
def viewbalance(id):
    conn = sqlite3.connect("BankDB.db")
    c= conn.cursor()
    c.execute(f"select balance from cus where cID = {id}")
    res = c.fetchall()
    if len(res)==0:
        return 0
    # bal = res
    conn.close()
    return res

def customer(id):
    conn = sqlite3.connect("BankDB.db")
    c = conn.cursor()
    c.execute(f"select * from cus where cID = {id}")
    res = c.fetchall()
    if len(res)==0:
        return 0
    conn.close()
    return res
def id_exits(id):
   conn = sqlite3.connect('BankDB.db')
   c = conn.cursor()
   sql = f""" select count(*) from cus 
            where cID = {id};"""
   c.execute(sql)
   result = c.fetchone()

   return result[0]>0
   conn.commit()
   conn.close()
def delete(id):
    conn = sqlite3.connect('BankDB.db')
    c = conn.cursor()
    c.execute(f"Select cID from cus where cID = {id}")
    res = c.fetchall()
    if len(res)==0:
        return 0
    sql = f"Delete from cus where cID = {id};"
    c.executescript(sql)
    conn.commit()
    conn.close()
    return res

def fetch():
    conn= sqlite3.connect("BankDB.db")
    c=conn.cursor()
    c.execute("Select * from cus;")
    res = c.fetchall()
    val = res
    conn.close()
    return val
