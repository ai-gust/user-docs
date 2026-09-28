## Topic: Financial reports

### Standard definitions
- Built on the Belgian MAR plus an example from books, refined through user feedback until acceptable to most firms.
- The balance sheet needs little customisation; the result sheet draws many customisation requests.
- Definitions are visible in the UI.
- Rough P&L structure (uncertain, check against Bart's detailed document):
  - Revenue: sales and work in progress (70/71).
  - Direct costs (60), including change in stock, giving gross margin.
  - 61, with 618 interim costs split out.
  - Personnel costs 62, split into management, labour workers and office workers.
  - Other costs, with 74/73 somewhere in this section.
  - Recurring versus non-recurring split unclear at this point, giving EBITDA.
  - One-time costs, depreciations and financial costs, giving taxable result.
  - Taxes, giving net result after taxes.
  - Processing of the result for the balance sheet.
- Definitions are entirely fixed today. A custom "management reports" feature is in development.

### Contribution margin and fixed/variable costs
- Only on the P&L today.
- It's a label set at GL account level, on 61 and probably 62 accounts, and it holds a fixed/variable percentage rather than a yes/no choice.
- Indirect costs are split: the variable portion sits above the contribution margin and the fixed portion below it, in near-identical sections.
- Gross margin (70 minus 60) is deliberately left untouched, so benchmarking stays comparable and users don't tailor their own margins.
- It can be set in two places:
  - Inline in the result sheet table view. A settings toggle enables fixed/var, and on eligible rows a small button next to the GL account shows the percentage and opens a slider to edit it.
  - Administration settings → mapping tab (same place as label mapping), for bulk editing whole sections or changing individual accounts.
- Fixed/var appears nowhere else today: not in KPIs, dashboards or benchmarks. Dashboard support is likely to be added.

### Report settings panel (settings/configuration button on top of the report)
- **Horizontal analysis toggle:** adds a growth or decrease column between periods.
- **Vertical analysis:** a three-way setting (absolute numbers, percentages, or both) rather than a toggle.
- **Year-to-date flag:** book years are the default. In YTD mode the columns show the same slice of time (e.g. 1 January–31 May) repeated across years.
- **Open periods toggle (book year view only):**
  - Example: an administration closing on 31 December, with data up to date until May, has 1 January 2026–31 May 2026 as its open period.
- YTD and open periods are also global settings on the Data settings page, added because people found it hard to tell whether they were looking at YTD or book year. They can still be changed directly from the report settings menu.
- **Grouping of the lowest level:** by GL account, by aiGust label, or by business partner.
  - The business partner option shows the most important partners within a section, which typical bookkeeping systems don't offer.
- **Alerts (colour coding):** not linked to triggers and alerts.
  - It colours the horizontal deltas green, light green, yellow, orange or red.
  - Severity combines two things: how large the line is relative to the total (a cost of 0.1% of revenue doesn't matter) and how large the change is (+100% matters more than +1%).
  - It can be toggled on or off.

### Column header options (three dots on each column header)
- "Three dots in aiGust always mean there is more you can do."
- **Sorting:**
  - Applies only to the detail rows at the lowest level. Revenue stays on top and gross margin stays below revenue and direct costs.
  - Detail rows can be sorted by GL account (61000 before 61001, 61002) or by the figures of the last or previous financial year.
- **Drill-down into periods or quarters:** see next section.

### Quarter and period view
- **What changes:**
  - It changes the aggregation level. Clicking book year 2025 lets you drill into quarters, or into months or periods if available.
  - The columns become 2025 Q1, Q2 and so on, as many as fit on the screen.
- **Comparison:**
  - With horizontal analysis on, each quarter is compared with the same slice of time in the previous year, not with the previous quarter.
  - Matching is based on time period, not on quarter labels. In an extended book year the last quarter may be Q5 or Q6, which maps to Q4 of the following year.
- **Why it's sometimes unavailable:**
  - Quarters and periods are built from the periods the source system delivers (see the financial periods topic).
  - Exact and Yuki files are mostly monthly bookers. Quarterly bookers are rarer, and one 12-month period is an exception today.
  - With no period-level data the option is greyed out. There is no pro-rating.
  - It's rather common because some administrations only have Silverfin or Adsolut fiscal-file data. These are compliance systems: aiGust receives balance totals (proef- en saldibalans), not transactions, and is limited to the periods created there.
  - Silverfin files are often reconciled once a year because it's cheaper, giving a single full-year period. Sometimes there are exotic cases such as periods of 8 and 12 months, or 4 months.

### Cell details (click a cell → side panel with tabs)
- **Transactions tab:**
  - Shows the transactions behind that cell (e.g. book year 2025 revenue = all 70 accounts in that year).
  - The list is already pre-filtered and adds up to the number in the cell. Today it can only be filtered further by business partner. A separate page exists for searching all transactions.
  - There's an export button.
  - Clicking a transaction shows its details, including the invoice when one is attached.
- **Evolution tab:**
  - A KPI chart at the chosen aggregation level (book year or YTD) with benchmarks. The last period shown is the one you clicked.
  - Every line in the result sheet and balance sheet is a KPI and is benchmarked.
- **Contributors tab:**
  - Same visual as the "top contributors" widget on the customer/supplier report, which can also be added to the slide deck.
  - A pie chart with a table of the top contributors in the period. Example: clicking 61 services for 2025 shows €600,000 in costs, €100,000 from supplier one, €50,000 from supplier two, and so on.
  - Top five by default; more can be added and specific contributors filtered out.
  - Below that are two tables, biggest risers and biggest fallers, comparing this period to the previous one in absolute numbers.
  - The underlying data is transactions aggregated per period and grouped by business partner, GL account and aiGust label. The contributors view keeps one of the three dimensions and drops the other two, and you can switch between business partner, GL account and label.
- **Comments:**
  - Saved against the period and the specific line.
  - The cell is highlighted in the firm's accent colour. Parent cells show a small indicator that a comment exists further down, since comments can be placed on an individual GL account.
  - Comments are threads, so others can reply.
  - Flags: public or internal (public comments are visible to end customers in the customer portal), and to-do/action point.

### Waterfall chart (P&L and cash flow)
- **Layout:**
  - Always one individual year. A table on the left shows that year only; deltas and vertical values can be shown, but not the previous year's absolute values.
  - The waterfall on the right is aligned with the table.
- **How to read it:**
  - Example: €1M revenue is a green bar to the right, €500,000 direct costs a red bar bringing the line down, and gross margin appears in the accent colour at €500,000.
  - The chart continues down to net result, showing where the biggest impact on the result is.
- **Cash flow:**
  - Starts from the liquidities at the end of the previous book year, shows the mutations split into operational, financial and investment cash flow, and ends with the closing liquidities.
  - This shows why a profit doesn't necessarily mean cash grew equally.
- **Drill-down:**
  - Lines can be clicked to drill down into a section, for example the indirect cash flow lines within operational cash flow: the result with non-cash items filtered out, stock growth, customers paying later.
  - You can navigate back up.
  - Individual cells keep the same cell details as the normal table: chart, transactions and so on.

### Balance sheet visual
- A block presentation of the balance sheet, not a waterfall.
- Assets ("active") sit on the left, split into fixed and current assets, and liabilities ("passive") on the right.
- The two sides are always equal, though negative numbers are harder to display; there is a presentation for them.
- Clicking a block drills down, for example current assets → liquidities, stock and so on.
- Balance-sheet KPI cards sit on top: solvency, liquidity (e.g. 1.2), net working capital and working capital needs.
- Clicking a card shows the formula and its calculation on the left, and highlights the blocks involved in the chart.

### Administration dashboard
- **Main part (KPI dashboard):**
  - One large chart with benchmarks and a table of the plotted values below it.
  - KPI cards on top (e.g. absolute revenue with horizontal delta and benchmark). Clicking a card switches the chart, for example to EBITDA.
- **Edit dashboard button (top right):**
  - Opens a side panel where you pick from dashboard templates (a template is a list of KPIs).
  - KPIs are added through the standard modal and reordered with drag and drop.
  - Firm-level templates are part of the firm setup topic; customisation is also possible per administration.
- **Other widgets:**
  - Alerts: number of applicable and active triggers.
  - Sector, subsector and company type: can be confirmed or updated.
  - Up-to-date-until date: same as the Data settings at the top of the page, and can be changed.
  - Data sources:
    - Shows the source (e.g. Exact or Adsolut), the last update, and which data is imported and why (e.g. no transactions for Silverfin-only files).
    - Ad hoc sync button, which typically takes 5–15 minutes.
    - Option to switch data source when the administration is found in multiple packages.
  - AI analysis: beta, generates discussion points. Work in progress; not to be covered in depth now.
- **Buttons on top:**
  - Follow/unfollow: marks administrations you manage, like starring a mail, so alerts can be shown only for followed administrations or for the whole portfolio.
  - Switch to customer portal: see the administration as the end customer sees it.
  - Edit dashboard.

### Global and personal view settings
- **Where they live:**
  - Firm level: workspace → report settings, applying to all users.
  - User level: user icon (top right) → profile (also language and name), which overrides the firm settings.
- **Column direction:** left-to-right or right-to-left. The National Bank of Belgium often shows the newest year on the left, and accountants differ in which they prefer.
- **Compact notation:** 6K versus 6,000. Compact is the default.
- **Hide/unhide empty lines:** empty lines are hidden by default when a line is empty in all years.
- **Number of periods to show:**
  - Set separately for quarter/period view and book year view.
  - The table shows as much as fits, with scroll buttons on top.
  - This matters on laptops and in presentation mode, where comparisons with previous years widen the table.

### Delta badge sensitivities
- Sensitivity thresholds for the coloured delta badges, based on the vertical value and the horizontal change, are set at aiGust level and can be overridden per firm in the workspace.

### Open questions
- Detailed P&L, balance sheet and cash flow definitions (Bart to provide the document).
- Where 74/73 sits, and how recurring versus non-recurring costs are treated.
- Whether fixed/var applies to 62 accounts.
- List of ratios with formulas (Bart to send as a table).
- Exact names of the colour levels and the default sensitivity thresholds.
- AI analysis widget: work in progress, to be covered later.

### Screenshots to take
- Report settings panel.
- Column header three-dots menu with sorting and drill-down.
- Quarter view with horizontal analysis.
- Greyed-out drill-down on a Silverfin file.
- Each cell details tab (transactions, evolution, contributors) and a comment thread with its flags.
- Parent cell comment indicator.
- Delta colour coding.
- P&L waterfall.
- Cash flow waterfall with drill-down.
- Balance sheet block visual with a KPI card selected.
- Administration dashboard with widgets.
- Edit dashboard side panel.
- Data sources widget.
- Workspace report settings and user profile view settings.
- Fixed/var slider and mapping tab.