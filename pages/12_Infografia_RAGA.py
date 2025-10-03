<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Chosen Palette: Corporate Blue & Gold -->
    <!-- Application Structure Plan: La SPA se estructura como una narrativa descendente que guía al usuario desde los conceptos de alto nivel hasta el impacto práctico. Comienza con una síntesis de los tres pilares de RAGA, profundiza en sus contribuciones académicas con visualizaciones comparativas, traduce la teoría a problemas empresariales concretos mediante una tabla estilizada y culmina en un panel de control interactivo. Este panel permite al usuario simular el funcionamiento de RAGA, manipulando controles como el 'Policy-Gate' y el umbral de calidad 'EEE' para observar su efecto en tiempo real sobre el riesgo y la fiabilidad. Esta estructura fue elegida para transformar un informe estático en una experiencia de aprendizaje activo, donde la interacción final refuerza la comprensión de los conceptos presentados previamente. -->
    <!-- Visualization & Content Choices: 
        - Síntesis Ejecutiva -> Goal: Inform -> Viz: Tarjetas HTML con iconos Unicode -> Justification: Presentación clara y concisa de los tres pilares fundamentales.
        - Gobernanza Proactiva -> Goal: Compare -> Viz: Gráfico de Donut (Chart.js) -> Justification: Muestra visualmente la proporción de fuentes de datos seguras frente a las bloqueadas, demostrando el impacto del 'Policy-Gate'.
        - Formalización del Razonamiento -> Goal: Compare -> Viz: Gráfico de Barras Apiladas (Chart.js) -> Justification: Contrasta una respuesta opaca de IA estándar con la estructura transparente de RAGA (CEWR), explicando el valor de XAI.
        - Tabla de Transferencia -> Goal: Organize -> Viz: Disposición de Flexbox/Grid en HTML -> Justification: Moderniza la presentación de la tabla del informe, mejorando la legibilidad de la conexión entre teoría y práctica.
        - Panel Interactivo -> Goal: Relationships/Explore -> Viz: Múltiples gráficos (Barras, Donut/Gauge) y texto dinámico (JavaScript) -> Justification: Permite al usuario explorar la relación causa-efecto entre los controles de gobernanza de RAGA y los resultados empresariales (riesgo, calidad), proporcionando una prueba tangible de su valor.
    -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->

    <title>Análisis Interactivo del Proyecto RAGA</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.0.0"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .chart-container { position: relative; width: 100%; max-width: 600px; margin-left: auto; margin-right: auto; height: 300px; max-height: 400px; }
        @media (min-width: 768px) { .chart-container { height: 350px; } }
        .switch { position: relative; display: inline-block; width: 60px; height: 34px; }
        .switch input { opacity: 0; width: 0; height: 0; }
        .slider { position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: .4s; border-radius: 34px; }
        .slider:before { position: absolute; content: ""; height: 26px; width: 26px; left: 4px; bottom: 4px; background-color: white; transition: .4s; border-radius: 50%; }
        input:checked + .slider { background-color: #003f5c; }
        input:checked + .slider:before { transform: translateX(26px); }
        .gauge-text { position: absolute; top: 65%; left: 50%; transform: translate(-50%, -50%); text-align: center; }
    </style>
</head>
<body class="bg-gray-100 text-gray-800">

    <header class="bg-[#003f5c] text-white text-center py-16 px-4">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">Análisis Interactivo del Proyecto RAGA</h1>
        <p class="text-lg md:text-xl max-w-3xl mx-auto">Una exploración de la IA Gobernada, la Originalidad Académica y su Transferencia al Entorno Empresarial.</p>
    </header>

    <main class="container mx-auto px-4 sm:px-6 lg:px-8 py-12">

        <section id="pilares" class="mb-20 text-center">
            <h2 class="text-3xl font-bold text-[#003f5c] mb-4">Los Tres Pilares de RAGA</h2>
            <p class="max-w-4xl mx-auto text-lg mb-10">RAGA integra tres principios fundamentales para construir un sistema de IA robusto, fiable y auditable.</p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
                <div class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-[#7a5195]">
                    <div class="text-5xl mb-4">⚖️</div>
                    <h3 class="text-2xl font-bold mb-3 text-[#7a5195]">Gobernanza Proactiva</h3>
                    <p>Filtra fuentes de datos *antes* de que la IA las procese, asegurando el cumplimiento de licencias, PII y jurisdicción.</p>
                </div>
                <div class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-[#ef5675]">
                    <div class="text-5xl mb-4">🧩</div>
                    <h3 class="text-2xl font-bold mb-3 text-[#ef5675]">Razonamiento Explicable</h3>
                    <p>Transforma respuestas opacas en argumentos lógicos y auditables, permitiendo la validación experta del *porqué*.</p>
                </div>
                <div class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-[#ffa600]">
                    <div class="text-5xl mb-4">🧑‍💼</div>
                    <h3 class="text-2xl font-bold mb-3 text-[#ffa600]">Supervisión Humana</h3>
                    <p>Posiciona al usuario como director estratégico del proceso, donde la IA asiste y el humano valida y decide.</p>
                </div>
            </div>
        </section>
        
        <section id="contribuciones" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">Contribuciones Académicas Fundamentales</h2>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div class="bg-white p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl font-bold text-[#003f5c] mb-4">Impacto del `Policy-Gate`</h3>
                    <p class="mb-6">Esta visualización demuestra cómo el `Policy-Gate` reduce drásticamente la exposición a fuentes de datos no conformes o de riesgo, un pilar de la IA "Safety by Design".</p>
                    <div class="chart-container">
                        <canvas id="policyGateChart"></canvas>
                    </div>
                </div>
                <div class="bg-white p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl font-bold text-[#003f5c] mb-4">Mejora de la Explicabilidad</h3>
                    <p class="mb-6">Se compara una respuesta de IA estándar, opaca por naturaleza, con la salida estructurada de RAGA, que desglosa el razonamiento en componentes auditables (CEWR).</p>
                    <div class="chart-container">
                        <canvas id="reasoningQualityChart"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <section id="transferencia" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">Del Laboratorio al Mercado: Transferencia Tecnológica</h2>
             <p class="max-w-4xl mx-auto text-lg mb-10 text-center">RAGA traduce conceptos teóricos en soluciones a problemas empresariales críticos, actuando como un puente entre la investigación y la industria.</p>
            <div class="bg-white p-8 rounded-xl shadow-lg">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-x-8 gap-y-4 font-bold text-lg border-b-2 border-[#003f5c] pb-4 mb-4 text-[#003f5c]">
                    <div>Dominio Académico</div>
                    <div class="md:col-span-2">Problemática Empresarial Abordada</div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-x-8 gap-y-6">
                    <div class="font-semibold text-[#7a5195]">Ética y Gobernanza de la IA</div>
                    <div class="md:col-span-2 text-gray-700">Mitiga el riesgo regulatorio (Ley de IA) y de reputación mediante el `Policy-Gate` y logs de auditoría.</div>
                    <div class="font-semibold text-[#ef5675]">Teoría de la Argumentación</div>
                    <div class="md:col-span-2 text-gray-700">Resuelve la opacidad del modelo ("caja negra") y los déficits de confianza con el mapa de argumentos `CEWR`.</div>
                    <div class="font-semibold text-[#ffa600]">Ingeniería de Fiabilidad (SRE)</div>
                    <div class="md:col-span-2 text-gray-700">Controla la imprevisibilidad de costes y fiabilidad operativa con `Observabilidad` y `Runbooks`.</div>
                    <div class="font-semibold text-green-600">Interacción Persona-PC (HCI)</div>
                    <div class="md:col-span-2 text-gray-700">Garantiza el alineamiento con objetivos de negocio a través del flujo `Intake` y `Plan` guiado por humanos.</div>
                </div>
            </div>
        </section>
        
        <section id="dashboard" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-[#003f5c] mb-12">Panel de Control Simulado de RAGA</h2>
            <div class="bg-white p-8 rounded-xl shadow-2xl border-2 border-gray-200">
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <div class="lg:col-span-1 p-6 bg-gray-50 rounded-lg">
                        <h3 class="text-xl font-bold mb-6 text-gray-700">Controles de Gobernanza</h3>
                        <div class="mb-8">
                            <label for="policyGateToggle" class="font-semibold text-lg flex items-center justify-between">
                                <span>`Policy-Gate`</span>
                                <label class="switch">
                                    <input type="checkbox" id="policyGateToggle" checked>
                                    <span class="slider"></span>
                                </label>
                            </label>
                            <p class="text-sm text-gray-600 mt-2">Actívelo para filtrar fuentes de datos no conformes y reducir el riesgo legal.</p>
                        </div>
                        <div>
                            <label for="eeeThresholdSlider" class="font-semibold text-lg block mb-2">Umbral de Calidad (`EEE`)</label>
                            <input type="range" id="eeeThresholdSlider" min="50" max="95" value="75" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer">
                            <div class="flex justify-between text-sm text-gray-600 mt-1">
                                <span>Bajo</span>
                                <span id="eeeValue" class="font-bold text-[#003f5c]">75%</span>
                                <span>Alto</span>
                            </div>
                            <p class="text-sm text-gray-600 mt-2">Defina la calidad mínima del razonamiento para la aprobación automática del informe.</p>
                        </div>
                    </div>

                    <div class="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div class="bg-gray-50 p-6 rounded-lg">
                            <h4 class="font-bold text-lg mb-4 text-center">Nivel de Riesgo Regulatorio</h4>
                            <div class="chart-container h-48">
                                <canvas id="riskChart"></canvas>
                            </div>
                        </div>
                         <div class="bg-gray-50 p-6 rounded-lg">
                            <h4 class="font-bold text-lg mb-4 text-center">Calidad del Informe</h4>
                             <div class="chart-container h-48 relative">
                                <canvas id="qualityGauge"></canvas>
                                <div id="qualityGaugeText" class="gauge-text">
                                    <span class="text-3xl font-bold text-gray-800">88%</span>
                                    <span class="block text-sm text-gray-600">Puntuación EEE</span>
                                 </div>
                            </div>
                        </div>
                        <div class="md:col-span-2 bg-blue-50 border-l-4 border-blue-500 text-blue-800 p-6 rounded-lg">
                            <h4 class="font-bold text-lg mb-2">Estado del Sistema</h4>
                            <p id="statusText">Informe APROBADO: La calidad del razonamiento (88%) supera el umbral del 75%. El `Policy-Gate` está activo, minimizando el riesgo.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-[#003f5c] text-white text-center mt-16 py-10 px-4">
        <p class="font-bold text-xl mb-2">RAGA: Un Artefacto de Conocimiento</p>
        <p class="max-w-3xl mx-auto">Este proyecto encapsula y transfiere prácticas avanzadas de la investigación en IA responsable a un formato comprensible, evaluable y finalmente adoptable por el sector empresarial.</p>
    </footer>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        const tooltipTitleCallback = {
            plugins: {
                tooltip: {
                    callbacks: {
                        title: function(tooltipItems) {
                            const item = tooltipItems[0];
                            let label = item.chart.data.labels[item.dataIndex];
                            if (Array.isArray(label)) {
                                return label.join(' ');
                            }
                            return label;
                        }
                    }
                }
            }
        };

        const wrapLabel = (label) => {
            if (label.length <= 16) return label;
            const words = label.split(' ');
            let lines = [];
            let currentLine = '';
            words.forEach(word => {
                if ((currentLine + word).length > 16) {
                    lines.push(currentLine.trim());
                    currentLine = '';
                }
                currentLine += word + ' ';
            });
            lines.push(currentLine.trim());
            return lines.filter(line => line.length > 0);
        };

        const policyGateCtx = document.getElementById('policyGateChart').getContext('2d');
        new Chart(policyGateCtx, {
            type: 'doughnut',
            data: {
                labels: ['Fuentes Verificadas y Seguras', 'Fuentes de Riesgo Bloqueadas'],
                datasets: [{
                    data: [92, 8],
                    backgroundColor: ['#003f5c', '#ef5675'],
                    borderColor: '#ffffff',
                    borderWidth: 5,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '70%',
                plugins: {
                    legend: { position: 'bottom' },
                    title: { display: false },
                    ...tooltipTitleCallback.plugins
                }
            }
        });

        const reasoningQualityCtx = document.getElementById('reasoningQualityChart').getContext('2d');
        new Chart(reasoningQualityCtx, {
            type: 'bar',
            data: {
                labels: [wrapLabel('Respuesta de IA Estándar'), wrapLabel('Respuesta Estructurada RAGA')],
                datasets: [
                    { label: 'Opacidad ("Caja Negra")', data: [100, 0], backgroundColor: '#ff6361' },
                    { label: 'Aserción (Claim)', data: [0, 25], backgroundColor: '#003f5c' },
                    { label: 'Evidencia', data: [0, 45], backgroundColor: '#7a5195' },
                    { label: 'Garantía (Warrant)', data: [0, 30], backgroundColor: '#ffa600' },
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                scales: {
                    x: { stacked: true, ticks: { callback: value => value + '%' } },
                    y: { stacked: true }
                },
                plugins: {
                    title: { display: false },
                    ...tooltipTitleCallback.plugins
                }
            }
        });

        const policyGateToggle = document.getElementById('policyGateToggle');
        const eeeThresholdSlider = document.getElementById('eeeThresholdSlider');
        const eeeValue = document.getElementById('eeeValue');
        const statusText = document.getElementById('statusText');
        const riskChartCanvas = document.getElementById('riskChart').getContext('2d');
        const qualityGaugeCanvas = document.getElementById('qualityGauge').getContext('2d');
        const qualityGaugeText = document.getElementById('qualityGaugeText').querySelector('span');

        let riskChart = new Chart(riskChartCanvas, {
            type: 'bar',
            data: {
                labels: ['Riesgo'],
                datasets: [{
                    label: 'Riesgo Regulatorio',
                    data: [15],
                    backgroundColor: ['#7a5195'],
                    borderRadius: 5,
                    barPercentage: 0.5,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                scales: {
                    x: { beginAtZero: true, max: 100, ticks: { callback: val => val + '%' } },
                    y: { display: false }
                },
                plugins: {
                    legend: { display: false },
                    ...tooltipTitleCallback.plugins
                }
            }
        });

        const simulatedQualityScore = 88;
        let qualityGauge = new Chart(qualityGaugeCanvas, {
            type: 'doughnut',
            data: {
                labels: ['Puntuación de Calidad', 'Restante'],
                datasets: [{
                    data: [simulatedQualityScore, 100 - simulatedQualityScore],
                    backgroundColor: ['#003f5c', '#e0e0e0'],
                    borderColor: '#ffffff',
                    borderWidth: 2,
                    circumference: 180,
                    rotation: 270,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '75%',
                plugins: {
                    legend: { display: false },
                    tooltip: { enabled: false }
                }
            }
        });
        
        function updateDashboard() {
            const isPolicyGateActive = policyGateToggle.checked;
            const eeeThreshold = parseInt(eeeThresholdSlider.value, 10);
            
            const riskLevel = isPolicyGateActive ? 15 : 85;
            riskChart.data.datasets[0].data[0] = riskLevel;
            riskChart.data.datasets[0].backgroundColor[0] = isPolicyGateActive ? '#7a5195' : '#ef5675';
            riskChart.update();

            eeeValue.textContent = `${eeeThreshold}%`;
            qualityGaugeText.textContent = `${simulatedQualityScore}%`;
            
            const passesThreshold = simulatedQualityScore >= eeeThreshold;
            const statusContainer = statusText.parentElement;
            
            let message = '';
            if (passesThreshold) {
                message = `Informe APROBADO: La calidad (${simulatedQualityScore}%) supera el umbral del ${eeeThreshold}%.`;
                statusContainer.className = 'md:col-span-2 bg-green-50 border-l-4 border-green-500 text-green-800 p-6 rounded-lg';
            } else {
                message = `ALERTA: REVISIÓN HUMANA REQUERIDA. La calidad (${simulatedQualityScore}%) está por debajo del umbral del ${eeeThreshold}%.`;
                statusContainer.className = 'md:col-span-2 bg-red-50 border-l-4 border-red-500 text-red-800 p-6 rounded-lg';
            }

            if (isPolicyGateActive) {
                message += ' El `Policy-Gate` está activo, minimizando el riesgo.';
            } else {
                message += ' ADVERTENCIA: El `Policy-Gate` está inactivo, aumentando el riesgo.';
            }

            statusText.textContent = message;
        }

        policyGateToggle.addEventListener('change', updateDashboard);
        eeeThresholdSlider.addEventListener('input', updateDashboard);
        
        updateDashboard();
    });
</script>

</body>
</html>


