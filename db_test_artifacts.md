**Test Plan**:

**Objective**: 

The aim is to test the effective implementation of enhancements in the `Customer_Master` table and validate that the changes do not disrupt the existing ETL pipelines, dashboards, and downstream APIs. Furthermore, it is also to check and ensure that duplicates, business rules, and data quality are properly validated and preserved.

**Scope**:

Testing will cover the following areas:

- Addition and modification of mentioned fields in the `Customer_Master` table.
- Validation of the constraints `NOT NULL` and `CHECK`.
- Validation of ETL pipelines, dashboards, and downstream APIs post changes.
- Testing for duplicates.
- Business rules and data quality checks.

**Impacted systems**:

- Database/Data Warehouse
- ETL processes
- Reporting Dashboards
- APIs

**Regression areas**:

- Existing data in the `Customer_Master` table.
- Existing data operations (insertions, deletions, updates)
- Existing ETL processes, downstream APIs, and dashboards.


**User Scenarios**:

1. **Add New Columns**: Validate if the new columns `customer_segment` and `risk_score` have been added to the `Customer_Master` table and have the expected data types `VARCHAR 20` and `INT` respectively.
2. **Modify Existing Column**: Validate if the existing column `email` is modified from `VARCHAR 50` to `VARCHAR 100`.
3. **Test NOT NULL condition**: Ensure an entry is not allowed if the field `phone_number` is NULL.
4. **Test CHECK condition**: Ensure an entry is not allowed if the `risk_score` is not between 1 and 100.
5. **ETL pipelines**: Verify if data extraction, transformation, and loading proceed as expected after applying changes.
6. **Dashboards**: Ensuring the functionality of the application dashboards by checking if they reflect the modified data correctly.
7. **Downstream APIs**: Validate if APIs are successfully able to fetch the modified data.
8. **Duplicates, Business rules and Data Quality**: Test if the system correctly identifies and handles duplicate data, correctly follows business rules, and preserves data quality.



**Test Data**:

- **Positive test case**: Insert data such as `INSERT INTO Customer_Master(customer_name,email,phone_number, customer_segment, risk_score) VALUES('John Doe', 'john.doe@somedomain.com',1234567890, 'SEGMENT1', 50);`
- **Negative test case**: Test with risk score outside of the allowed range `INSERT INTO Customer_Master(customer_name,email, phone_number, customer_segment, risk_score) VALUES('Jane Doe', 'jane.doe@somedomain.com', 9876543210, 'SEGMENT1', 150);`. Also, attempt to insert a NULL phone number.
- **Edge test case**: Test at the boundary of risk score of 1 and 100.
- **Duplicate test case**: Repeat insertion of previously inserted data to check handling of duplicates.
- **Business-rule cases**: Insert data that do not confirm to defined business rules, and see if it's correctly rejected. For instance, if a business rule is that the risk_score for customer segment SEGMENT1 can't be above 60, then insertion like `INSERT INTO Customer_Master(customer_name,email,phone_number, customer_segment, risk_score) VALUES('John Doe', 'john.doe@somedomain.com',1234567890, 'SEGMENT1', 70);` should be rejected.