## Topic: Benchmarking

### Peer group criteria
- System-defined peer groups come out of the box. They are built per subsector and split by company type (management company versus operating company), so IT management companies sit in a different group from IT operating companies.
- Custom peer groups use the same filter mechanism as advanced search at tenant level.
- There are two families of criteria:
  - Any KPI with any of the four KPI types, for example turnover between 2 and 5 million, solvability, liquidity or headcount.
  - Administration properties: province (derived from the address), legal type, company type, sector and subsector.
- Criteria combine with AND. Within a single criterion you can use OR, for example legal type BV or NV, or province Limburg or West Flanders.

### Membership year
- The default is the last closed book year, determined from today's actual date, not from the administration's up-to-date-until date.
- Year-to-date filtering was recently added as an option.

### Calculation
- You press the calculate button when creating a peer group, and you can trigger a recalculation manually.
- Requests go into a queue and typically take 10–30 minutes.

### Privacy minimum
- A group with fewer than 10 peers can't be selected or calculated.
- Because the database changes, a group can have 10 or more peers today but fewer than 10 in an earlier book year. Benchmarks then show only for the years with enough data. This is rare, but it happens with tight criteria that sit around 10–11 peers.

### Book year matching
- There is no pro-rating. Your administration's book year is the reference, and each peer's book year with the greatest overlap is mapped onto it.
- Example: a peer closing on 30 September maps its year ending September 2025 onto your year ending December 2025, based on a 9-month overlap.
- On an exact 6-month tie the older book year wins. This is deliberate, so peers whose current book year hasn't closed yet don't drop out and push the group below 10.
- Most files close in March, June, September or December.

### Year-to-date matching
- Your YTD window (e.g. 1 January–31 May) is replicated into previous years and into the peers.
- The system looks for a period, or a combination of periods, within a single book year that fully overlaps the window, then pro-rates.
- Book years are never combined, so a peer closing in March, whose window spans two book years, can't contribute.
- Annual-only files, common from Silverfin, are hard to map.
- Flagged for Bart's double-check.

### Charts
- Bar charts are used for absolute values and line charts for percentages and margins.
- Your own data uses the firm's main accent colour and benchmarks use the secondary accent colour.
- Q0, Q25, Q50, Q75 and Q100 are all calculated. By default the chart shows a band from Q25 to Q75; Q0 and Q100 aren't used elsewhere.
- The median is hidden by default because it overloaded the chart, and can be toggled on.
- Below every chart, a table repeats the plotted numbers, with a show/hide toggle for each benchmark line. Hiding either quartile line collapses the band.

### KPI cards
- Configurable on the dashboard. The main value can be:
  - Absolute, with a coloured patch showing the rise or fall.
  - Relative (vertical analysis), e.g. EBITDA as a percentage of revenue, where the patch shows the change in percentage points (−5 when going from 45% to 40%).
- The benchmark toggle adds a small boxplot to the card showing the band, the median and a dot for your own value.
- Cards follow the global data setting at the top of the page (book year or YTD). In book year mode they always show the last closed book year, never the open year.

### Performance vs benchmark
- A dashboard widget, also available as a slide widget. It is modelled on IntelliFin's five-star mechanism and was requested by an investor.
- Each company starts with a base score of 5/10. Five KPIs each add +1, 0 or −1: above the band earns a point, inside the band earns 0, below the band loses a point.
- A standalone version scores the company's own values against fixed thresholds instead of against peers.
- KPI sentiment flips the direction: rising turnover is good, rising costs are bad.
- Bart considers the feature rudimentary and due for rework, since not every KPI matters equally for every administration.

### Explaining quartiles
- **The class example:**
  - In a class of 25, one child scores 65% on a maths exam. Is that bad? Schools usually only give you the median.
  - Rank all the grades from low to high. The quartiles mark the middle 50% band, with the nerds as outliers above it and the laggards below.
- **Then swap the class for a peer group:**
  - A logistics company with 3M revenue is compared with other road transport companies, filtered to roughly 1–7M revenue so the single-truck operator doesn't skew the result.
  - About 20 peers are found. Revenue growth is calculated for each one, the values are ranked and the quartiles are taken.
- Individual values are never shown, only the bands.

### Reading the right KPI type (deserves a dedicated section)
- Absolute-value benchmarks are valuable for judging level and size, but they can't support conclusions about growth. For growth you need the horizontal-delta benchmark.
- Likewise, a relative-value benchmark tells you whether your EBITDA margin is good compared with others. Only the benchmark of the delta of the relative value tells you whether margins were under pressure.
- This is where people make vital errors.

### Open questions
- How often peer groups recalculate automatically (nightly or weekly).
- Whether YTD benchmarking pro-rates a fully overlapping period as described.
- Whether the KPI card boxplot uses Q0 and Q100 for its whiskers.
- The exact five KPIs behind Performance vs benchmark, and their thresholds.

### Screenshots to take
- Peer group creation and filter screen.
- Peer group suggestions screen.
- Data settings selector at the top of the portal.
- Chart with the benchmark band, plus the table with its toggles.
- KPI card with the boxplot.
- Performance vs benchmark widget.
- The quartile explanation chart (Bart to provide).
- The presentation with the absolute-versus-growth example (Bart to provide).