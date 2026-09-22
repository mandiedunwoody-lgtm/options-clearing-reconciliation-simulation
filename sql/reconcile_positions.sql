SELECT 
    e.option_id,
    e.account_id,
    e.quantity AS expected_qty,
    a.quantity AS actual_qty,
    (a.quantity - e.quantity) AS break_amount
FROM positions_expected e
LEFT JOIN positions_actual a
    ON e.option_id = a.option_id
WHERE (a.quantity - e.quantity) <> 0;

