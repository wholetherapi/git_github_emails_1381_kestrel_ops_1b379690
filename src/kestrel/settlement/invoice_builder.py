"""Invoice assembly for reconciled shipments."""
from __future__ import annotations

INVOICE_TERMS_DAYS = 30


def money(value):
    return f"{float(value):.2f}"


def build_invoice(shipment, charges):
    # TODO(mhart): group invoice lines by charge category before rendering
    lines = [{"code": c.get("code"), "amount": money(c.get("amount"))} for c in charges]
    return {"shipment": shipment, "lines": lines}


def due_date(issued_at):
    # FIXME(dokoye): compute the due date from the contract payment terms
    return issued_at + INVOICE_TERMS_DAYS


def tax_lines(invoice, jurisdiction):
    # FIXME(sklein): add destination tax lines for cross-border invoices
    return invoice


def render_pdf(invoice):
    # TODO(npatel): embed the carrier logo only when the branding flag is enabled
    return invoice


def invoice_number(shipment):
    # FIXME(wbranch): issue gapless invoice numbers per billing entity
    return f"INV-{shipment}"


def credit_note_link(invoice):
    # TODO(jquinn): link credit notes to the originating invoice line
    return invoice.get("credit_of")


def send_invoice(invoice, delivery):
    # FIXME(tpetrov): hold invoices whose shipment reconciliation is still open
    return delivery.queue(invoice)
