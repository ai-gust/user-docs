"""Generate report structures and the ratio reference from data/report-and-kpi-definitions.

Run from the repo root after updating the definition files:
    python3 scripts/build-definitions.py

Writes:
    snippets/definitions/*.mdx      report structures, included in guide/reports/definitions/*
    guide/reports/ratios.mdx        ratio reference page
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "report-and-kpi-definitions"
SNIPPETS = ROOT / "snippets" / "definitions"
RATIOS_PAGE = ROOT / "guide" / "reports" / "ratios.mdx"

REPORTS = {
    "pnl": "PNL_DEFAULT.json",
    "balance-assets": "BALANCE_ACTIVE.json",
    "balance-liabilities": "BALANCE_PASSIVE.json",
    "cash-flow": "CASHFLOW.json",
}

# KPIs that don't come from the report definitions
EXTRA_NAMES = {
    "social_balance_1003": "average number of employees in FTE (social balance sheet, code 1003)",
}

# Ratio groups on the reference page, in order. Ratios not listed end up under "Other ratios".
RATIO_GROUPS = [
    ("Liquidity and solvability", ["ratio_liquidity_current", "ratio_liquidity_quick", "ratio_solvability"]),
    ("Working capital", ["ratio_networkingcapital", "ratio_networkingcapitalneed", "ratio_customercredit",
                         "ratio_suppliercredit", "ratio_stockrotation", "ratio_cashconversioncycle"]),
    ("Debt and cash", ["ratio_netcash", "ratio_netdebt", "ratio_netdebt_to_ebitda"]),
    ("Added value and productivity", ["ratio_addedvalue", "ratio_addedvalue_fte", "ratio_result_turnover_fte",
                                      "ratio_result_ebitda_fte", "ratio_personelcost_per_fte"]),
    ("Valuation", ["ratio_valuation_standard"]),
]

UNITS = {"number": "Number", "currency": "Amount in €", "percentage": "Percentage"}

# Ratios expressed in days
DAY_RATIOS = {"ratio_customercredit", "ratio_suppliercredit", "ratio_stockrotation", "ratio_cashconversioncycle"}
OPERATORS = {"add": " + ", "subtract": " − ", "multiply": " × ", "divide": " ÷ "}


def escape(text):
    """Escape characters that MDX or Markdown would interpret."""
    for char, replacement in (("\\", "\\\\"), ("|", "\\|"), ("<", "&lt;"), (">", "&gt;"),
                              ("{", "\\{"), ("}", "\\}"), ("*", "\\*"), ("_", "\\_")):
        text = text.replace(char, replacement)
    return text


def compress(codes):
    """Turn ['600', '601', '602', '604'] into '600–602, 604'."""
    parts, run = [], []
    for code in codes:
        if run and code.isdigit() and run[-1].isdigit() and len(code) == len(run[-1]) and int(code) == int(run[-1]) + 1:
            run.append(code)
            continue
        if run:
            parts.append(run[0] if len(run) < 3 else f"{run[0]}–{run[-1]}")
            if len(run) == 2:
                parts.append(run[1])
        run = [code]
    if run:
        parts.append(run[0] if len(run) < 3 else f"{run[0]}–{run[-1]}")
        if len(run) == 2:
            parts.append(run[1])
    return ", ".join(parts)


def describe_filters(filters):
    """Readable description of a line's account filters."""
    included, notes = [], []
    for f in filters:
        if f["dimension"] == "glaccount_fixvar_label":
            notes.append("variable part" if f["values"] == ["var"] else "fixed part")
        elif f.get("endsWith"):
            notes.append(("excluding" if f.get("negate") else "only") + f" accounts ending in {', '.join(f['values'])}")
        elif f.get("negate"):
            notes.append(f"excluding {compress(f['values'])}")
        else:
            included.append(compress(f["values"]))
    text = ", ".join(included)
    return ", ".join([t for t in [text] + notes if t])


# ---------- Report structures ----------

def load_report(filename):
    return json.load((SOURCE / filename).open(encoding="utf-8"))["definition"]["groups"]


