select cust.name, rent.rentals_date from customers cust join rentals rent on 
(rent.id_customers = cust.id) where extract(month from rent.rentals_date) = 9
