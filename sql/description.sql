SELECT
    materials.description
FROM
    materials
WHERE
    materials.material = :material_part
    AND materials.brand = :brand_part