def index_lines(groups, index):
    for g in groups:
        index[g["key"]] = g
        index_lines(g.get("groups", []), index)
    return index


def line_detail(g, index):
    """Accounts or formula of a line, as plain text."""
    if "formula_operands" in g:
        terms = []
        for i, key in enumerate(g["formula_operands"]):
            operand = index.get(key)
            label = operand["name_en"] if operand else key
            sign = operand.get("arithmic_operator", "+") if operand else "+"
            terms.append(label if i == 0 else f"{'−' if sign == '-' else '+'} {label}")
        return "= " + " ".join(terms)
    return describe_filters(g.get("filters", []))


def jsx_text(text):
    """A JSX expression holding the text as a string literal, so no character needs escaping."""
    return "{" + json.dumps(text, ensure_ascii=False) + "}"


def render_rows(g, index, depth):
    name = jsx_text(g["name_en"])
    if g.get("is_vertical_reference"):
        name += f' <span className="def-note">{jsx_text("reference for vertical analysis")}</span>'
    indent = 0.75 + depth * 1.25
    weight = ", fontWeight: 600" if depth == 0 else ""
    row_class = "def-level-0" if depth == 0 else f"def-level-{min(depth, 3)}"
    if "formula_operands" in g:
        row_class += " def-formula"
    rows = [
        f'    <tr className="{row_class}">'
        f'<td style={{{{ paddingLeft: "{indent}rem"{weight} }}}}>{name}</td>'
        f"<td>{jsx_text(line_detail(g, index))}</td></tr>"
    ]
    for child in g.get("groups", []):
        rows += render_rows(child, index, depth + 1)
    return rows


def build_report_snippets():
    SNIPPETS.mkdir(parents=True, exist_ok=True)
    all_lines = {}
    for slug, filename in REPORTS.items():
        groups = load_report(filename)
        index = index_lines(groups, {})
        all_lines.update({k: v for k, v in index.items() if k not in all_lines})
        body = [
            f"{{/* Generated by scripts/build-definitions.py from {filename}. Don't edit by hand. */}}",
            "",
            '<table className="def-table">',
            "  <thead>",
            "    <tr><th>Line</th><th>Accounts or formula</th></tr>",
            "  </thead>",
            "  <tbody>",
        ]
        for g in groups:
            body += render_rows(g, index, 0)
        body += ["  </tbody>", "</table>"]
        (SNIPPETS / f"{slug}.mdx").write_text("\n".join(body) + "\n", encoding="utf-8")
    return all_lines


# ---------- Ratio reference ----------

def kpi_name(key, lines, ratios, ambiguous):
    if key in ratios:
        return ratios[key]["name_en"]
    if key in EXTRA_NAMES:
        return EXTRA_NAMES[key]
    if key in lines:
        name = lines[key]["name_en"]
        if name in ambiguous:
            side = "assets" if key.startswith("active_") else "liabilities" if key.startswith("passive_") else None
            if side:
                name = f"{name} ({side})"
        return name
    return key


def render_expression(node, lines, ratios, ambiguous, top=True):
    kind = node.get("type")
    if kind == "kpi":
        return kpi_name(node["kpi"], lines, ratios, ambiguous)
    if kind == "expression":
        inner = OPERATORS[node["operation"]].join(
            render_expression(t, lines, ratios, ambiguous, top=False) for t in node["terms"])
        return inner if top else f"({inner})"
    if kind == "filter":
        codes = compress([v for f in node["filters"] for v in f["values"]])
        return f"balance of accounts {codes}"
    if kind == "period_length_in_days":
        return "days in the period"
    if kind == "primitive":
        return str(node["value"])
    raise ValueError(f"Unknown node: {node}")


