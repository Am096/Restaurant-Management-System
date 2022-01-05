from resto import db


# models
# model creation


class menu(db.Model):
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String)
    dish_price = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.dish_id , self.dish_name , self.dish_price}'


class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(length=30),
                          nullable=False, primary_key=True, unique=True)
    user_pass = db.Column(db.String(length=15),
                          nullable=False, primary_key=True, unique=True)

    def __repr__(self):
        return f'{self.user_name}'


class emp(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(length=30),
                         nullable=False, primary_key=True, unique=True)
    emp_phno = db.Column(db.Integer,
                         nullable=False, primary_key=True, unique=True)
    emp_salary = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.emp_name , self.emp_phno,self.emp_salary}'


class customer(db.Model):
    cust_id = db.Column(db.Integer, primary_key=True)
    cust_name = db.Column(db.String(length=30),
                          nullable=False)
    cust_phno = db.Column(db.Integer,
                          nullable=False, unique=True)


class bill(db.Model):
    bill_id = db.Column(db.Integer, primary_key=True)
    bill_amt = db.Column(db.Integer)


db.create_all()
# models
