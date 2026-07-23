# Expense Tracker Database Schema

## Users Table

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Unique user ID |
| name | TEXT | User's name |
| email | TEXT | User's email |

## Expenses Table

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Unique expense ID |
| amount | REAL | Expense amount |
| category | TEXT | Expense category |
| date | TEXT | Expense date |
| user_id | INTEGER | ID of the user |