def build_ratio_page(lines):
    rows = list(csv.reader((SOURCE / "kpi-definitions.txt").open(encoding="utf-8")))[1:]
    ratios, duplicates = {}, []
    for row in rows:
        ratio = json.loads(row[0])
        if ratio["id"] in ratios:
            duplicates.append(ratio["id"])
            continue
        ratios[ratio["id"]] = ratio

    # Only disambiguate names that occur more than once among the lines the formulas use
    def referenced(node, found):
        if isinstance(node, dict):
            if node.get("type") == "kpi" and node["kpi"] in lines:
                found.add(node["kpi"])
            for value in node.values():
                referenced(value, found)
        elif isinstance(node, list):
            for value in node:
                referenced(value, found)
        return found
    used = set()
    for r in ratios.values():
        referenced(r["definition"], used)
    counts = {}
    for key in used:
        counts[lines[key]["name_en"]] = counts.get(lines[key]["name_en"], 0) + 1
    ambiguous = {name for name, n in counts.items() if n > 1}

    out = [
        "---",
        'title: "Ratio reference"',
        'description: "Definitions of the financial ratios in aiGust, with the formula and unit of each."',
        "---",
        "",
        "{/* Generated by scripts/build-definitions.py from kpi-definitions.txt. Don't edit by hand. */}",
        "",
        "Besides the lines of the standard reports, aiGust calculates the financial ratios below. "
        "Like every [KPI](/guide/concepts/kpis), you can use them in advanced search, triggers, dashboards and benchmarks.",
        "",
        "The formulas use the lines of the [profit and loss](/guide/reports/definitions/profit-and-loss), "
        "the [balance sheet](/guide/reports/definitions/balance-sheet) and the [cash flow](/guide/reports/definitions/cash-flow). "
        "Ratios per FTE use the average number of employees from the [social balance sheet](/guide/personnel/data-sources), "
        "so they're only available for administrations with social data. "
        "Ratios based on a period shorter or longer than a year are converted to a full year.",
        "",
    ]
    placed = set()
    groups = RATIO_GROUPS + [("Other ratios", [k for k in ratios if k not in {i for _, ids in RATIO_GROUPS for i in ids}])]
    for title, ids in groups:
        ids = [i for i in ids if i in ratios]
        if not ids:
            continue
        out += [f"## {title}", "", "| Ratio | Formula | Unit |", "|---|---|---|"]
        for i in ids:
            r = ratios[i]
            formula = escape(render_expression(r["definition"], lines, ratios, ambiguous))
            unit = "Days" if i in DAY_RATIOS else UNITS.get(r["value_type"], r["value_type"])
            out.append(f"| **{escape(r['name_en'])}** | {formula} | {unit} |")
            placed.add(i)
        out.append("")
    RATIOS_PAGE.write_text("\n".join(out), encoding="utf-8")
    return duplicates


# ---------- Built-in triggers ----------

TRIGGERS_SOURCE = ROOT / "data" / "triggers" / "trigger-definitions.json"
TRIGGERS_SNIPPET = ROOT / "snippets" / "triggers" / "built-in.mdx"

# Built-in triggers that shouldn't be documented, by English title
SKIP_TRIGGERS = {"Test"}

OPERATOR_SIGNS = {"lt": "<", "lte": "≤", "gt": ">", "gte": "≥", "eq": "=", "in": "is"}
PERIODS = {"bookyear_last": "last closed financial year", "bookytd_last": "year to date"}
COMPANY_TYPES = {
    "OPERATING_COMPANY": "operating company", "MANAGEMENT_COMPANY": "management company",
    "HOLDING": "holding", "INVESTMENT_COMPANY": "investment company", "PATRIMONIAL_COMPANY": "patrimonial company",
}
LEGAL_TYPES = {"bv": "BV", "nv": "NV", "nat_pers": "natural person (sole proprietorship)"}

# Clearer names for report lines whose name is ambiguous on its own
TRIGGER_NAMES = {
    "result_indirectcosts_directors": "Directors' remuneration",
    "result_indirectcosts_personnel": "Personnel costs",
    "result_ebitda": "EBITDA",
}


def format_number(value, decimals=0):
    text = f"{value:,.{decimals}f}"
    return text if not text.startswith("-") else "−" + text[1:]


def format_value(value, kpi_type, value_type):
    """Format a threshold for its KPI type: fractions become % or pp, amounts get €."""
    number = float(value)
    if kpi_type == "delta_abs" or (kpi_type == "rel") or (kpi_type == "abs" and value_type == "percentage"):
        return format_number(number * 100, 0 if (number * 100).is_integer() else 1) + "%"
    if kpi_type == "delta_rel":
        return format_number(number * 100, 0 if (number * 100).is_integer() else 1) + " pp"
    if value_type == "number":
        return format_number(number, 0 if number.is_integer() else 2)
    return "€" + format_number(number)


