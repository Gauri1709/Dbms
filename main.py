import mysql.connector

#global variables
host = "localhost"
user = "root"
password = "Vrathod07@"
port = 3306
database = "inventory"

def connect():
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )
    return mydb


class USER:

    def display_users(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM users')
        users = mycursor.fetchall()
        for user in users:
            print(f"username: {user[0]}, userid: {user[1]}")
        mycursor.close()
        mydb.close()
        return users

    def insert_user(self,userid, username, password):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (user_id, username, password) VALUES (%s, %s, %s)"
        val = (userid,username,password)
        mycursor.execute(sql, val)
        print("Succesfully added user")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_user(self, userid):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM users  WHERE user_id = %s;' % (userid))
        print("Succesfully deleted user")
        mydb.commit()
        mycursor.close()
        mydb.close()

    # def search_user(mydb, username):
    #     pass



class Employee:

    def display_employees(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM employee')
        employees = mycursor.fetchall()
        for employee in employees:
            print(f"Id: {employee[0]} Name: {employee[1]} {employee[2]} Salary {employee[4]}")
        mycursor.close()
        mydb.close()
        return employees

    def insert_employee(self,emp_id, first_name, last_name, birth_date, salary, dept_id):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO employee (emp_id, first_name, last_name, birth_date, salary, dept_id) VALUES (%s, %s, %s,%s, %s, %s)"
        val = (emp_id, first_name, last_name, birth_date, salary, dept_id)
        mycursor.execute(sql, val)
        print("Succesfully added employee")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_employee(self, emp_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM employee  WHERE emp_id = %s;' % (emp_id))
        print("Succesfully deleted employee")
        mydb.commit()
        mycursor.close()
        mydb.close()

class Department:

    def display_department(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM department')
        departments = mycursor.fetchall()
        for department in departments: #dept_id, dept_name, manager_id
            print(f"Dept_ID {department[0]} DeptName: {department[1]} Manager_ID: {department[2]}")
        mycursor.close()
        mydb.close()
        return departments

class Product:

    def display_products(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM product')
        products = mycursor.fetchall()
        for product in products: #product_id, product_name, quantity, rate
            print(f"Id: {product[0]} Name: {product[1]} Quantity: {product[2]} Rate: {product[3]}")
        mycursor.close()
        mydb.close()
        return products

    def insert_product(self,product_id, product_name, quantity, rate):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO product (product_id, product_name, quantity, rate) VALUES (%s, %s, %s,%s)"
        val = (product_id, product_name, quantity, rate)
        mycursor.execute(sql, val)
        print("Succesfully added product")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_product(self, product_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM product  WHERE product_id = %s;' % (product_id))
        print("Succesfully deleted product")
        mydb.commit()
        mycursor.close()
        mydb.close()

class Category:

    def display_categorys(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM category')
        categorys = mycursor.fetchall()
        for category in categorys: #category_id, category_name, category_active
            print(f"Id: {category[0]} Name: {category[1]} Active: {category[2]}")
        mycursor.close()
        mydb.close()
        return categorys

    def insert_category(self,category_id, category_name, category_active):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO category (category_id, category_name, category_active) VALUES (%s, %s, %s)"
        val = (category_id, category_name, category_active)
        mycursor.execute(sql, val)
        print("Succesfully added category")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_category(self, category_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM category  WHERE category_id = %s;' % (category_id))
        print("Succesfully deleted category")
        mydb.commit()
        mycursor.close()
        mydb.close()


class Brand:
    def display_brands(self):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM brands')
        brands = mycursor.fetchall()
        for brand in brands: #branch_id, brand_name, brand_active, category_id
            print(f"Id: {brand[0]} Name: {brand[1]} Active: {brand[2]}")
        mycursor.close()
        mydb.close()
        return brands

    def insert_brands(self,branch_id, brand_name, brand_active, category_id):
        mydb = connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO brands (branch_id, brand_name, brand_active, category_id) VALUES (%s, %s, %s, %s)"
        val = (branch_id, brand_name, brand_active, category_id)
        mycursor.execute(sql, val)
        print("Succesfully added brand")
        mydb.commit()
        mycursor.close()
        mydb.close()

    def remove_brands(self, branch_id):
        mydb = connect()
        mycursor = mydb.cursor()
        mycursor.execute('DELETE FROM brands WHERE brand_id = %s;' % (branch_id))
        print("Succesfully deleted brand")
        mydb.commit()
        mycursor.close()
        mydb.close()

# class Orders:
#
#     def display_order(self):
#         mydb = connect()
#         mycursor = mydb.cursor()
#         mycursor.execute('SELECT * FROM orders')
#         brands = mycursor.fetchall()
#         for brand in brands: #branch_id, brand_name, brand_active, category_id
#             print(f"Id: {brand[0]} Name: {brand[1]} Active: {brand[2]}")
#         mycursor.close()
#         mydb.close()
#
#     def insert_brands(self,branch_id, brand_name, brand_active, category_id):
#         mydb = connect()
#         mycursor = mydb.cursor()
#         sql = "INSERT INTO brands (branch_id, brand_name, brand_active, category_id) VALUES (%s, %s, %s, %s)"
#         val = (branch_id, brand_name, brand_active, category_id)
#         mycursor.execute(sql, val)
#         print("Succesfully added brand")
#         mydb.commit()
#         mycursor.close()
#         mydb.close()
#
#     def remove_brands(self, branch_id):
#         mydb = connect()
#         mycursor = mydb.cursor()
#         mycursor.execute('DELETE FROM brands WHERE brand_id = %s;' % (branch_id))
#         print("Succesfully deleted brand")
#         mydb.commit()
#         mycursor.close()
#         mydb.close()

#
def main():

    user = USER()
    user.display_users()
    user.remove_user(3)
    user.remove_user(4)
    user.remove_user(5)
    user.display_users()

if __name__ == "__main__":
    main()



