// KPI type icons, matching the aiGust app (Material Symbols Outlined, weight 400).
// Usage in MDX: import { KpiTypeIcon } from "/snippets/kpi-type-icon.jsx";  <KpiTypeIcon type="horizontal" />

export const KpiTypeIcon = ({ type }) => {
  const paths = {
    euro: "M600-120q-115 0-212.5-67.5T255-370H120v-60h123q-4-28-3.5-50t3.5-50H120v-60h135q35-115 132.5-182.5T600-840q69 0 129.5 23.5T840-748l-43 42q-41-36-92-55t-105-19q-94 0-171.5 52.5T319-590h281v60H304q-5 27-5 50t5 50h296v60H319q32 85 109.5 137.5T600-180q53 0 104-18t94-56l42 42q-44 42-107 67t-133 25Z",
    numbers: "m239-160 40-159H120l15-60h159l51-202H186l15-60h159l39-159h59l-39 159h203l39-159h59l-39 159h159l-15 60H666l-51 202h159l-15 60H600l-40 159h-59l40-159H338l-40 159h-59Zm114-219h203l51-202H404l-51 202Z",
    percent: "M289.9-540q-53.9 0-91.9-38.1-38-38.1-38-92t38.1-91.9q38.1-38 92-38t91.9 38.1q38 38.1 38 92T381.9-578q-38.1 38-92 38Zm-.02-60q29.12 0 49.62-20.38 20.5-20.38 20.5-49.5t-20.38-49.62q-20.38-20.5-49.5-20.5t-49.62 20.38q-20.5 20.38-20.5 49.5t20.38 49.62q20.38 20.5 49.5 20.5ZM669.9-160q-53.9 0-91.9-38.1-38-38.1-38-92t38.1-91.9q38.1-38 92-38t91.9 38.1q38 38.1 38 92T761.9-198q-38.1 38-92 38Zm49.6-80.38q20.5-20.38 20.5-49.5t-20.38-49.62q-20.38-20.5-49.5-20.5t-49.62 20.38q-20.5 20.38-20.5 49.5t20.38 49.62q20.38 20.5 49.5 20.5t49.62-20.38ZM202-160l-42-42 598-598 42 42-598 598Z",
    trending_up: "m123-240-43-43 292-291 167 167 241-241H653v-60h227v227h-59v-123L538-321 371-488 123-240Z",
    change_history: "m80-160 401-640 399 640H80Zm107-60h586L481-685 187-220Zm293-233Z",
  };

  const names = {
    currency: "euro",
    number: "numbers",
    percentage: "percent",
    vertical: "percent",
    horizontal: "trending_up",
  };

  const style = { display: "inline-block", verticalAlign: "-0.2em" };

  // Vertical delta: change_history with a small percent sign at the top right, as in the app
  if (type === "vertical-delta") {
    return (
      <svg viewBox="0 -960 1160 960" width="1.45em" height="1.2em" fill="currentColor" style={style} role="img" aria-label="Vertical delta">
        <path d={paths.change_history} />
        <path d={paths.percent} transform="translate(632 -432) scale(0.55)" />
      </svg>
    );
  }

  const name = names[type] || "euro";
  return (
    <svg viewBox="0 -960 960 960" width="1.2em" height="1.2em" fill="currentColor" style={style} role="img" aria-label={type}>
      <path d={paths[name]} />
    </svg>
  );
};