def describe_condition(condition, lines, ratios):
    left, operator, right = condition["left_operand"], condition["operator"], condition["right_operand"]
    column = left["selected_column"]
    if left["type"] == "property":
        values = [v.strip() for v in str(right).split(",")]
        if column == "company_type":
            names = [COMPANY_TYPES.get(v, v) for v in values]
            return "Company type is " + " or ".join(names)
        if column == "kbo_legal_type":
            names = [LEGAL_TYPES.get(v, v) for v in values]
            return "Legal type is " + " or ".join(names)
        return f"{column} {OPERATOR_SIGNS.get(operator, operator)} {right}"

    if column in TRIGGER_NAMES:
        name, value_type = TRIGGER_NAMES[column], "currency"
    elif column in ratios:
        name, value_type = ratios[column]["name_en"], ratios[column]["value_type"]
    else:
        name, value_type = (lines[column]["name_en"] if column in lines else column), "currency"
    reference = "turnover" if column.startswith("result_") else "total assets"
    kpi_type = left.get("kpi_type")
    subject = {
        "abs": name,
        "delta_abs": f"{name} growth",
        "rel": f"{name} as % of {reference}",
        "delta_rel": f"Change in {name if name[:2].isupper() else name[0].lower() + name[1:]} as % of {reference}",
    }.get(kpi_type, name)
    period = PERIODS.get(left.get("period_type"), left.get("period_type"))
    value = format_value(right, kpi_type, value_type)
    return f"{subject} {OPERATOR_SIGNS.get(operator, operator)} {value} ({period})"


def build_trigger_snippet(lines):
    rows = list(csv.reader((SOURCE / "kpi-definitions.txt").open(encoding="utf-8")))[1:]
    ratios = {}
    for row in rows:
        ratio = json.loads(row[0])
        ratios.setdefault(ratio["id"], ratio)

    triggers = json.load(TRIGGERS_SOURCE.open(encoding="utf-8"))["items"]
    # Built-in triggers belong to no firm; skip firm-specific and excluded ones
    built_in = [t for t in triggers if t.get("tenant_id") is None and t["title_en"] and t["title_en"] not in SKIP_TRIGGERS]

    out = [
        "{/* Generated by scripts/build-definitions.py from data/triggers/trigger-definitions.json. Don't edit by hand. */}",
        "",
        "<AccordionGroup>",
    ]
    for t in built_in:
        out += ["", f"<Accordion title={json.dumps(t['title_en'], ensure_ascii=False)}>", ""]
        out += [escape(t["description_en"].strip()), ""]
        if t["base_filter"]:
            out += ["**Applies to:**", ""]
            out += [f"- {escape(describe_condition(c, lines, ratios))}" for c in t["base_filter"]]
            out.append("")
        else:
            out += ["**Applies to:** all administrations", ""]
        out += ["**Raises an alert when:**", ""]
        out += [f"- {escape(describe_condition(c, lines, ratios))}" for c in t["trigger_filter"]]
        out += ["", "</Accordion>"]
    out += ["", "</AccordionGroup>", ""]
    TRIGGERS_SNIPPET.parent.mkdir(parents=True, exist_ok=True)
    TRIGGERS_SNIPPET.write_text("\n".join(out), encoding="utf-8")
    return len(built_in)


def main():
    lines = build_report_snippets()
    duplicates = build_ratio_page(lines)
    print(f"Wrote {len(REPORTS)} report snippets to {SNIPPETS.relative_to(ROOT)} and {RATIOS_PAGE.relative_to(ROOT)}")
    if duplicates:
        print(f"Warning: duplicate ratio ids, only the first definition is used: {', '.join(duplicates)}")
    if TRIGGERS_SOURCE.exists():
        count = build_trigger_snippet(lines)
        print(f"Wrote {count} built-in triggers to {TRIGGERS_SNIPPET.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
