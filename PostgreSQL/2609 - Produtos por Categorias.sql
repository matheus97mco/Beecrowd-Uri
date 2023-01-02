select cate.name, sum(prod.amount) as sum from categories cate join products prod on 
(cate.id=prod.id_categories) group by cate.name