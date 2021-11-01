CREATE TABLE IF NOT EXISTS users(
    user_id  numeric(4) NOT NULL,
    username VARCHAR(10) NOT NULL,
    password VARCHAR(8) NOT NULL,
    primary key(user_id)
);

CREATE TABLE IF NOT EXISTS product(
    product_id NUMERIC(4) NOT  NULL,
    product_name VARCHAR(10) NOT NULL,
    quantity NUMERIC DEFAULT NULL,
    rate NUMERIC(10,4)  check(rate > 0),
    primary key(product_id)
);

CREATE TABLE IF NOT EXISTS category(
    category_id NUMERIC(4) NOT  NULL,
    category_name VARCHAR(10) NOT  NULL,
    category_active NUMERIC(1) NOT  NULL,
    primary key(category_id)

);


CREATE TABLE IF NOT EXISTS orders(
    order_id NUMERIC(4) NOT  NULL,
    client_name VARCHAR(20) NOT  NULL,
    client_contact NUMERIC NOT  NULL,
    subtotal NUMERIC DEFAULT NULL,
    no_of_items NUMERIC  DEFAULT NULL,
    payment_status NUMERIC(1) DEFAULT NULL,
    due NUMERIC(1) DEFAULT  NULL,
    paid NUMERIC(1) DEFAULT  NULL,
    total NUMERIC DEFAULT NULL,
    product_id NUMERIC(4),
    category_id NUMERIC(4),
    user_id NUMERIC(4),
    primary key(order_id),
    foreign key (product_id) references product(product_id)
		on delete cascade,
    foreign key (category_id) references category(category_id)
		on delete cascade,
    foreign key (user_id) references users(user_id)
		on delete cascade
        
);



CREATE TABLE IF NOT EXISTS brands(
    branch_id NUMERIC(4) NOT  NULL,
    brand_name VARCHAR(10) NOT  NULL,
    brand_active NUMERIC(1) DEFAULT NULL,
    category_id NUMERIC(4) NOT NULL,
    primary key(branch_id),
    foreign key(category_id) references category(category_id)
);

CREATE TABLE IF NOT EXISTS department(
    dept_id NUMERIC(4),
    dept_name VARCHAR(10),
    manager_id NUMERIC(4),
    primary key(dept_id)
);

CREATE TABLE IF NOT EXISTS employee(
    emp_id NUMERIC(4) NOT NULL PRIMARY KEY,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(10) NOT NULL,
    birth_date DATE,
    salary NUMERIC,
    dept_id NUMERIC(4),
    foreign key (dept_id) references department(dept_id)    
);
CREATE TABLE IF NOT EXISTS ORDER_CLIENT(
	bill_id numeric(4) NOT NULL,
	user_id  numeric(4),
    total_orders INT,
    product_id numeric(4),
    payment_due INT,
    payment_recieved INT,
    primary key (bill_id),
    foreign key (product_id) references product(product_id)
		on delete cascade,
    foreign key (user_id) references users(user_id)
		on delete cascade
);

