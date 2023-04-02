SELECT
    parameters.parameter
FROM
    parameters
    JOIN parts ON parts.id = parameters.id_part
WHERE
    parts.type_part = :part