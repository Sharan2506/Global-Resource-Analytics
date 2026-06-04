# Global-Resource-Analytics
Interactive dark-themed analytics dashboard built with Streamlit and Plotly tracking global energy mixes, forest cover trends, mineral metrics (log scale), and freshwater extraction.
Built entirely in Python using **Streamlit** and **Plotly**, this web application integrates custom responsive CSS styles and stateful event triggers to enable fluid, interactive data storytelling.

## Architectural & Engineering Features

* **Dynamic Deep-Dive Panels:** Utilizes Streamlit reactive state controls. When selecting specific countries, materials, or continents, the dashboard dynamically updates a custom-styled sidebar with contextual resource facts and localized insights.
* **Logarithmic Axis Stabilization:** The Mineral Production module implements a true **Logarithmic Scale** (`log_x=True`) on horizontal vectors. This prevents high-volume data (e.g., Coal at 8,400M tonnes) from rendering low-volume transition components (e.g., Lithium at 0.13M tonnes) completely invisible on standard pixel displays.
* **High-Contrast presentation Styling:** Embedded custom CSS styling combined with `plotly_dark` layouts forces clean typography and absolute high contrast, making the interface exceptionally readable under bright projector lights or screens.
* **Modular Tab Selection:** Neatly sections distinct datasets to allow developers or presenters to pace their delivery topic-by-topic.

---

## Modeled Datasets & Sources

The quantitative metrics used in this model are mapped from empirical global frameworks:
1. **Energy Footprint:** Electricity generation percentages and oil reserves metrics (mapped from the BP / Energy Institute Statistical Review).
2. **Forest Vectors:** Multi-decadal regional land cover variance from 2000 to current metrics (World Bank & UN FAO).
3. **Extraction Volumes:** Critical mineral production indices (U.S. Geological Survey).
4. **Water Assets:** National/Continental annual freshwater extraction levels (FAO AQUASTAT).

---

## Local Setup & Deployment

To launch the web application server on your machine, follow these execution steps via your terminal (do not run the file directly through standard editor script execution keys):

 1. Project Assembly
```bash
git clone [https://github.com/YOUR_USERNAME/global-resource-analytics.git](https://github.com/YOUR_USERNAME/global-resource-analytics.git)
cd global-resource-analytics

2. Dependency Resolution
Install the required computational and presentation packages:
python -m pip install streamlit pandas plotly

3. Initiate the Streamlit Server
Execute the runtime command via the Command Line Interface (CLI):
python -m streamlit run app.py

Core Discussion Points for Project EvaluationsData Normalization:
Be prepared to highlight the technical necessity of the Logarithmic Scale. On standard linear grids, the vast numeric discrepancy between Coal and Lithium distorts the chart utility; applying logarithmic transformations scales the visual space efficiently without modifying original data values.Sustainability Insights: The Freshwater Tab clearly indicates that Asia leads resource consumption with over $2,559\text{ km}^3/\text{year}$ due to heavy agricultural requirements. This frames the dashboard as a foundational tool for proving where CSE innovations—such as automated IoT smart irrigation meshes—are critically required.
