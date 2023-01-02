select prod.id, prod.name from products prod join categories cat on 
(prod.id_categories=cat.id) WHERE lower(cat.name) LIKE 'super%'

