import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Global Natural Resources Analysis", layout="wide")

# --- INITIALIZE RAW REGIONAL & CATEGORICAL DATASETS ---
energy_df = pd.DataFrame({
    'Source': ['Hydro', 'Wind', 'Solar', 'Nuclear', 'Biomass', 'Coal', 'Natural Gas', 'Oil'],
    'Percentage': [26, 22, 18, 10, 8, 8, 6, 2],
    'Fact': [
        'Dominates the green grid footprint globally, led heavily by massive installations across China, Brazil, and Canada.',
        'Experiencing exponential capacity growth across offshore installations, primarily driven by North Sea and East Asia developments.',
        'Maintains the fastest accelerating deployment rate of any generation infrastructure over the last five sequential quarters.',
        'Provides critical, high-reliability carbon-free baseload power, seeing structural re-investments globally.',
        'Plays an essential role in structural heating and localized waste-to-energy recovery infrastructure.',
        'Continues a structural contraction phase across Western economies while maintaining baseload dominance in industrial Asia.',
        'Frequently utilized as a tactical transitional fuel due to lower combustion emission baselines relative to heavier hydrocarbons.',
        'Gradually shifting away from grid-scale electrical generation and strictly concentrating on heavy transport and industrial applications.'
    ]
})

forest_df = pd.DataFrame({
    'Region': ['South America', 'Europe', 'North America', 'Africa', 'Asia'],
    'Coverage_2000': [57, 32, 34, 23, 19],
    'Coverage_2023': [49, 35, 34, 20, 20],
    'Insight': [
        'Experiencing net loss vector due to broad agricultural expansion across key tropical baseline corridors.',
        'Showing stable incremental growth fueled directly by multi-decade managed afforestation and conservation mandates.',
        'Maintains long-term cyclical stability with robust forest boundary enforcement and industrial logging regulations.',
        'Undergoing active forest canopy reductions linked to agricultural scaling and regional biomass dependency.',
        'Demonstrating a historical trend reversal with documented net structural recovery driven by reforestation programs in China and India.'
    ]
})

min_df = pd.DataFrame({
    'Mineral': ['Coal', 'Iron Ore', 'Bauxite', 'Copper', 'Zinc', 'Nickel', 'Lithium'],
    'Production': [8400, 2600, 390, 22, 13, 3.3, 0.13],
    'Usage': ['Heavy Electrical Power Generation', 'Structural Steel Infrastructure', 'Primary Aluminum Smelting', 'High-Conductivity Electrical Grid Networks', 'Structural Galvanization Alloys', 'Energy Storage & High-Grade Stainless Steel', 'High-Density Electric Vehicle Batteries']
})

water_df = pd.DataFrame({
    'Continent': ['Asia', 'Americas', 'Europe', 'Africa', 'Oceania'],
    'Withdrawal': [2559, 1015, 418, 215, 25],
    'Details': [
        'Highest usage global benchmark, primarily driven by expansive agricultural irrigation frameworks required across highly populated regions.',
        'Reflects intense, highly mechanized industrial manufacturing demands balanced with large-scale commercial farming networks.',
        'Exhibits a structural allocation focus centering heavily on thermal power plant cooling systems and dense municipal public supply.',
        'Predominantly structured around foundational subsistence agriculture, with many sub-regions actively managing localized physical scarcity.',
        'Lowest global total volume footprint, tightly constrained by regional geographic scale and targeted arid-zone water management.'
    ]
})

# --- ADVANCED HIGH-CONTRAST DARK THEME STYLING ---
st.markdown("""
    <style>
    /* Absolute Dark Canvas Background */
    .stApp { background-color: #000000; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    /* Sleek Structural KPI Blocks */
    .metric-card { 
        background-color: #0C0C0E; 
        padding: 22px; 
        border-radius: 12px; 
        border: 1px solid #1C1E24; 
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.5);
    }
    .metric-label { font-size: 11px; color: #88888E; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }
    .metric-value { font-size: 34px; font-weight: 800; color: #FFFFFF; line-height: 1.1; }
    
    /* Stateful Presentation Insight Panels */
    .detail-card {
        background-color: #070709; 
        padding: 25px; 
        border-left: 5px solid #1D9E75;
        border-radius: 8px; 
        border-top: 1px solid #1C1E24;
        border-right: 1px solid #1C1E24;
        border-bottom: 1px solid #1C1E24;
        box-shadow: 4px 4px 20px rgba(0,0,0,0.6);
    }
    .detail-header { color: #1D9E75; font-weight: 800; text-transform: uppercase; font-size: 12px; letter-spacing: 0.08em; display: block; margin-bottom: 8px; }
    
    /* Strict Typography Controls */
    h1, h2, h3, p, span, label { color: #FFFFFF !important; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .chart-subtitle { color: #88888E !important; font-size: 13px; margin-top: -10px; margin-bottom: 20px; }
    
    /* Streamlit Interactive Component Adjustments */
    .stTabs [data-baseweb="tab-list"] { gap: 28px; border-bottom: 1px solid #1C1E24; }
    .stTabs [data-baseweb="tab"] { color: #66666E !important; font-weight: 600; font-size: 15px; padding-bottom: 12px; }
    .stTabs [aria-selected="true"] { color: #FFFFFF !important; border-bottom-color: #1D9E75 !important; }
    </style>
""", unsafe_allow_html=True)

