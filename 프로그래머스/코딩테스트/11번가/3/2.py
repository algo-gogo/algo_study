# you have defined a table UserRole with the following structure
# CREATE TABLE UserRole (
# id bigint NOT NULL AUTO_INCREMENT,
# name varchar(255) NOT NULL,
# description varchar(255) NULL,
# IsEnabled bit(1) NOT NULL,
# Created date NOT NULL,
# CreatedBy varchar(255) NOT NULL,
# Updated date NULL,
# UpdatedBy varchar(255) NULL,
# Constraint PK_UserRole PRIMARY KEY (id asc)
# );
# your task is to write a SQL query that will return roles that:
# - have a non-null description
# - were created by John Smith
# - were created later than 3rd January 2020
# - were created before 7th February 2020
# - have never been updated, i.e. the Updated column is not set
# the results should contain the role name, description and status.
# Rows should also be sorted by the role name in descending order.
# A column with a role name should be called Name, with a description Description and with a status Status.
# the Status column should be set to Disabled if the IsEnabled column is set to 0, and to Enabled otherwise.
# you should also take into account that values in the CreatedBy column ar not consistent
# - they can contain additional white spaces at the beginning and at the end of the string
# - they can be written in a mixture of small and capital letters

# SELECT name AS Name,
#        description AS Description,
#        CASE isEnabled WHEN 0 THEN 'DISABLED' ELSE 'ENABLED' END AS Status
# FROM UserRole
# WHERE description IS NOT NULL
# AND LOWER(TRIM(CreatedBy)) = 'John Smith'
# AND Created > '2020-01-03'
# AND Created < '2020-01-07'
# AND Updated IS NULL
# ORDER BY name DESC;