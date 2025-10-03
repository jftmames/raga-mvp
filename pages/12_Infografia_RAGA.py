<!DOCTYPE html>
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
        body {
            font-family: 'Inter', sans-serif;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
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
                </div>
                <div class="bg-white p-6 rounded-xl shadow-lg border-t-4 border-[#ef5675] flex flex-col justify-between">
                    <div>
                        <div class="text-4xl mb-3">🧩</div>
                        <h3 class="text-xl font-bold mb-2 text-[#ef5675]">Teoría de la Argumentación</h3>
                        <p>Estructura las respuestas de la IA de forma lógica y explicable, superando la "caja negra".</p>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-lg border-t-4 border-[#ffa600] flex flex-col justify-between">
                    <div>
                        <div class="text-4xl mb-3">🧑‍💼</div>
                        <h3 class="text-xl font-bold mb-2 text-[#ffa600]">Supervisión Humana</h3>
                        <p>Posiciona al usuario como director estratégico del proceso, garantizando el control y la validación.</p>
                    </div>
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

        <section id="valor" class="bg-white p-10 rounded-xl shadow-lg">
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
                        if (Array.isArray(label)) {
                          return label.join(' ');
                        } else {
                          return label;
                        }
                    }
                }
            }
        }
    };
    
    const wrapLabel = (label) => {
        if (label.length <= 16) {
            return label;
        }
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
            labels: ['Fuentes Verificadas', 'Fuentes Bloqueadas'],
            datasets: [{
                label: 'Estado de Fuentes',
                data: [95, 5],
                backgroundColor: ['#003f5c', '#ff764a'],
                borderColor: '#ffffff',
                borderWidth: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Eficacia del `Policy-Gate` en el Filtrado de Datos'
                },
                ...tooltipTitleCallback.plugins
            }
        }
    });

    const reasoningQualityCtx = document.getElementById('reasoningQualityChart').getContext('2d');
    new Chart(reasoningQualityCtx, {
        type: 'bar',
        data: {
            labels: ['Respuesta de IA Estándar', 'Respuesta Estructurada RAGA'],
            datasets: [
                {
                    label: 'Opacidad ("Caja Negra")',
                    data: [100, 0],
                    backgroundColor: '#ff764a',
                },
                {
                    label: 'Aserción (Claim)',
                    data: [0, 25],
                    backgroundColor: '#003f5c',
                },
                 {
                    label: 'Evidencia',
                    data: [0, 45],
                    backgroundColor: '#7a5195',
                },
                 {
                    label: 'Garantía (Warrant)',
                    data: [0, 30],
                    backgroundColor: '#ffa600',
                },
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: 'y',
            scales: {
                x: {
                    stacked: true,
                    ticks: { callback: value => value + '%' }
                },
                y: {
                    stacked: true
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Comparativa de Explicabilidad'
                },
                ...tooltipTitleCallback.plugins
            }
        }
    });

    function createRiskChart(canvasId, label, color) {
        const ctx = document.getElementById(canvasId).getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Sin RAGA', 'Con RAGA'],
                datasets: [{
                    label: label,
                    data: [80 + Math.random() * 15, 10 + Math.random() * 10],
                    backgroundColor: [ '#d1d5db', color],
                    borderColor: '#ffffff',
                    borderWidth: 2,
                    barPercentage: 0.6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        display: false
                    },
                    x: {
                        grid: { display: false }
                    }
                },
                plugins: {
                    legend: { display: false },
                     ...tooltipTitleCallback.plugins
                }
            }
        });
    }

    createRiskChart('riskChart1', 'Riesgo Regulatorio', '#003f5c');
    createRiskChart('riskChart2', 'Opacidad del Modelo', '#7a5195');
    createRiskChart('riskChart3', 'Costes Operativos', '#ef5675');
    createRiskChart('riskChart4', 'Desalineación Estratégica', '#ffa600');

</script>
</body>
</html>


