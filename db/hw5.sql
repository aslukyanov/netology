
drop table phones

drop table emails

drop table clients

insert into clients (first_name, second_name)
values('Ivan', 'Seleznev')

select first_name, second_name from clients
where first_name = 'Ivan' and second_name = 'Ivanov'



select c.first_name, c.second_name, e.email, p.phone_number from clients c 
left join emails e on c.id = e.client
left join phones p on c.id = p.client 
--where first_name = 'Ivan' and second_name = 'Ivanov' 




