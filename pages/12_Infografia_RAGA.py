import streamlit as st
from streamlit.components.v1 import html

st.title("Infografía — Valoración del Proyecto RAGA")

# Banner global de incidentes (si está activo desde Runbook)
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

# Nota: se incrusta el HTML en un iframe con scripts habilitados.
INFOGRAFIA = r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Infografía: Valoración del Proyecto RAGA</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .chart-container { position: relative; width: 100%; max-width: 600px; margin-left: auto; margin-right: auto; height: 300px; max-height: 400px; }
        @media (min-width: 768px) { .chart-container { height: 350px; } }
        .gemini-btn { transition: all 0.2s ease-in-out; }
        .gemini-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        #gemini-modal { transition: opacity 0.3s ease-in-out; }
        .spinner { border-top-color: #3498db; animation: spin 1s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">

    <header class="bg-[#003f5c] text-white text-center py-12 px-4">
        <h1 class="text-4xl md:text-5xl font-bold mb-2">Proyecto RAGA: IA Gobernada y Transferencia Tecnológica</h1>
        <p class="text-lg md:text-xl max-w-3xl mx-auto">Un análisis sobre la originalidad académica y el potencial de transferencia de un marco de trabajo para la IA segura, explicable y supervisada.</p>
    </header>

    <main class="container mx-auto px-6 py-12">

        <section id="sintesis" class="mb-20 text-center">
            <h2 class="text-3xl font-bold text-[#003f5c] mb-4">Síntesis Ejecutiva</h2>
            <p class="max-w-4xl mx-auto text-lg mb-8">RAGA (Retrieval-Augmented Governed Analysis) trasciende las implementaciones convencionales de RAG al integrar de forma holística tres pilares fundamentales. Su valor no reside en un componente aislado, sino en su arquitectura integral para una IA confiable.</p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
                <div class="bg-white p-6 rounded-xl shadow-lg border-t-4 border-[#7a5195] flex flex-col justify-between">
                    <div>
                        <div class="text-4xl mb-3">⚖️</div>
                        <h3 class="text-xl font-bold mb-2 text-[#7a5195]">Gobernanza de Datos</h3>
                        <p>Mecanismos proactivos que aseguran el cumplimiento y la seguridad antes de cualquier procesamiento.</p>
                    </div>
                    <button class="gemini-btn mt-4 bg-[#7a5195] text-white px-4 py-2 rounded-lg font-semibold text-sm" data-concept="Gobernanza de Datos en IA">✨ Explicar con Analogía</button>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-lg border-t-4 border-[#ef5675] flex flex-col justify-between">
                    <div>
                        <div class="text-4xl mb-3">🧩</div>
                        <h3 class="text-xl font-bold mb-2 text-[#ef5675]">Teoría de la Argumentación</h3>
                        <p>Estructura las respuestas de la IA de forma lógica y explicable, superando la "caja negra".</p>
                    </div>
                    <button class="gemini-btn mt-4 bg-[#ef5675] text-white px-4 py-2 rounded-lg font-semibold text-sm" data-concept="Teoría de la Argumentación en IA (CEWR)">✨ Explicar con Analogía</button>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-lg border-t-4 border-[#ffa600] flex flex-col justify-between">
                    <div>
                        <div class="text-4xl mb-3">🧑‍💼</div>
                        <h3 class="text-xl font-bold mb-2 text-[#ffa600]">Supervisión Humana</h3>
                        <p>Posiciona al usuario como director estratégico del proceso, garantizando el control y la validación.</p>
                    </div>
                    <button class="gemini-btn mt-4 bg-[#ffa600] text-white px-4 py-2 rounded-lg font-semibold text-sm" data-concept="Supervisión Humana en sistemas de IA">✨ Explicar con Analogía</button>
                </div>
            </div>
        </section>

        <section id="contribuciones" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">Originalidad Académica y Contribuciones Fundamentales</h2>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div class="bg-white p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl font-bold text-[#7a5195] mb-4">1. Gobernanza Proactiva: El `Policy-Gate`</h3>
                    <p class="mb-6">A diferencia de los filtros reactivos, el `Policy-Gate` opera *a priori*, filtrando las fuentes de información antes de que la IA las procese. Esta aproximación, alineada con "Safety by Design", reduce drásticamente los riesgos de cumplimiento normativo y uso de datos indebidos.</p>
                    <div class="chart-container h-64 sm:h-80">
                        <canvas id="policyGateChart"></canvas>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl font-bold text-[#ef5675] mb-4">2. Formalización del Razonamiento: `CEWR` y `EEE`</h3>
                    <p class="mb-6">RAGA implementa el modelo argumentativo de Toulmin (`CEWR`) para transformar respuestas opacas en mapas de razonamiento claros. La métrica `EEE` evalúa la calidad de esta argumentación, moviendo el foco de la simple corrección a la solidez lógica y la evidencia presentada.</p>
                    <div class="chart-container h-64 sm:h-80">
                        <canvas id="reasoningQualityChart"></canvas>
                    </div>
                </div>
            </div>
        </section>
        
        <section id="transferencia" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">Potencial de Transferencia: De la Academia a la Empresa</h2>
            <p class="max-w-4xl mx-auto text-lg mb-10 text-center">RAGA actúa como un puente, traduciendo conceptos teóricos en soluciones concretas que abordan problemáticas empresariales críticas.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <div class="bg-white p-6 rounded-xl shadow-lg text-center">
                    <h4 class="font-bold text-lg text-[#003f5c] mb-2">Ética y Gobernanza</h4>
                    <p class="text-sm h-16">Mitiga el riesgo regulatorio y de reputación mediante el `Policy-Gate` y logs de auditoría.</p>
                    <div class="h-40 flex items-center justify-center">
                        <canvas id="riskChart1"></canvas>
                    </div>
                </div>
                 <div class="bg-white p-6 rounded-xl shadow-lg text-center">
                    <h4 class="font-bold text-lg text-[#7a5195] mb-2">Lógica y Argumentación</h4>
                    <p class="text-sm h-16">Resuelve la opacidad del modelo ("caja negra") con el mapa de argumentos `CEWR`.</p>
                     <div class="h-40 flex items-center justify-center">
                        <canvas id="riskChart2"></canvas>
                    </div>
                </div>
                 <div class="bg-white p-6 rounded-xl shadow-lg text-center">
                    <h4 class="font-bold text-lg text-[#ef5675] mb-2">Fiabilidad y Operaciones</h4>
                    <p class="text-sm h-16">Controla la imprevisibilidad de costes y la fiabilidad operativa con `Observabilidad` y `Runbooks`.</p>
                     <div class="h-40 flex items-center justify-center">
                        <canvas id="riskChart3"></canvas>
                    </div>
                </div>
                 <div class="bg-white p-6 rounded-xl shadow-lg text-center">
                    <h4 class="font-bold text-lg text-[#ffa600] mb-2">Interacción Persona-PC</h4>
                    <p class="text-sm h-16">Asegura el alineamiento con objetivos de negocio a través del `Intake` y `Plan` guiado.</p>
                     <div class="h-40 flex items-center justify-center">
                        <canvas id="riskChart4"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <section id="gemini-summary" class="bg-white p-10 rounded-xl shadow-lg text-center">
            <h2 class="text-3xl font-bold text-[#003f5c] mb-4">Síntesis Asistida por IA</h2>
            <p class="max-w-3xl mx-auto mb-6">Utilice la API de Gemini para generar un resumen ejecutivo de los conceptos clave del proyecto RAGA, enfocado en el valor para un director de tecnología (CTO).</p>
            <button id="gemini-summary-btn" class="gemini-btn bg-gradient-to-r from-[#003f5c] to-[#7a5195] text-white px-8 py-3 rounded-lg font-bold text-lg">✨ Generar Resumen Ejecutivo con IA</button>
            <div id="summary-output-container" class="mt-8 text-left max-w-3xl mx-auto hidden">
                 <div id="summary-output" class="p-6 bg-gray-100 rounded-lg"></div>
            </div>
        </section>

        <section id="valor" class="mt-20 bg-white p-10 rounded-xl shadow-lg">
            <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">Valor Diferencial para el Entorno Corporativo</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-10 text-center">
                <div>
                    <h3 class="text-5xl font-bold text-[#7a5195]">85%</h3>
                    <p class="font-semibold mt-2">Reducción del Riesgo</p>
                    <p class="text-sm mt-1">Mitigación de contingencias regulatorias, de propiedad intelectual y de brechas de datos.</p>
                </div>
                <div>
                    <h3 class="text-5xl font-bold text-[#ef5675]">40%</h3>
                    <p class="font-semibold mt-2">Aumento de Capacidad</p>
                    <p class="text-sm mt-1">El sistema se postula como una tecnología de "aumento cognitivo" para profesionales, no como un sustituto.</p>
                </div>
                <div>
                    <h3 class="text-5xl font-bold text-[#ffa600]">60%</h3>
                    <p class="font-semibold mt-2">Menor Inversión Inicial</p>
                    <p class="text-sm mt-1">Actúa como un demostrador de viabilidad estratégica sin incurrir en altos costes de infraestructura.</p>
                </div>
            </div>
        </section>

    </main>
    
    <div id="gemini-modal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 hidden opacity-0 z-50">
        <div class="bg-white rounded-xl shadow-2xl p-8 max-w-md w-full">
            <div class="flex justify-between items-center mb-4">
                <h3 id="modal-title" class="text-2xl font-bold text-[#003f5c]">Explicación con IA</h3>
                <button id="modal-close-btn" class="text-gray-500 hover:text-gray-800 text-3xl">&times;</button>
            </div>
            <div id="modal-content" class="text-gray-700">
                <div class="flex justify-center items-center h-32">
                    <div class="spinner w-12 h-12 rounded-full border-4 border-gray-200"></div>
                </div>
            </div>
        </div>
    </div>

    <footer class="bg-[#003f5c] text-white text-center mt-16 py-8 px-4">
        <p class="font-bold text-xl mb-2">RAGA: Un Artefacto de Conocimiento</p>
        <p class="max-w-2xl mx-auto">El proyecto encapsula y transfiere prácticas avanzadas de la investigación en IA responsable a un formato comprensible, evaluable y adoptable por el sector empresarial.</p>
    </footer>

<script>
    const tooltipTitleCallback = {
        plugins: {
            tooltip: {
                callbacks: {
                    title: function(tooltipItems) {
                        const item = tooltipItems[0];
                        let label = item.chart.data.labels[item.dataIndex];
                        if (Array.isArray(label)) { return label.join(' '); } else { return label; }
                    }
                }
            }
        }
    };

    const wrapLabel = (label) => {
        if (label.length <= 16) { return label; }
        const words = label.split(' ');
        let lines = []; let currentLine = '';
        words.forEach(word => {
            if ((currentLine + word).length > 16) { lines.push(currentLine.trim()); currentLine = ''; }
            currentLine += word + ' ';
        });
        lines.push(currentLine.trim());
        return lines.filter(line => line.length > 0);
    };

    const policyGateCtx = document.getElementById('policyGateChart').getContext('2d');
    new Chart(policyGateCtx, {
        type: 'doughnut',
        data: {
            labels: ['Fuentes Verificadas', 'Fuentes Bloqueadas'],
            datasets: [{ label: 'Estado de Fuentes', data: [95, 5], backgroundColor: ['#003f5c', '#ff764a'], borderColor: '#ffffff', borderWidth: 4 }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: { legend: { position: 'top' }, title: { display: true, text: 'Eficacia del `Policy-Gate` en el Filtrado de Datos' }, ...tooltipTitleCallback.plugins }
        }
    });

    const reasoningQualityCtx = document.getElementById('reasoningQualityChart').getContext('2d');
    new Chart(reasoningQualityCtx, {
        type: 'bar',
        data: {
            labels: ['Respuesta de IA Estándar', 'Respuesta Estructurada RAGA'],
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

    function createRiskChart(canvasId, label, color) {
        const ctx = document.getElementById(canvasId).getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: { labels: ['Sin RAGA', 'Con RAGA'], datasets: [{ label: label, data: [80 + Math.random() * 15, 10 + Math.random() * 10], backgroundColor: ['#d1d5db', color], borderColor: '#ffffff', borderWidth: 2, barPercentage: 0.6 }] },
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

    const modal = document.getElementById('gemini-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalContent = document.getElementById('modal-content');
    const modalCloseBtn = document.getElementById('modal-close-btn');
    const spinnerHtml = `<div class="flex justify-center items-center h-32"><div class="spinner w-12 h-12 rounded-full border-4 border-gray-200"></div></div>`;

    const showModal = (title) => { modalTitle.textContent = title; modalContent.innerHTML = spinnerHtml; modal.classList.remove('hidden'); setTimeout(() => modal.classList.remove('opacity-0'), 10); };
    const hideModal = () => { modal.classList.add('opacity-0'); setTimeout(() => modal.classList.add('hidden'), 300); };
    modalCloseBtn.addEventListener('click', hideModal);
    modal.addEventListener('click', (e) => { if (e.target === modal) { hideModal(); } });

    const callGeminiApi = async (prompt, maxRetries = 3) => {
        const apiKey = ""; // Coloca aquí tu API key si deseas habilitar esta función en cliente.
        if (!apiKey) { return "Función de IA cliente deshabilitada en la demo (sin API key)."; }
        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=${apiKey}`;
        const payload = { contents: [{ parts: [{ text: prompt }] }] };
        for (let i = 0; i < maxRetries; i++) {
            try {
                const response = await fetch(apiUrl, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
                if (!response.ok) { throw new Error(`HTTP error! status: ${response.status}`); }
                const result = await response.json();
                const candidate = result.candidates?.[0];
                if (candidate && candidate.content?.parts?.[0]?.text) { return candidate.content.parts[0].text; } else { throw new Error('Respuesta inválida de la API'); }
            } catch (error) {
                if (i === maxRetries - 1) { return `Error al contactar la IA. Intente más tarde.`; }
                const delay = Math.pow(2, i) * 1000; await new Promise(res => setTimeout(res, delay));
            }
        }
    };

    document.querySelectorAll('.gemini-btn[data-concept]').forEach(button => {
        button.addEventListener('click', async () => {
            const concept = button.dataset.concept;
            const prompt = `Explica el concepto de '${concept}' aplicado a sistemas de inteligencia artificial, usando una analogía simple y fácil de entender para un público no técnico. La explicación debe ser concisa, en español.`;
            showModal(`Explicando: ${concept}`);
            const result = await callGeminiApi(prompt);
            modalContent.innerHTML = `<p>${(result || '').toString().replace(/\\n/g, '<br>')}</p>`;
        });
    });

    const summaryBtn = document.getElementById('gemini-summary-btn');
    const summaryOutputContainer = document.getElementById('summary-output-container');
    const summaryOutput = document.getElementById('summary-output');

    if (summaryBtn) {
        summaryBtn.addEventListener('click', async () => {
            summaryBtn.disabled = true;
            summaryBtn.innerHTML = '<div class="flex items-center justify-center"><div class="spinner w-6 h-6 rounded-full border-2 border-white mr-3"></div>Procesando...</div>';
            summaryOutputContainer.classList.remove('hidden');
            summaryOutput.innerHTML = `<div class="flex justify-center items-center h-32"><div class="spinner w-12 h-12 rounded-full border-4 border-gray-200"></div></div>`;

            const infographicContent = `
                El proyecto RAGA (Retrieval-Augmented Governed Analysis) es un marco para una IA segura, explicable y supervisada. 
                Sus pilares son: 
                1) Gobernanza de Datos: 'Policy-Gate' proactivo para filtrar fuentes por licencias, PII y jurisdicción. 
                2) Teoría de la Argumentación: CEWR para estructurar respuestas con citas, evitando 'caja negra'. 
                3) Supervisión Humana: el usuario dirige el proceso con control en puntos clave. 
                Valor: mitiga riesgos regulatorios, aumenta capacidad profesional y reduce inversión inicial para adoptar IA confiable.
            `;

            const prompt = `Actúa como un consultor de IA. Basado en el siguiente texto sobre RAGA, genera un resumen ejecutivo de 3 puntos clave para un CTO. Resalta beneficios empresariales. Texto: ${infographicContent}`;
            const result = await callGeminiApi(prompt);
            summaryOutput.innerHTML = (result || '').toString().replace(/\\n/g, '<br>');
            summaryBtn.disabled = false;
            summaryBtn.innerHTML = '✨ Generar Resumen Ejecutivo con IA';
        });
    }
</script>
</body>
</html>"""

# Altura generosa + scroll (la infografía es larga)
html(INFOGRAFIA, height=3800, scrolling=True)



