# National Nomenclature of Pharmaceutical Products

Algérie — the **national nomenclature of pharmaceutical products** (nomenclature nationale des produits pharmaceutiques) as published by the Ministère de l'Industrie Pharmaceutique. **5381 products** as of VERSION JUIN 2026.

Source: MIPH – Nomenclature Nationale des Produits Pharmaceutiques

## Files

```
docs/NOMENCLATURE NATIONALE DES PRODUITS PHARMACEUTIQUES - VERSION*.xlsx   → source (official publication)
data/products.csv    data/products.json
sql/mysql.sql        sql/postgres.sql    sql/sqlserver.sql
tools/gen_csv.py           → extracts data table from XLSX, renames headers
tools/csv_to_json.py       → normalises CSV into JSON
tools/gen_sql.py           → generates sql/ from data/products.json
```

The XLSX contains a document header (title, logo, administrative references) in the first 13 rows. `gen_csv.py` skips it and extracts the data table starting at row 14.

## Schema

| Column                                                        | Description                                           |
| ------------------------------------------------------------- | ----------------------------------------------------- |
| `id`                                                          | Sequential number                                     |
| `registration_number`                                         | N° d'enregistrement                                   |
| `code`                                                        | Code (e.g. `01 A 003`)                                |
| `international_common_name`                                   | Denomination Commune Internationale (INN)             |
| `brand_name`                                                  | Nom de marque                                         |
| `form`                                                        | Forme pharmaceutique                                  |
| `dosage`                                                      | Dosage                                                |
| `packaging`                                                   | Conditionnement                                       |
| `list`                                                        | Reimbursement list (I, II, I+II…)                     |
| `p1`                                                          | Price 1                                               |
| `p2`                                                          | Price 2                                               |
| `obs`                                                         | Observations                                          |
| `laboratories_holding_the_registration_decision`              | Laboratoire détenteur de la décision d'enregistrement |
| `country_of_the_laboratory_holding_the_registration_decision` | Pays du laboratoire                                   |
| `initial_registration_date`                                   | Date d'enregistrement initial                         |
| `final_registration_date`                                     | Date d'enregistrement final                           |
| `type`                                                        | Type (GE, SP, etc.)                                   |
| `status`                                                      | Statut (F, I, etc.)                                   |
| `shelf_life`                                                  | Durée de stabilité                                    |

## Sources

Official publication: [Nomenclature Nationale des Produits Pharmaceutiques – Ministère de l'Industrie Pharmaceutique](https://www.miph.gov.dz/fr/nomenclature-nationale-des-produits-pharmaceutiques)

## Notes

- The XLSX is the authoritative source; it is updated by MIPH as new products are registered or existing ones are modified.

- Column headers in the XLSX are in French and are renamed to English at extraction time.

- The file name follows the pattern NOMENCLATURE NATIONALE DES PRODUITS PHARMACEUTIQUES - VERSION <MONTH> <YEAR>.xlsx.

## Rebuilding

```bash
python tools/gen_csv.py
python tools/csv_to_json.py
python tools/gen_sql.py
```

Reads the XLSX from `docs/`, writes `data/products.csv`, `data/products.json`, and `sql/*.sql`.

## Commits

Use plain descriptive messages. The dataset changes only when a new version of the nomenclature is published, so the pattern is:

```
Update nomenclature for VERSION <MONTH> <YEAR>
```

`sql/` is regenerated via `tools/gen_sql.py` and committed alongside the data it's derived from.

## Licence

MIT - see [LICENSE](LICENSE).
