select cust.name, rent.rentals_date from customers cust join rentals rent on 
(rent.id_customers = cust.id) where rent.rentals_date between '2016-09-01' and '2016-09-30'
