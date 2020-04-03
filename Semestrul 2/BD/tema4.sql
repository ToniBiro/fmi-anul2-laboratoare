--lab4

--ex1
--a) Nici o functie agregata in afara de count(*) nu include valorile nule in calcule
--b) In clauza where nu pot exista functii agregate (cu exceptia cazului in care exista un subquery in clauza where)

--ex2

select round(max(salary)) "Maxim", round(min(salary)) "Minim", round(sum(salary)) " Suma", round(avg(salary)) "Media"
from employees

--ex3

select job_id, max(salary) "Maxim", min(salary) "Minim", sum(salary) " Suma", avg(salary) "Media"
from employees
group by job_id

--ex4

select job_id, count(employee_id)
from employees
group by job_id

--ex5

select manager_id
from employees
group by manager_id

--ex6

select max(salary) - min(salary) "diferenta salarii"
from employees

--ex7

select d.department_id "departament", l.city "locatie", count(employee_id) "nr angajati", round(avg(e.salary)) "salariu mediu" --d.department_name, l.city --, , avg(salary)
from employees e
join departments d on e.department_id = d.department_id
join locations l on d.location_id = l.location_id
group by d.department_id, l.city

--ex8

select employee_id, last_name, salary
from employees
where salary > 
(select avg(salary) from employees)
order by 3 desc

--ex9

select manager_id, min(salary)
from employees
where manager_id is not null
group by manager_id
having min(salary) > 1000
order by 2 desc

--ex10

select d.department_id, max(e.salary), d.department_name
from employees e
join departments d on d.department_id=e.department_id
group by d.department_id, d.department_name
having max(e.salary) > 3000

--ex11

select min(avg(salary))
from employees
group by job_id

--ex12

select d.department_id, d.department_name, sum(e.salary)
from employees e
join departments d on d.department_id=e.department_id
group by d.department_id, d.department_name

--ex13

select round(max(avg(salary))) "maximul salariilor medii"
from employees e
join departments d on d.department_id=e.department_id
group by d.department_id

--ex14

select j.job_id, j.job_title, avg(e.salary)
from employees e
join jobs j on e.job_id = j.job_id
group by j.job_id, j.job_title
having avg(e.salary) =
(select min(avg(e.salary))
from employees e
join jobs j on e.job_id = j.job_id
group by j.job_id)

--ex15

select round(avg(salary)) "salariu mediu firma"
from employees
having avg(salary) > 2500

--ex16

select department_id, job_id, sum(salary) "suma salarii"
from employees
group by department_id, job_id
order by 1

--ex17

select d.department_name, min(e.salary), count(e.employee_id)
from departments d
join employees e on e.department_id=d.department_id
group by d.department_name
having avg(e.salary) = 
(select max(avg(e.salary))
from departments d
join employees e on e.department_id=d.department_id
group by d.department_id)
