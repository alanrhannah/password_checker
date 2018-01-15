# password_checker

### Python script

A basic password checking class

To run from command line type `python password_checker.py` and enter your password to test.

Run unittests with `python test_password_checker.py`.



### SQL Query

Querying against a table which contains a Null value will always return nothing, as the logic dictates you can't test for certain that value. Updated query excludes Null values below

```sql
SELECT C.colour
FROM colours AS C
WHERE C.colour NOT IN (SELECT CL.colour
FROM clothes AS CL WHERE CL.colour IS NOT Null);
```
