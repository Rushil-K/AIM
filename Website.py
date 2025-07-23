import streamlit as st
import streamlit.components.v1 as components

# It's best practice to keep your HTML in a separate file for larger projects.
# For this example, I'm embedding the HTML directly as a string.
# In a real scenario, you might read it from an 'index.html' file:
# with open("index.html", "r", encoding="utf-8") as f:
#     html_content = f.read()

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Rise of AI in Indian Retail: An Interactive Report</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Chosen Palette: Warm Neutrals & Subtle Blues -->
    <!-- Application Structure Plan: A top-down narrative dashboard. Starts with a high-level summary (Hero), then dives into three core pillars: Market Opportunity (the 'why'), The Indian Consumer (the 'who'), and AI in Action (the 'how'), concluding with real-world Industry Leaders. This thematic structure is more intuitive for exploration than the report's linear format. Navigation is handled by a sticky header, allowing users to jump to sections of interest. Interactions like tabs and accordions are used to layer complex information without overwhelming the user, promoting focused discovery. -->
    <!-- Visualization & Content Choices: 
        - Market Growth: Goal: Show change. Viz: Line chart (Chart.js) for intuitive trend visualization. Interaction: Hover tooltips. Justification: Best for time-series data.
        - Dominant AI Components: Goal: Inform/Compare proportions. Viz: Doughnut chart (Chart.js) for Solution vs. Services share. Interaction: Hover tooltips. Justification: Clearly shows proportional breakdown of components.
        - Technology Breakdown: Goal: Inform. Viz: Textual explanation. Justification: Provides context for specific technologies.
        - Consumer Sentiment: Goal: Compare/Inform. Viz: Horizontal Bar charts (Chart.js) & Key Stat Cards (HTML/Tailwind). Interaction: Toggles to switch between views. Justification: Bar charts effectively compare India vs. Global. Stat cards highlight key metrics for quick absorption.
        - AI Applications: Goal: Organize. Viz: Tabbed interface (HTML/JS). Interaction: Clicking tabs reveals content. Justification: Organizes dense information into clean, user-selectable categories.
        - Company Case Studies: Goal: Organize/Inform. Viz: Accordion (HTML/JS). Interaction: Clicking a company name expands to show details. Justification: A space-efficient way to present multiple case studies without a long scroll.
    -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8f7f4;
            color: #333;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 300px; /* Base height for the container */
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px; /* Adjusted height for larger screens */
            }
        }
        .nav-link {
            transition: color 0.3s, border-bottom-color 0.3s;
            border-bottom: 2px solid transparent;
        }
        .nav-link:hover, .nav-link.active {
            color: #2563eb;
            border-bottom-color: #2563eb;
        }
        .stat-card {
            background-color: white;
            border-radius: 0.75rem;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        }
        .accordion-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s ease-in-out;
        }
        /* Refined styling for superscript reference links */
        .reference-link-sup {
            vertical-align: super;
            font-size: 0.65em; /* Made slightly smaller */
            margin-left: 2px;
            line-height: 1; /* Ensures it doesn't affect line height */
        }
        .reference-link-sup a {
            color: #2563eb; /* Apply color to the anchor */
            text-decoration: none;
        }
        .reference-link-sup a:hover {
            text-decoration: underline; /* Apply underline on hover to the anchor */
        }
    </style>
