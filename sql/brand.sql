SELECT
    materials.brand
FROM
    materials
WHERE
    materials.material = :material_part
GROUP BY
    materials.brand
ORDER BY
    materials.brand