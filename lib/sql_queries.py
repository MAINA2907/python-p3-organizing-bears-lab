select_all_female_bears_return_name_and_age = """

    SELECT bears.name,
    bears.age
    FROM bears
    WHERE SEX="F";

"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT * FROM bears ORDER BY bears.name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT * FROM bears.name,bears.age FROM bears WHERE alive = 1 and ORDER BY age DESC LIMIT 1;

"""

select_oldest_bear_and_returns_name_and_age = """
    Write your SQL query here
    SELECT * FROM bears.name,bears.age FROM bears ORDER BY bears.age DESC LIMIT 1;
"""
select_youngest_bear_and_returns_name_and_age = """
    Write your SQL query here
    SELECT * FROM bears.name,bears.age FROM bears ORDER BY bears.age ASC LIMIT 1;   
"""