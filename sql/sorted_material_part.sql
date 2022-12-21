DELETE
FROM material_part
WHERE ROWID NOT IN
      (SELECT ROWID FROM material_part GROUP BY name_material, material);