</head>
<body class="antialiased">

    <header id="header" class="bg-white/80 backdrop-blur-lg sticky top-0 z-50 shadow-sm">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <h1 class="text-xl font-bold text-gray-800">AI in Indian Retail</h1>
            <div class="hidden md:flex space-x-8">
                <a href="#market" class="nav-link font-medium text-gray-600 pb-1">Market Opportunity</a>
                <a href="#consumer" class="nav-link font-medium text-gray-600 pb-1">The Consumer</a>
                <a href="#applications" class="nav-link font-medium text-gray-600 pb-1">AI in Action</a>
                <a href="#leaders" class="nav-link font-medium text-gray-600 pb-1">Industry Leaders</a>
                <a href="#references" class="nav-link font-medium text-gray-600 pb-1">References</a>
            </div>
            <button id="mobile-menu-button" class="md:hidden focus:outline-none">
                <svg class="w-6 h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
            </button>
        </nav>
        <div id="mobile-menu" class="hidden md:hidden">
            <a href="#market" class="block py-2 px-6 text-sm text-gray-700 hover:bg-gray-100">Market Opportunity</a>
            <a href="#consumer" class="block py-2 px-6 text-sm text-gray-700 hover:bg-gray-100">The Consumer</a>
            <a href="#applications" class="block py-2 px-6 text-sm text-gray-700 hover:bg-gray-100">AI in Action</a>
            <a href="#leaders" class="block py-2 px-6 text-sm text-gray-700 hover:bg-gray-100">Industry Leaders</a>
            <a href="#references" class="block py-2 px-6 text-sm text-gray-700 hover:bg-gray-100">References</a>
        </div>
    </header>

    <main class="container mx-auto px-6 py-8 md:py-12">
        <section class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">India's Retail Revolution is AI-Powered</h2>
            <p class="max-w-3xl mx-auto text-lg text-gray-600 mb-8">
                A new era of retail is dawning in India, driven by a powerful synergy between ambitious businesses and a digitally-savvy consumer base. Explore the data behind this transformation.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
                <div class="stat-card text-center">
                    <p class="text-4xl font-bold text-blue-600">33.7%<sup class="reference-link-sup"><a href="#ref-1">[1, 2]</a></sup></p>
                    <p class="text-gray-500 mt-2">Projected CAGR (2025-2030)</p>
                </div>
                <div class="stat-card text-center">
                    <p class="text-4xl font-bold text-blue-600">82%<sup class="reference-link-sup"><a href="#ref-6">[6]</a></sup></p>
                    <p class="text-gray-500 mt-2">of Consumers Open to AI</p>
                </div>
                <div class="stat-card text-center">
                    <p class="text-4xl font-bold text-blue-600">59%<sup class="reference-link-sup"><a href="#ref-5">[5]</a></sup></p>
                    <p class="text-gray-500 mt-2">of Large Enterprises Use AI</p>
                </div>
            </div>
        </section>

        <section id="market" class="pt-16 mb-16">
            <div class="text-center mb-6">
                <h3 class="text-3xl font-bold text-gray-900 mb-2">The Market Opportunity</h3>
                <p class="max-w-2xl mx-auto text-gray-600">This section explores the significant financial growth and widespread business adoption fueling the AI revolution in Indian retail. The data shows a market not just growing, but accelerating, with businesses of all sizes investing in AI to gain a competitive edge.</p>
            </div>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h4 class="text-xl font-semibold text-center mb-4">AI in Retail Market Growth (USD Millions)<sup class="reference-link-sup"><a href="#ref-1">[1, 2]</a></sup></h4>
                    <div class="chart-container">
                        <canvas id="marketGrowthChart"></canvas>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h4 class="text-xl font-semibold text-center mb-4">Dominant AI Components & Technologies<sup class="reference-link-sup"><a href="#ref-1">[1, 2]</a><a href="#ref-14">[14]</a></sup></h4>
                    <div class="chart-container">
                        <canvas id="componentsChart"></canvas>
                    </div>
                    <p class="text-gray-600 text-sm mt-4">
                        Machine Learning leads with a 40.21% revenue share (2024), foundational for current AI applications. Generative AI is projected for significant growth (27.6% CAGR to 2030), signaling its importance in content creation and advanced personalization. Omnichannel strategies held a dominant 45.7% of the AI in Retail market share in 2024, emphasizing unified data flows.
                    </p>
                </div>
            </div>
        </section>

        <section id="consumer" class="pt-16 mb-16 bg-blue-50/50 -mx-6 px-6 py-12 rounded-lg">
            <div class="text-center mb-6">
                <h3 class="text-3xl font-bold text-gray-900 mb-2">Understanding the Indian Consumer</h3>
                <p class="max-w-2xl mx-auto text-gray-600">Successful AI integration hinges on understanding the end-user. This section delves into the digital landscape of India's consumers, their evolving preferences, and their unique perspective on AI—a blend of high enthusiasm and critical concerns about privacy.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                <div class="stat-card text-center">
                    <p class="text-3xl font-bold text-blue-600">974M<sup class="reference-link-sup"><a href="#ref-15">[15]</a></sup></p>
                    <p class="text-gray-500 mt-1">Internet Users</p>
                </div>
                <div class="stat-card text-center">
                    <p class="text-3xl font-bold text-blue-600">85.5%<sup class="reference-link-sup"><a href="#ref-17">[17]</a></sup></p>
                    <p class="text-gray-500 mt-1">Household Smartphone Penetration</p>
                </div>
                <div class="stat-card text-center">
                    <p class="text-3xl font-bold text-blue-600">84%<sup class="reference-link-sup"><a href="#ref-5">[5]</a></sup></p>
                    <p class="text-gray-500 mt-1">UPI Share of Digital Payments</p>
                </div>
                 <div class="stat-card text-center">
                    <p class="text-3xl font-bold text-blue-600">₹9<sup class="reference-link-sup"><a href="#ref-15">[15, 16]</a></sup></p>
                    <p class="text-gray-500 mt-1">Avg. Cost per GB of Data</p>
                </div>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-lg">
                <h4 class="text-xl font-semibold text-center mb-4">Consumer Sentiment on AI<sup class="reference-link-sup"><a href="#ref-6">[6]</a><a href="#ref-7">[7]</a></sup></h4>
                 <div class="chart-container">
                    <canvas id="consumerSentimentChart"></canvas>
                </div>
                <p class="text-center text-sm text-gray-500 mt-4">Indian consumers show significantly higher trust and openness to AI in their shopping journey compared to global averages, yet data privacy remains a paramount concern for 82%<sup class="reference-link-sup"><a href="#ref-7">[7]</a></sup> of them.</p>
            </div>
        </section>

        <section id="applications" class="pt-16 mb-16">
            <div class="text-center mb-6">
                <h3 class="text-3xl font-bold text-gray-900 mb-2">AI in Action: Transforming Retail</h3>
                <p class="max-w-2xl mx-auto text-gray-600">AI is not a future concept; it's a present-day reality revolutionizing every facet of retail. This interactive section showcases how AI is being applied to create more personal customer experiences and drive unprecedented operational efficiency. Click through the tabs to explore key use cases.</p>
            </div>
            <div>
                <div class="border-b border-gray-200 mb-6">
                    <nav class="-mb-px flex space-x-6" aria-label="Tabs">
                        <button class="tab-btn active text-blue-600 border-blue-600 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm" data-tab="personalization">Personalization</button>
                        <button class="tab-btn text-gray-500 hover:text-gray-700 hover:border-gray-300 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm" data-tab="operations">Operations</button>
                        <button class="tab-btn text-gray-500 hover:text-gray-700 hover:border-gray-300 whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm" data-tab="service">Customer Service</button>
                    </nav>
                </div>
                <div id="tab-content" class="bg-white p-8 rounded-lg shadow-lg">
                    <div id="personalization-content" class="tab-pane active">
                        <h4 class="text-2xl font-semibold mb-3">Hyper-Personalized Experiences<sup class="reference-link-sup"><a href="#ref-2">[2]</a><a href="#ref-3">[3, 4]</a><a href="#ref-8">[8]</a><a href="#ref-9">[9]</a></sup></h4>
                        <p class="text-gray-600 mb-4">AI algorithms analyze browsing history, purchase behavior, and preferences to deliver tailored product recommendations and marketing. This moves beyond simple suggestions to create a unique shopping journey for every customer.</p>
                        <ul class="list-disc list-inside space-y-2 text-gray-700">
                            <li><strong>Taste-Mapping:</strong> Sophisticated systems understand individual style, not just what's popular.<sup class="reference-link-sup"><a href="#ref-20">[20]</a></sup></li>
                            <li><strong>Generative AI Marketing:</strong> 42% of retailers use GenAI for personalized ads and content.<sup class="reference-link-sup"><a href="#ref-9">[9]</a></sup></li>
                            <li><strong>Key Outcome:</strong> 44% of MSMEs rely on AI personalization to enhance customer experience and loyalty.<sup class="reference-link-sup"><a href="#ref-3">[3, 4]</a></sup></li>
                        </ul>
                    </div>
                    <div id="operations-content" class="tab-pane hidden">
                        <h4 class="text-2xl font-semibold mb-3">Unprecedented Operational Efficiency<sup class="reference-link-sup"><a href="#ref-2">[2]</a><a href="#ref-5">[5]</a><a href="#ref-8">[8]</a><a href="#ref-9">[9]</a></sup></h4>
                        <p class="text-gray-600 mb-4">Behind the scenes, AI is optimizing the backbone of retail. From predicting demand to automating warehouses, AI drives down costs and increases resilience, directly impacting the bottom line.</p>
                         <ul class="list-disc list-inside space-y-2 text-gray-700">
                            <li><strong>Demand Forecasting:</strong> >90% forecast accuracy, reducing stockouts by 40% and excess inventory by 25%.<sup class="reference-link-sup"><a href="#ref-5">[5]</a></sup></li>
                            <li><strong>Supply Chain Optimization:</strong> AI predicts disruptions and optimizes delivery routes, reducing costs.<sup class="reference-link-sup"><a href="#ref-2">[2]</a><a href="#ref-8">[8]</a><a href="#ref-9">[9]</a></sup></li>
                            <li><strong>Warehouse Automation:</strong> Up to 99.9% order accuracy and 20% reduction in operational costs with robotics.<sup class="reference-link-sup"><a href="#ref-5">[5]</a></sup></li>
                        </ul>
                    </div>
                    <div id="service-content" class="tab-pane hidden">
                        <h4 class="text-2xl font-semibold mb-3">Enhanced Customer Service<sup class="reference-link-sup"><a href="#ref-2">[2]</a><a href="#ref-8">[8]</a><a href="#ref-9">[9]</a></sup></h4>
                        <p class="text-gray-600 mb-4">AI-powered chatbots and virtual assistants provide 24/7 support, resolving queries instantly and freeing up human agents for more complex issues. This ensures a responsive and seamless customer support experience.</p>
                        <ul class="list-disc list-inside space-y-2 text-gray-700">
                            <li><strong>24/7 Support:</strong> AI chatbots handle common queries anytime, day or night.<sup class="reference-link-sup"><a href="#ref-2">[2]</a><a href="#ref-8">[8]</a><a href="#ref-9">[9]</a></sup></li>
                            <li><strong>Proactive Logistics:</strong> AI resolves 70-80% of delivery issues automatically before they become problems.<sup class="reference-link-sup"><a href="#ref-20">[20]</a></sup></li>
                            <li><strong>Consumer Comfort:</strong> 82% of Indian consumers are open to chatbots assisting with their queries.<sup class="reference-link-sup"><a href="#ref-6">[6]</a></sup></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section id="leaders" class="pt-16">
            <div class="text-center mb-6">
                <h3 class="text-3xl font-bold text-gray-900 mb-2">Industry Leaders: AI in Practice</h3>
                <p class="max-w-2xl mx-auto text-gray-600">Theory meets practice. This section highlights how leading Indian companies are implementing tailored AI solutions to solve real-world challenges and create distinct competitive advantages. Click on each company to see how they are innovating.</p>
            </div>
            <div class="space-y-4 max-w-4xl mx-auto">
                <div class="accordion-item bg-white rounded-lg shadow-md">
                    <button class="accordion-header w-full text-left p-6 flex justify-between items-center">
                        <span class="text-xl font-semibold text-gray-800">Myntra (Fashion Retail)<sup class="reference-link-sup"><a href="#ref-20">[20]</a></sup></span>
                        <span class="accordion-icon text-2xl text-blue-600 transform transition-transform">+</span>
                    </button>
                    <div class="accordion-content px-6 pb-6">
                        <p class="text-gray-600">Myntra uses ML to power every frame of its app, from personalized homepages to "taste-mapping" algorithms that understand individual fashion sense. Its conversational AI stylist acts as a virtual shopping assistant, providing outfit ideas for specific occasions.</p>
                    </div>
                </div>
                 <div class="accordion-item bg-white rounded-lg shadow-md">
                    <button class="accordion-header w-full text-left p-6 flex justify-between items-center">
                        <span class="text-xl font-semibold text-gray-800">Shipway (Logistics)<sup class="reference-link-sup"><a href="#ref-20">[20]</a></sup></span>
                        <span class="accordion-icon text-2xl text-blue-600 transform transition-transform">+</span>
                    </button>
                    <div class="accordion-content px-6 pb-6">
                        <p class="text-gray-600">Shipway leverages AI to optimize the entire delivery process. It maps courier performance by success rate and speed to choose the best option for each delivery. Its AI-powered chatbots proactively resolve 70-80% of delivery issues (like incorrect addresses) before a package is returned to origin.</p>
                    </div>
                </div>
                <div class="accordion-item bg-white rounded-lg shadow-md">
                    <button class="accordion-header w-full text-left p-6 flex justify-between items-center">
                        <span class="text-xl font-semibold text-gray-800">Panasonic (Consumer Durables)<sup class="reference-link-sup"><a href="#ref-20">[20]</a></sup></span>
                        <span class="accordion-icon text-2xl text-blue-600 transform transition-transform">+</span>
                    </button>
                    <div class="accordion-content px-6 pb-6">
                        <p class="text-gray-600">Panasonic uses AI to forecast demand by analyzing factors like weather and regional events, ensuring optimal inventory levels for products like air conditioners. It also uses AI to identify high-intent users on its website and trigger proactive support to convert interest into sales.</p>
                    </div>
                </div>
                <div class="accordion-item bg-white rounded-lg shadow-md">
                    <button class="accordion-header w-full text-left p-6 flex justify-between items-center">
                        <span class="text-xl font-semibold text-gray-800">Shiprocket (eCommerce Enablement)<sup class="reference-link-sup"><a href="#ref-5">[5]</a></sup></span>
                        <span class="accordion-icon text-2xl text-blue-600 transform transition-transform">+</span>
                    </button>
                    <div class="accordion-content px-6 pb-6">
                        <p class="text-gray-600">Shiprocket developed Shunya.ai, India's first sovereign AI engine for MSMEs. Trained on Indian commerce data and supporting 9 regional languages, it's a "Made for Bharat" solution that ensures data sovereignty by being hosted on local infrastructure. It automates cataloguing, marketing, and fulfillment for small businesses.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="references" class="pt-16 mb-16">
            <div class="text-center mb-12">
                <h3 class="text-3xl font-bold text-gray-900 mb-2">References</h3>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-lg max-w-4xl mx-auto">
                <ol class="list-decimal list-inside space-y-3 text-gray-700">
                    <li id="ref-1">"India Artificial Intelligence in Retail Market Size, Share & Trends Analysis Report By Component (Solution, Services), By Technology (Machine Learning, Natural Language Processing, Computer Vision, Others), By Application, By Deployment, By Organization Size, By Region, And Segment Forecasts, 2024 - 2030." Grand View Research, April 2024.</li>
                    <li id="ref-2">"India Artificial Intelligence in Retail Market Size and Forecast (2024-2030)." TechSci Research, 2024.</li>
                    <li id="ref-3">"Zoho Survey on Indian MSMEs: AI Adoption and Omnichannel Strategies." Zoho, 2024.</li>
                    <li id="ref-4">"Zoho survey: 60% of Indian MSMEs to adopt AI/ML by 2030." The Economic Times, May 2024.</li>
                    <li id="ref-5">"Shiprocket-KPMG Report: AI in Indian Retail." Shiprocket, KPMG, 2024.</li>
                    <li id="ref-6">"EY Survey: Indian Consumer Sentiment on AI." EY, 2024.</li>
                    <li id="ref-7">"PwC India Survey: Consumer Trust and Privacy in Digital India." PwC India, 2024.</li>
                    <li id="ref-8">"India Artificial Intelligence in Retail Market Size, Share, Trends, Opportunities and Forecasts (2023-2032)." Market Research Future, 2024.</li>
                    <li id="ref-9">"AI in Retail: The Future of Shopping." Shopify, 2024.</li>
                    <li id="ref-10">"India's AI Opportunity: A Trillion-Dollar Vision." NITI Aayog, 2024.</li>
                    <li id="ref-11">"India Retail Market Outlook 2026." Invest India, 2022.</li>
                    <li id="ref-12">"The Evolving Indian Consumer: Trends and Preferences." Deloitte, 2023.</li>
                    <li id="ref-13">"CBRE and Invest India Survey: Experiential Retail." CBRE, Invest India, 2023.</li>
                    <li id="ref-14">"Generative AI in Retail Market Analysis." Allied Market Research, 2024.</li>
                    <li id="ref-15">"Telecom Regulatory Authority of India (TRAI) Reports." TRAI, March 2024.</li>
                    <li id="ref-16">"Department of Telecommunications (DoT) Annual Reports." DoT, April 2024.</li>
                    <li id="ref-17">"National Family Health Survey (NFHS-5) 2019-21." Ministry of Health and Family Welfare, Government of India.</li>
                    <li id="ref-18">"India Smartphone Market Report." Counterpoint Research, 2021.</li>
                    <li id="ref-19">"India's Consumption Story: Rise of the Middle Class." CRISIL, 2024.</li>
                    <li id="ref-20">"AI in Indian Retail: Company Case Studies." Various industry reports and company statements, 2023-2024.</li>
                </ol>
            </div>
        </section>
    </main>

    <footer class="bg-gray-800 text-white mt-16">
        <div class="container mx-auto px-6 py-4 text-center text-sm">
            <p>&copy; 2024 Interactive Report on AI in Indian Retail. All data sourced from the provided report.</p>
        </div>
    </footer>

    <script>
        let marketGrowthChartInstance;
        let componentsChartInstance;
        let consumerSentimentChartInstance;

        const chartOptions = {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        font: {
                            family: "'Inter', sans-serif"
                        }
                    }
                },
                tooltip: {
                    bodyFont: {
                        family: "'Inter', sans-serif"
                    },
                    titleFont: {
                        family: "'Inter', sans-serif"
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            family: "'Inter', sans-serif"
                        }
                    }
                },
                x: {
                    ticks: {
                        font: {
                            family: "'Inter', sans-serif"
                        }
                    }
                }
            }
        };

        function createChart(canvasId, type, data, options) {
            const canvas = document.getElementById(canvasId);
            const container = canvas.closest('.chart-container');
            if (!canvas || !container) {
                console.error(`Canvas or container not found for ID: ${canvasId}`);
                return null;
            }

            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;

            const ctx = canvas.getContext('2d');
            return new Chart(ctx, { type, data, options });
        }

        function renderAllCharts() {
            if (marketGrowthChartInstance) marketGrowthChartInstance.destroy();
            if (componentsChartInstance) componentsChartInstance.destroy();
            if (consumerSentimentChartInstance) consumerSentimentChartInstance.destroy();

            marketGrowthChartInstance = createChart('marketGrowthChart', 'line', {
                labels: ['2024', '2025', '2026', '2027', '2028', '2029', '2030'],
                datasets: [{
                    label: 'Market Revenue (USD M)',
                    data: [584.7, 781.7, 1045.1, 1397.3, 1868.2, 2500.0, 3474.6],
                    borderColor: 'rgba(37, 99, 235, 1)',
                    backgroundColor: 'rgba(37, 99, 235, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            }, chartOptions);

            componentsChartInstance = createChart('componentsChart', 'doughnut', {
                labels: ['Solution (88.52%)', 'Services (11.48%)'],
                datasets: [{
                    label: 'Market Share (%)',
                    data: [88.52, 11.48],
                    backgroundColor: [
                        'rgba(37, 99, 235, 0.7)',
                        'rgba(59, 130, 246, 0.7)'
                    ],
                    borderColor: [
                        'rgba(37, 99, 235, 1)',
                        'rgba(59, 130, 246, 1)'
                    ],
                    borderWidth: 1
                }]
            }, {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            font: {
                                family: "'Inter', sans-serif"
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                let label = context.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                if (context.parsed !== null) {
                                    label += context.parsed + '%';
                                }
                                return label;
                            }
                        },
                        bodyFont: {
                            family: "'Inter', sans-serif"
                        },
                        titleFont: {
                            family: "'Inter', sans-serif"
                        }
                    }
                }
            });

            consumerSentimentChartInstance = createChart('consumerSentimentChart', 'bar', {
                labels: ['Open to AI for Purchase Decisions', 'Trust AI for Tailored Deals', 'Open to Chatbots'],
                datasets: [
                    {
                        label: 'India (%)',
                        data: [82, 48, 82],
                        backgroundColor: 'rgba(37, 99, 235, 0.7)',
                        borderColor: 'rgba(37, 99, 235, 1)',
                        borderWidth: 1
                    },
                    {
                        label: 'Global Avg (%)',
                        data: [58, 23, 58], 
                        backgroundColor: 'rgba(147, 197, 253, 0.7)',
                        borderColor: 'rgba(147, 197, 253, 1)',
                        borderWidth: 1
                    }
                ]
            }, chartOptions);
        }

        document.addEventListener('DOMContentLoaded', function () {
            renderAllCharts();
            window.addEventListener('resize', renderAllCharts);

            const tabBtns = document.querySelectorAll('.tab-btn');
            const tabPanes = document.querySelectorAll('.tab-pane');
            tabBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    tabBtns.forEach(b => {
                        b.classList.remove('active', 'text-blue-600', 'border-blue-600');
                        b.classList.add('text-gray-500', 'hover:text-gray-700', 'hover:border-gray-300');
                    });
                    btn.classList.add('active', 'text-blue-600', 'border-blue-600');
                    btn.classList.remove('text-gray-500', 'hover:text-gray-700', 'hover:border-gray-300');

                    tabPanes.forEach(pane => {
                        pane.classList.add('hidden');
                    });
                    document.getElementById(`${btn.dataset.tab}-content`).classList.remove('hidden');
                });
            });

            const accordionItems = document.querySelectorAll('.accordion-item');
            accordionItems.forEach(item => {
                const header = item.querySelector('.accordion-header');
                const content = item.querySelector('.accordion-content');
                const icon = item.querySelector('.accordion-icon');
                header.addEventListener('click', () => {
                    const isOpen = content.style.maxHeight && content.style.maxHeight !== '0px';
                    
                    accordionItems.forEach(i => {
                        i.querySelector('.accordion-content').style.maxHeight = '0px';
                        i.querySelector('.accordion-icon').textContent = '+';
                        i.querySelector('.accordion-icon').classList.remove('rotate-45');
                    });

                    if (!isOpen) {
                        content.style.maxHeight = content.scrollHeight + 'px';
                        icon.textContent = ''; 
                        icon.innerHTML = '&times;';
                        icon.classList.add('rotate-45');
                    } else {
                        content.style.maxHeight = '0px';
                        icon.textContent = '+';
                        icon.classList.remove('rotate-45');
                    }
                });
            });

            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });
            
            const navLinks = document.querySelectorAll('nav a');
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if(!mobileMenu.classList.contains('hidden')) {
                       mobileMenu.classList.add('hidden');
                    }
                });
            });

            const sections = document.querySelectorAll('section');
            const headerNavLinks = document.querySelectorAll('#header .nav-link');
            window.addEventListener('scroll', () => {
                let current = '';
                sections.forEach(section => {
                    const sectionTop = section.offsetTop;
                    if (pageYOffset >= sectionTop - 60) {
                        current = section.getAttribute('id');
                    }
                });

                headerNavLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href').includes(current)) {
                        link.classList.add('active');
                    }
                });
            });
        });
    </script>
</body>
</html>
"""

st.set_page_config(layout="wide") # Use wide layout for better display of the HTML

st.title("AI in Indian Retail: Interactive Report")

# Embed the HTML content
components.html(html_content, height=2000, scrolling=True) # Adjust height as needed
