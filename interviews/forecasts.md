## Topic: Forecasts and tax prepayments

### Scope today
- A forecast only extends the P&L to the end of the current financial year. Multi-year forecasting and a cash flow forecast are in development.
- Forecasts exist at administration level only, not at firm level.

### How the automatic forecast is built
- aiGust looks at the last 12 months and the same period before that, per GL account. It checks each account's growth figures and how variable it is, or whether it dropped to zero.
- It copies the same periods from the previous year into the future periods.
- Depending on how variable a line is, it either:
  - extends it at zero,
  - copies the last value, or
  - copies the same period last year with the growth figure applied.

### Forecast editor
- **Forecast overview:** forecasts are shown as cards or in a tabular view. Clicking one opens the editor.
- **Default collapsed view:** shows the previous year, the first part of this year's actuals, a yellow column where the forecast can be edited, totals for the year, and deltas against the previous year.
- **Toggle on top:** shows the individual periods, and individual cells can then be edited.
- **Editing:**
  - Click a cell to edit it.
  - A change on a parent level (e.g. turnover) is spread pro rata over the lines below it and over the periods.
  - The forecast is always saved at the lowest level, the GL account; changes at macro level are translated down to it.
  - It works like a big pivot table that recalculates immediately.
- **Scenarios:** you can save forecasts and create multiple scenarios (e.g. worst case, normal case).

### Using a forecast in reporting
- **Activating:**
  - Activate a forecast through the Data settings button (top right of the page) by selecting the forecast to use.
  - The forecast is appended to the actuals, so the open period in the dashboard, KPI dashboard and financial reports is extended with forecasted values.
- **How forecasts are marked:**
  - In charts, forecasted bars have a different surface, "with lines".
  - The table under the chart shows a forecast label on that column.
  - The result sheet clearly marks the column as forecast.
- **Limits and uses:**
  - Actuals versus budget is not shown today; it is in development.
  - Forecasts can be used in meetings and presentations to discuss with customers.
  - Benchmarks are calculated on actuals only, never on forecasts. Automatic forecasting with benchmarks is a possible future feature.

### Tax calculation and prepayments
- This is the second tab in the forecast editor. It takes the forecasted result of the chosen year.
- **Fill-in fields:** disallowed expenses (verworpen uitgaven), which are re-added, plus a few other items, possibly discounts; Bart didn't remember exactly. These give a corrected result, from which the taxable result is calculated.
- **Prepayment form per quarter:**
  - Prepayments already made are pre-filled. They are detected from bookings on specific accounts in the Belgian accounting system, so this only works when individual transactions are available.
  - Payments are assigned to the right prepayment moment, since they aren't mapped directly to financial periods; you can pay until the 10th, and there are fixed moments in time.
  - Normally detection is correct, but sometimes a payment has to be moved to the right quarter manually.
- **Wizard and penalty:** a small wizard pre-calculates suggested prepayments, which can be changed. The remaining penalty owed to the government updates immediately.
- The result is a net result calculation that takes possible prepayment penalties into account.
- There are no prepayment deadline reminders and no firm-level overview of which administrations still need a prepayment decision.

### Permissions and customer portal
- Any accountant with access to the administration can do anything at administration level, including forecasts. Key users have extra rights only for user management, templates and firm-wide settings.
- End customers can see an activated forecast in the customer portal but cannot change it or choose to factor it in.
- The accountant controls what the end customer sees, including the month until which data is visible, which can differ from the accountant portal. The customer portal settings are to be discussed in a later topic.

### Planned, not available today
- Exporting forecasts.
- Deleting scenarios.
- Copying a forecast to another year.

### Open questions
- Exact list of fill-in fields in the tax calculation beyond disallowed expenses.
- Which GL accounts are used to detect prepayments.
- Exact name and pattern of the forecast bar style.

### Screenshots to take
- Forecast overview (cards and table view).
- Forecast editor, collapsed and period views, with the yellow edit column.
- A pro rata edit in progress.
- Scenario creation.
- Data settings with forecast selection.
- Chart with forecast bars and the forecast label in the table.
- Result sheet with the forecast column.
- Tax calculation tab with fill-in fields.
- Prepayment form with wizard and penalty calculation.