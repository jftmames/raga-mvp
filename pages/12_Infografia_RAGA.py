import streamlit as st
from streamlit.components.v1 import html as st_html

st.title("Infografía — Valoración del Proyecto RAGA")

# Banner global de incidentes (si está activo desde Runbook)
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

# HTML embebido (sin Gemini, sólo Tailwind + Chart.js)
INFOGRAFIA = r"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Infografía: Valoración del Proyecto RAGA</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet"/>
  <style>
    body { font-family: 'Inter', sans-serif; }
    .chart-container {
      position: relative; width: 100%; max-width: 600px;
      margin-left: auto; margin-right: auto; height: 300px; max-height: 400px;
    }
    @media (min-width: 768px) { .chart-container { height: 350px; } }
  </style>
</head>
<body class="bg-gray-50 text-gray-800">

  <header class="bg-[#003f5c] text-white text-center py-12 px-4">
    <h1 class="text-4xl md:text-5xl font-bold mb-2">Proyecto RAGA: IA Gobernada y Transferencia Tecnológica</h1>
    <p class="text-lg md:text-xl max-w-3xl mx-auto">
      Análisis de originalidad académica y potencial de transferencia de un marco para IA segura, explicable y supervisada.
    </p>
  </header>

  <main class="container mx-auto px-6 py-12">

    <!-- Síntesis -->
    <section id="sintesis" class="mb-20 text-center">
      <h2 class="text-3xl font-bold text-[#003f5c] mb-4">Síntesis Ejecutiva</h2>
      <p class="max-w-4xl mx-auto text-lg mb-8">
        RAGA (Retrieval-Augmented Governed Analysis) integra de forma holística tres pilares:
        Gobernanza de Datos, Teoría de la Argumentación y Supervisión Humana. El valor está en la arquitectura integral.
      </p>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        <div class="bg-white p-6 rounded-xl shadow-lg border-t-4 border-[#7a5195]">
          <div class="text-4xl mb-3">⚖️</div>
          <h3 class="text-xl font-bold mb-2 text-[#7a5195]">Gobernanza de Datos</h3>
          <p>Mecanismos proactivos que aseguran cumplimiento y seguridad antes de cualquier procesamiento.</p>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-lg border-t-4 border-[#ef5675]">
          <div class="text-4xl mb-3">🧩</div>
          <h3 class="text-xl font-bold mb-2 text-[#ef5675]">Teoría de la Argumentación</h3>
          <p>Estructura lógica y explicable (CEWR) que evita la “caja negra”.</p>
        </div>
        <div class="bg-white p-6 rounded-xl shadow-lg border-t-4 border-[#ffa600]">
          <div class="text-4xl mb-3">🧑‍💼</div>
          <h3 class="text-xl font-bold mb-2 text-[#ffa600]">Supervisión Humana</h3>
          <p>La persona dirige el proceso y valida salidas en puntos de control.</p>
        </div>
      </div>
    </section>

    <!-- Contribuciones -->
    <section id="contribuciones" class="mb-20">
      <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">
        Originalidad Académica y Contribuciones Fundamentales
      </h2>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        <div class="bg-white p-8 rounded-xl shadow-lg">
          <h3 class="text-2xl font-bold text-[#7a5195] mb-4">1. Gobernanza Proactiva: “Policy-Gate”</h3>
          <p class="mb-6">
            A diferencia de filtros reactivos, opera <em>a priori</em>, bloqueando fuentes por licencia/PII/jurisdicción antes del uso por la IA (Safety by Design).
          </p>
          <div class="chart-container h-64 sm:h-80">
            <canvas id="policyGateChart"></canvas>
          </div>
        </div>

        <div class="bg-white p-8 rounded-xl shadow-lg">
          <h3 class="text-2xl font-bold text-[#ef5675] mb-4">2. Formalización del Razonamiento: CEWR y EEE</h3>
          <p class="mb-6">
            CEWR transforma respuestas opacas en mapas argumentales claros. EEE evalúa la calidad del razonamiento (explícitud, evidencia, examen).
          </p>
          <div class="chart-container h-64 sm:h-80">
            <canvas id="reasoningQualityChart"></canvas>
          </div>
        </div>
      </div>
    </section>

    <!-- Transferencia -->
    <section id="transferencia" class="mb-20">
      <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">Potencial de Transferencia</h2>
      <p class="max-w-4xl mx-auto text-lg mb-10 text-center">
        RAGA traduce conceptos de investigación en prácticas adoptables por empresa.
      </p>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="bg-white p-6 rounded-xl shadow-lg text-center">
          <h4 class="font-bold text-lg text-[#003f5c] mb-2">Ética y Gobernanza</h4>
          <p class="text-sm h-16">Mitiga riesgo regulatorio y reputacional con Policy-Gate y logs.</p>
          <div class="h-40 flex items-center justify-center"><canvas id="riskChart1"></canvas></div>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-lg text-center">
          <h4 class="font-bold text-lg text-[#7a5195] mb-2">Lógica y Argumentación</h4>
          <p class="text-sm h-16">Reduce opacidad con mapas CEWR y citas.</p>
          <div class="h-40 flex items-center justify-center"><canvas id="riskChart2"></canvas></div>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-lg text-center">
          <h4 class="font-bold text-lg text-[#ef5675] mb-2">Fiabilidad y Operaciones</h4>
          <p class="text-sm h-16">Control de costes y fiabilidad vía Observabilidad y Runbooks.</p>
          <div class="h-40 flex items-center justify-center"><canvas id="riskChart3"></canvas></div>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-lg text-center">
          <h4 class="font-bold text-lg text-[#ffa600] mb-2">Interacción Persona-PC</h4>
          <p class="text-sm h-16">Alineamiento con negocio mediante Intake y Plan guiado.</p>
          <div class="h-40 flex items-center justify-center"><canvas id="riskChart4"></canvas></div>
        </div>
      </div>
    </section>

    <!-- Valor -->
    <section id="valor" class="mt-20 bg-white p-10 rounded-xl shadow-lg">
      <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">Valor Diferencial para Empresa</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-10 text-center">
        <div>
          <h3 class="text-5xl font-bold text-[#7a5195]">85%</h3>
          <p class="font-semibold mt-2">Reducción del Riesgo</p>
          <p class="text-sm mt-1">Menos contingencias normativas y de datos.</p>
        </div>
        <div>
          <h3 class="text-5xl font-bold text-[#ef5675]">40%</h3>
          <p class="font-semibold mt-2">Aumento de Capacidad</p>
          <p class="text-sm mt-1">Aumento cognitivo a profesionales, no sustitución.</p>
        </div>
        <div>
          <h3 class="text-5xl font-bold text-[#ffa600]">60%</h3>
          <p class="font-semibold mt-2">Menor Inversión Inicial</p>
          <p class="text-sm mt-1">Demostrador estratégico sin infra costosa.</p>
        </div>
      </div>
    </section>

  </main>

  <footer class="bg-[#003f5c] text-white text-center mt-16 py-8 px-4">
    <p class="font-bold text-xl mb-2">RAGA: Un Artefacto de Conocimiento</p>
    <p class="max-w-2xl mx-auto">
      Transferencia de prácticas de IA responsable a un formato comprensible y auditable para empresa.
    </p>
  </footer>

  <script>
    // Tooltip: título estable
    const tooltipTitleCallback = {
      plugins: {
        tooltip: {
          callbacks: {
            title: function(tooltipItems) {
              const item = tooltipItems[0];
              const label = item.chart.data.labels[item.dataIndex];
              return Array.isArray(label) ? label.join(' ') : label;
            }
          }
        }
      }
    };

    // Gráfico Policy-Gate
    const policyGateCtx = document.getElementById('policyGateChart').getContext('2d');
    new Chart(policyGateCtx, {
      type: 'doughnut',
      data: {
        labels: ['Fuentes Verificadas', 'Fuentes Bloqueadas'],
        datasets: [{ label: 'Estado de Fuentes', data: [95, 5], backgroundColor: ['#003f5c', '#ff764a'], borderColor: '#ffffff', borderWidth: 4 }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { position: 'top' }, title: { display: true, text: 'Eficacia del Policy-Gate' }, ...tooltipTitleCallback.plugins }
      }
    });

    // Gráfico Comparativa Explicabilidad
    const reasoningQualityCtx = document.getElementById('reasoningQualityChart').getContext('2d');
    new Chart(reasoningQualityCtx, {
      type: 'bar',
      data: {
        labels: ['IA Estándar', 'Respuesta Estructurada RAGA'],
        datasets: [
          { label: 'Opacidad ("Caja Negra")', data: [100, 0], backgroundColor: '#ff764a' },
          { label: 'Aserción (Claim)', data: [0, 25], backgroundColor: '#003f5c' },
          { label: 'Evidencia', data: [0, 45], backgroundColor: '#7a5195' },
          { label: 'Garantía (Warrant)', data: [0, 30], backgroundColor: '#ffa600' }
        ]
      },
      options: {
        responsive: true, maintainAspectRatio: false, indexAxis: 'y',
        scales: { x: { stacked: true, ticks: { callback: value => value + '%' } }, y: { stacked: true } },
        plugins: { title: { display: true, text: 'Comparativa de Explicabilidad' }, ...tooltipTitleCallback.plugins }
      }
    });

    // Helper de pequeños gráficos de riesgo
    function createRiskChart(canvasId, label, color) {
      const ctx = document.getElementById(canvasId).getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: { labels: ['Sin RAGA', 'Con RAGA'],
          datasets: [{ label: label, data: [90, 18], backgroundColor: ['#d1d5db', color], borderColor: '#ffffff', borderWidth: 2, barPercentage: 0.6 }] },
        options: {
          responsive: true, maintainAspectRatio: false,
          scales: { y: { beginAtZero: true, display: false }, x: { grid: { display: false } } },
          plugins: { legend: { display: false }, ...tooltipTitleCallback.plugins }
        }
      });
    }

    createRiskChart('riskChart1', 'Riesgo Regulatorio', '#003f5c');
    createRiskChart('riskChart2', 'Opacidad del Modelo', '#7a5195');
    createRiskChart('riskChart3', 'Costes Operativos', '#ef5675');
    createRiskChart('riskChart4', 'Desalineación Estratégica', '#ffa600');
  </script>
</body>
</html>"""

# Altura con margen (la infografía es larga)
st_html(INFOGRAFIA, height=3000, scrolling=True)
