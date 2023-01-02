Select prod.name,provi.name from products prod join providers provi on
(provi.id=prod.id_providers) where id_categories = 6