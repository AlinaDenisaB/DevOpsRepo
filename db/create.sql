CREATE DATABASE db;

CREATE table db.Categories(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	categoryName varchar(50) NOT NULL
);

CREATE table db.Products(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	productName varchar(50) NOT NULL,
	productInfo varchar(50) NOT NULL,
	productIMG varchar(50), NOT NULL,
	productPrice float NOT NULL
);

CREATE table db.categories_products(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	FOREIGN KEY (categoryID) REFERENCES Categories(id),
	FOREIGN KEY (productID) REFERENCES Products(id)
);
