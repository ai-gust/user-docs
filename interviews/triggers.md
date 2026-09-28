## Topic: Triggers and alerts

### Concept
- Triggers are firm-wide rules that generate alerts. Technically they are KPI filters, built the same way as custom peer groups.
- A trigger has two parts: a base filter, which decides which administrations it applies to, and a trigger filter, which decides when it fires.

### Built-in triggers
- There are roughly 10–15 built-in triggers. Examples:
  - Turnover up while EBITDA % drops (may be gross margin instead; open question).
  - EBITDA versus gross margin, to separate a pricing problem from a problem in other costs.
  - Change in personnel costs.
  - Liquidity.
  - YTD revenue decrease versus the same period last year beyond X%.
  - Profit with negative cash flow.
- Most run on the last closed book year and a few on YTD. Triggers can be defined either way.

### Creating a custom trigger
- **Name and description:**
  - The name appears everywhere, including on the alert inside an administration.
  - The description explains the intent to other users and is useful metadata if it's ever ingested by the AI chat agent.
  - A new trigger starts with empty filters.
- **Base filter (optional):**
  - Scopes the trigger to a subset of administrations without selecting them one by one.
  - Bart's example: a minimum revenue of €25,000 to strip out dormant companies and companies heading for retirement.
  - It can also restrict the trigger to legal types (BV, NV) or to management versus operating companies. Margin and pricing triggers suit operating companies.
- **Trigger filter:**
  - Needs at least one criterion.
  - Choosing a KPI opens a wizard that drills through the P&L structure to the exact line, then asks for the KPI type and the thresholds.
- **Calculating:**
  - Save, then open the three dots at the top → more actions → calculate. ("Three dots in aiGust always mean there is more to do.")
  - Triggers re-evaluate automatically every 24h, and you can trigger or re-trigger the calculation manually.
  - Calculation creates and removes alerts.

### Trigger overview
- Shows the list of administrations plus a progress bar. The full bar is the number of administrations the trigger applies to; the filled part is those with an active alert.
- Example: 900 eligible and 300 active means the bar is one third full.

### Customising the overview table
- One step of trigger creation shows the configuration and another shows the table. A small config option opens a side panel where KPI columns can be added, removed and reordered with drag and drop.
- Adding a column uses the same modal as the filter criteria:
  - Choose the result sheet, balance sheet, cash flow, ratios, or personnel figures and ratios (e.g. headcount, revenue per employee).
  - Drill down to the value.
  - Choose book year or YTD.
  - Choose the value type.
- Every KPI always appears as three columns: previous year, this year and delta. Bart notes this fixed set may be worth re-evaluating.
- The table defaults to the KPIs used in the filters, and the customisation is saved as part of the trigger configuration.

### Navigation
- Tenant level → triggers with their progress bars → administration list (filterable to with alerts, without alerts, or all) → administration dashboard.

### Alerts on the administration dashboard
- The alerts card shows two counters: applicable triggers and active alerts (e.g. 3 of 12).
- Clicking the card opens a side panel. Active alerts are shown by default, with a toggle to see all applicable triggers.
- Each entry shows the name, the description, and the evaluation of the criteria explaining why the alert is or isn't active.

### Snoozing and deactivating
- Each alert has a more options button.
- **Deactivate:** permanently hides the alert for that company.
- **Snooze:** opens a modal where you pick the date until which it's snoozed.
- Bart's example: profit with negative cash flow is normally worth investigating, but it's explainable for a management company that just bought a car, so you snooze it until the next book year.
- A second tab in the side panel lists snoozed and deactivated alerts, where they can be reactivated or the snooze cleared.

### Permissions
- Only key users can create and manage triggers today. Under the hood everything is permission-based: a role is a combination of permissions, and roles will become manageable in the near future.
- Key users can create and delete triggers, and can subscribe or unsubscribe from the built-in aiGust triggers. Unsubscribing hides a trigger firm-wide; it can be re-subscribed later.
- Triggers exist only at firm level, never per administration.

### Notifications
- None today: no emails and no notification inbox in aiGust.

### Open questions
- The full list of built-in triggers and what each one means (Bart needs his PC).
- Whether the turnover-versus-margin trigger uses EBITDA or gross margin.

### Screenshots to take
- Firm-level trigger overview with the progress bar.
- Trigger creation screen with name and description.
- Base filter and trigger filter editors.
- KPI selection wizard.
- Three-dots more actions menu.
- Trigger table config side panel.
- Administration list with its filter options.
- Alerts card on the administration dashboard.
- Alerts side panel showing the criteria evaluation.
- Snooze modal.
- Second tab with snoozed and deactivated alerts.