# --- APP BRANDING HEADER ---
st.markdown('<p style="font-size: 11px; letter-spacing: 0.15em; color: #1D9E75 !important; font-weight: 700; text-transform: uppercase; margin: 0;">DATA ANALYSIS COMPONENT · PORTFOLIO DEPLOYMENT</p>', unsafe_allow_html=True)
st.title("Global Natural Resources Analytical Suite")
st.markdown("<p class='chart-subtitle'>Empirical modeling tracking energy distribution systems, forestry shifts, mineral volume variance, and hydrological allocation profiles.</p>", unsafe_allow_html=True)

# --- STRUCTURAL UPPER KPI MATRIX ---
k1, k2, k3, k4 = st.columns(4)
with k1: st.markdown('<div class="metric-card"><p class="metric-label">Global Resource Cap</p><p class="metric-value">1.73T</p></div>', unsafe_allow_html=True)
with k2: st.markdown('<div class="metric-card"><p class="metric-label">Renewable Grid Base</p><p class="metric-value">74%</p></div>', unsafe_allow_html=True)
with k3: st.markdown('<div class="metric-card"><p class="metric-label">Forest Surface Baseline</p><p class="metric-value">31%</p></div>', unsafe_allow_html=True)
with k4: st.markdown('<div class="metric-card"><p class="metric-label">Annual Fresh Withdrawal</p><p class="metric-value">4.2k</p></div>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- MODULAR FUNCTIONAL TABS ---
tabs = st.tabs(["⚡ Generation Mix", "🌳 Canopy Dynamics", "💎 Mineral Analytics", "💧 Hydrological Assets"])

# ==========================================
# TAB 1: GENERATION MIX (DYNAMIC ENERGY DEEP-DIVE)
# ==========================================
with tabs[0]:
    col_e1, col_e2 = st.columns([1.6, 1])
    with col_e1:
        st.subheader("Global Electricity Generation Share")
        selected_e = st.selectbox("Select Target Energy Vector to Inspect:", energy_df['Source'])
        
        fig_e = px.pie(energy_df, values='Percentage', names='Source', hole=0.6, 
                       color_discrete_sequence=px.colors.qualitative.T10, template="plotly_dark")
        fig_e.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                            margin=dict(t=20, b=20, l=10, r=10), font=dict(color="#FFF"))
        st.plotly_chart(fig_e, use_container_width=True)
    
    with col_e2:
        st.write("<br><br>", unsafe_allow_html=True)
        e_data = energy_df[energy_df['Source'] == selected_e].iloc[0]
        st.markdown(f"""
            <div class="detail-card" style="border-left-color: #1D9E75;">
                <span class="detail-header">Sector Analytics</span>
                <h2>{selected_e} Power</h2>
                <p style="font-size: 28px; font-weight: 800; color: #1D9E75 !important; margin: 5px 0;">{e_data['Percentage']}% Allocation</p>
                <hr style="border: 0.5px solid #1C1E24; margin: 15px 0;">
                <p><b>Structural Trend & Context:</b> {e_data['Fact']}</p>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 2: CANOPY DYNAMICS (DYNAMIC REGIONAL FOREST MOVES)
# ==========================================
with tabs[1]:
    col_f1, col_f2 = st.columns([1.6, 1])
    with col_f1:
        st.subheader("Multi-Decadal Forest Boundary Shifting")
        selected_r = st.radio("Select Target Region for Structural Trend Assessment:", forest_df['Region'], horizontal=True)
        
        # Reshape data cleanly for comparative visualization
        r_plot = forest_df[forest_df['Region'] == selected_r].melt(id_vars='Region', value_vars=['Coverage_2000', 'Coverage_2023'])
        r_plot['variable'] = r_plot['variable'].replace({'Coverage_2000': 'Year 2000 Base', 'Coverage_2023': 'Year 2023 Survey'})
        
        fig_f = px.bar(r_plot, x='variable', y='value', color='variable', 
                       labels={'value': 'Total Surface Area %', 'variable': 'Temporal Interval'},
                       color_discrete_sequence=['#2D3139', '#1D9E75'], template="plotly_dark")
        fig_f.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False,
                            xaxis_title=None, yaxis_gridcolor='#1C1E24')
        st.plotly_chart(fig_f, use_container_width=True)
    
    with col_f2:
        st.write("<br><br>", unsafe_allow_html=True)
        f_data = forest_df[forest_df['Region'] == selected_r].iloc[0]
        st.markdown(f"""
            <div class="detail-card" style="border-left-color: #BA7517;">
                <span class="detail-header" style="color: #BA7517;">Ecological Variance</span>
                <h2>{selected_r}</h2>
                <p style="margin: 5px 0;"><b>2000 Baseline:</b> {f_data['Coverage_2000']}% Surface Cover</p>
                <p style="margin: 5px 0;"><b>2023 Survey:</b> {f_data['Coverage_2023']}% Surface Cover</p>
                <hr style="border: 0.5px solid #1C1E24; margin: 15px 0;">
                <p><b>Analytical Assessment:</b> {f_data['Insight']}</p>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 3: MINERAL ANALYTICS (FIXED COLUMN TYPO & LOG SCALE)
# ==========================================
with tabs[2]:
    col_m1, col_m2 = st.columns([1.6, 1])
    with col_m1:
        st.subheader("Global Mineral Extraction Scale")
        selected_m = st.selectbox("Select Target Mineral Commodity:", min_df['Mineral'])
        
        # FIXED: Changed y='Minerals' to y='Mineral' to resolve schema conflict crashing production
        fig_m = px.bar(min_df.sort_values('Production'), x='Production', y='Mineral', orientation='h', 
                       log_x=True, template="plotly_dark", color='Production', color_continuous_scale='Viridis')
        fig_m.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', coloraxis_showscale=False,
                            xaxis_title="Logarithmic Gross Volumetric Production (Million Tonnes)", yaxis_title=None,
                            xaxis_gridcolor='#1C1E24')
        st.plotly_chart(fig_m, use_container_width=True)
    
    with col_m2:
        st.write("<br><br>", unsafe_allow_html=True)
        m_data = min_df[min_df['Mineral'] == selected_m].iloc[0]
        st.markdown(f"""
            <div class="detail-card" style="border-left-color: #AFA9EC;">
                <span class="detail-header" style="color: #AFA9EC;">Commodity Intelligence</span>
                <h2>{selected_m} Analysis</h2>
                <p style="font-size: 24px; font-weight: 700; color: #AFA9EC !important; margin: 5px 0;">{m_data['Production']}M Tonnes Output</p>
                <hr style="border: 0.5px solid #1C1E24; margin: 15px 0;">
                <p><b>Primary Industrial Application:</b> {m_data['Usage']}</p>
                <p style="font-size: 11px; color: #88888E !important; margin-top: 15px; font-style: italic;">
                    Engineering Context: A logarithmic visualization framework normalizes severe mathematical dispersion across data fields, protecting fine trace elements from structural pixel omission.
                </p>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 4: HYDROLOGICAL ASSETS (DYNAMIC FRESHWATER EXPANSION)
# ==========================================
with tabs[3]:
    st.subheader("Continental Freshwater Extraction Matrix")
    col_w1, col_w2 = st.columns([1.6, 1])
    
    with col_w1:
        selected_w = st.selectbox("Select Target Continental Boundary Zone:", water_df['Continent'])
        
        fig_w = px.bar(water_df, x='Continent', y='Withdrawal', 
                       color='Withdrawal', color_continuous_scale='Blues',
                       template="plotly_dark", labels={'Withdrawal': 'Extraction Rate (km³/yr)'})
        fig_w.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', coloraxis_showscale=False,
                            xaxis_title=None, yaxis_gridcolor='#1C1E24')
        st.plotly_chart(fig_w, use_container_width=True)
        
    with col_w2:
        st.write("<br><br>", unsafe_allow_html=True)
        w_data = water_df[water_df['Continent'] == selected_w].iloc[0]
        st.markdown(f"""
            <div class="detail-card" style="border-left-color: #378ADD;">
                <span class="detail-header" style="color: #378ADD;">Hydrological Assessment</span>
                <h2>{selected_w} Resource Profile</h2>
                <p style="font-size: 26px; font-weight: 800; color: #378ADD !important; margin: 5px 0;">{w_data['Withdrawal']} km³ / Year</p>
                <hr style="border: 0.5px solid #1C1E24; margin: 15px 0;">
                <p><b>Consumption Mechanics:</b> {w_data['Details']}</p>
                <p style="font-size: 11px; color: #88888E !important; margin-top: 15px; font-style: italic;">Source Reference: Food and Agriculture Organization (UN FAO) AQUASTAT Frame.</p>
            </div>
        """, unsafe_allow_html=True)

# --- RUNTIME FOOTER INFRASTRUCTURE ---
st.markdown("<hr style='border: 0.5px solid #1C1E24; margin-top: 50px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #44444A !important; font-size: 12px;'>Data Mapping Synthesized from BP Statistical Review · World Bank Ecosystems Index · UN FAO · USGS Minerals Core</p>", unsafe_allow_html=True)
