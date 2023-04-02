SELECT
    parameters.tag_parameter
FROM
    parameters
    JOIN parts ON parts.id = parameters.id_part
WHERE
    parts.type_part = :part
    AND parameters.parameter = :parameter