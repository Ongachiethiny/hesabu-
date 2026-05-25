import { useState } from 'react';

const calculators = [
  {
    key: 'mechanical',
    title: 'Mechanical',
    subtitle: 'Torque and load checks',
    description:
      'Capture dimensions, forces, and safety factors in one place before the backend calculator takes over.',
    fieldName: 'input_value',
    fieldLabel: 'Input value',
    fieldType: 'number',
    placeholder: 'e.g. 1250',
    endpoint: '/api/calculators/mechanical/preview',
    accent: false,
  },
  {
    key: 'structural',
    title: 'Structural',
    subtitle: 'Beam and section analysis',
    description:
      'Track spans, reactions, and section properties with a layout built for quick iteration.',
    fieldName: 'load_case',
    fieldLabel: 'Load case',
    fieldType: 'text',
    placeholder: 'Dead + live load',
    endpoint: '/api/calculators/structural/preview',
    accent: true,
  },
  {
    key: 'electrical',
    title: 'Electrical',
    subtitle: 'Voltage and current planning',
    description:
      'Prepare circuit parameters now so the backend can calculate the practical values later.',
    fieldName: 'circuit_label',
    fieldLabel: 'Circuit label',
    fieldType: 'text',
    placeholder: 'Lighting circuit A',
    endpoint: '/api/calculators/electrical/preview',
    accent: false,
  },
];

function CalculatorCard({ calculator }) {
  const [value, setValue] = useState('');
  const [output, setOutput] = useState('');
  const [running, setRunning] = useState(false);

  const runPreview = async () => {
    setRunning(true);
    setOutput('Calling backend preview endpoint...');

    try {
      const payload = {
        [calculator.fieldName]: calculator.fieldType === 'number' ? Number(value) : value,
      };

      const response = await fetch(calculator.endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = await response.json();
      setOutput(`${data.domain.toUpperCase()} preview\n${JSON.stringify(data.result, null, 2)}`);
    } catch (error) {
      setOutput(`Unable to reach the backend: ${error.message}`);
    } finally {
      setRunning(false);
    }
  };

  return (
    <article className={`card panel ${calculator.accent ? 'accent' : ''}`}>
      <div className="panel-head">
        <span>{calculator.title}</span>
        <span className="pill">Draft</span>
      </div>
      <h2>{calculator.subtitle}</h2>
      <p>{calculator.description}</p>
      <label>
        {calculator.fieldLabel}
        <input
          name={calculator.fieldName}
          type={calculator.fieldType}
          min={calculator.fieldType === 'number' ? '0' : undefined}
          step={calculator.fieldType === 'number' ? '0.01' : undefined}
          placeholder={calculator.placeholder}
          value={value}
          onChange={(event) => setValue(event.target.value)}
        />
      </label>
      <button className="button primary full" type="button" onClick={runPreview} disabled={running}>
        {running ? 'Running...' : 'Run preview'}
      </button>
      <output className="result" aria-live="polite">
        {output}
      </output>
    </article>
  );
}

export default function App() {
  return (
    <>
      <div className="bg-orb bg-orb-left" />
      <div className="bg-orb bg-orb-right" />

      <main className="shell">
        <section className="hero card">
          <div className="eyebrow">Hesabu+ Engineering Suite</div>
          <h1>Model calculations with a cleaner, faster workflow.</h1>
          <p className="lede">
            A focused workspace for mechanical, structural, and electrical analysis.
            Start with the React frontend today and wire in backend logic as the
            calculation engine grows.
          </p>

          <div className="hero-actions">
            <a className="button primary" href="#calculators">Open calculators</a>
            <a className="button secondary" href="#workflow">View workflow</a>
          </div>

          <div className="metrics">
            <div>
              <strong>3</strong>
              <span>calculation domains</span>
            </div>
            <div>
              <strong>1</strong>
              <span>shared workspace</span>
            </div>
            <div>
              <strong>React</strong>
              <span>frontend foundation</span>
            </div>
          </div>
        </section>

        <section id="calculators" className="grid">
          {calculators.map((calculator) => (
            <CalculatorCard key={calculator.key} calculator={calculator} />
          ))}
        </section>

        <section id="workflow" className="card workflow">
          <div>
            <div className="eyebrow">Workflow</div>
            <h2>Designed to bridge React input and backend calculation.</h2>
          </div>

          <ol>
            <li>Capture engineering inputs in the React frontend.</li>
            <li>Send the data to backend endpoints as they are implemented.</li>
            <li>Render clear outputs, warnings, and calculation summaries.</li>
          </ol>
        </section>
      </main>
    </>
  );
}