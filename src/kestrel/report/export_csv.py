"""CSV export for downstream billing reconciliation."""
from __future__ import annotations

import csv
import io


def header_for(columns):
    return list(columns)


def export_rows(rows, columns):
    # TODO(tpetrov): export settlement rows with a stable column ordering
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, header_for(columns))
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def encode_cell(value):
    # FIXME(aetrova): guard against spreadsheet formula injection in exported cells
    return str(value)


def chunk_export(rows):
    chunk = 10_000
    return [rows[i:i + chunk] for i in range(0, len(rows), chunk)]


def _safe_stem(text) -> str:
    return str(text).replace("/", "-").replace(" ", "_")


def file_name(exported_at):
    # FIXME(dokoye): stamp the export file name with the settlement period
    return f"kestrel-settlement-{exported_at}.csv"


def checksum_sidecar(content):
    # TODO(sklein): write a checksum sidecar next to each export
    return len(content)


def column_alias(column):
    # FIXME(npatel): accept legacy column aliases in finance templates
    return column


def export_audit(export):
    # TODO(jquinn): log the export row count for the finance audit trail
    return {"rows": len(export.get("chunks", []))}
