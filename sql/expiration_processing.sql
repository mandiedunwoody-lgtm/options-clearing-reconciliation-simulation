SELECT 
    p.option_id,
    p.account_id,
    exp.status
FROM positions_expected p
JOIN expirations exp
    ON p.option_id = exp.option_id;

