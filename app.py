import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Natural Resources Analysis - Dark Edition", layout="wide")

# --- DATASETS ---
energy_df = pd.DataFrame({
    'Source': ['Hydro', 'Wind', 'Solar', 'Nuclear', 'Biomass', 'Coal', 'Natural Gas', 'Oil'],
    'Percentage': [26, 22, 18, 10, 8, 8, 6, 2],
    'Fact': ['Largest renewable source.', 'Rapid growth in offshore capacity.', 'Highest annual growth rate.', 'Stable baseload power.', 'Crucial for heating.', 'Declining in the West.', 'Lower emissions than coal.', 'Primarily used for transport.']
})

forest_df = pd.DataFrame({
    'Region': ['South America', 'Europe', 'North America', 'Africa', 'Asia'],
    'Coverage_2000': [57, 32, 34, 23, 19],
    'Coverage_2023': [49, 35, 34, 20, 20]
})

water_df = pd.DataFrame({
    'Continent': ['Asia', 'Americas', 'Europe', 'Africa', 'Oceania'],
    'Withdrawal': [2559, 1015, 418, 215, 25],
    'Details': [
        'Highest usage globally, primarily driven by massive agricultural irrigation.',
        'High industrial and agricultural withdrawal in both North and South America.',
        'Significant portion dedicated to industrial cooling and public supply.',
        'Primarily used for agriculture; many regions face severe water stress.',
        'Lowest total volume due to smaller population and specific land use.'
    ]
})

min_df = pd.DataFrame({
    'Mineral': ['Coal', 'Iron Ore', 'Bauxite', 'Copper', 'Zinc', 'Nickel', 'Lithium'],
    'Production': [8400, 2600, 390, 22, 13, 3.3, 0.13]
})

# --- DARK THEME STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .metric-card { 
        background-color: #111111; padding: 20px; border-radius: 12px; 
        border: 1px solid #222222; text-align: center;
    }
    .metric-label { font-size: 12px; color: #888888; font-weight: 700; text-transform: uppercase; }
    .metric-value { font-size: 32px; font-weight: 800; color: #FFFFFF; }
    
    .detail-card {
        background-color: #0A0A0A; padding: 25px; border-left: 5px solid #378ADD;
        border-radius: 8px; border: 1px solid #222;
    }
    .detail-header { color: #378ADD; font-weight: 800; text-transform: uppercase; font-size: 13px; }
    h1, h2, h3, p, span, label { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("📊 Natural Resources Global Dashboard")
st.markdown("<p style='color: #666 !important;'>Energy · Forests · Minerals · Water</p>", unsafe_allow_html=True)

# --- KPI ROW ---
k1, k2, k3, k4 = st.columns(4)
with k1: st.markdown('<div class="metric-card"><p class="metric-label">Oil Reserves</p><p class="metric-value">1.73T</p></div>', unsafe_allow_html=True)
with k2: st.markdown('<div class="metric-card"><p class="metric-label">Hydro Share</p><p class="metric-value">26%</p></div>', unsafe_allow_html=True)
with k3: st.markdown('<div class="metric-card"><p class="metric-label">Forest Cover</p><p class="metric-value">31%</p></div>', unsafe_allow_html=True)
with k4: st.markdown('<div class="metric-card"><p class="metric-label">Water Withdrawal</p><p class="metric-value">4.2k</p></div>', unsafe_allow_html=True)

st.write("---")

# --- TABS ---
tabs = st.tabs(["⚡ Energy", "🌳 Forests", "💎 Minerals", "💧 Water"])

# --- WATER TAB ---
with tabs[3]:
    st.subheader("Freshwater Withdrawal Analysis")
    col_a, col_b = st.columns([1.6, 1])
    
    with col_a:
        selected_continent = st.selectbox("Select Continent to Analyze:", water_df['Continent'])
        fig_wat = px.bar(water_df, x='Continent', y='Withdrawal', 
                         color='Withdrawal', color_continuous_scale='Blues',
                         template="plotly_dark", labels={'Withdrawal': 'km³/year'})
        fig_wat.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_wat, use_container_width=True)

    with col_b:
        w_info = water_df[water_df['Continent'] == selected_continent].iloc[0]
        st.markdown(f"""
            <div class="detail-card">
                <span class="detail-header">Water Resource Insight</span>
                <h2>{selected_continent}</h2>
                <p style="font-size: 24px; color: #378ADD !important;">{w_info['Withdrawal']} km³/year</p>
                <hr style="border: 0.5px solid #333;">
                <p><b>Context:</b> {w_info['Details']}</p>
                <p style="font-size: 12px; color: #888 !important;">Source: FAO AQUASTAT</p>
            </div>
        """, unsafe_allow_html=True)

# --- ENERGY TAB ---
with tabs[0]:
    col_e1, col_e2 = st.columns([1.6, 1])
    with col_e1:
        st.subheader("Electricity Mix")
        selected_e = st.selectbox("Select Energy Source:", energy_df['Source'])
        fig_e = px.pie(energy_df, values='Percentage', names='Source', hole=0.6, template="plotly_dark")
        fig_e.update_layout(paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_e, use_container_width=True)
    with col_e2:
        e_data = energy_df[energy_df['Source'] == selected_e].iloc[0]
        st.markdown(f'<div class="detail-card" style="border-left-color:#1D9E75"><h2>{selected_e}</h2><p>{e_data["Fact"]}</p></div>', unsafe_allow_html=True)

# --- FOREST TAB ---
with tabs[1]:
    col_f1, col_f2 = st.columns([1.6, 1])
    with col_f1:
        st.subheader("Forest Coverage Trends")
        selected_r = st.radio("Region:", forest_df['Region'], horizontal=True)
        r_plot = forest_df[forest_df['Region'] == selected_r].melt(id_vars='Region')
        fig_f = px.bar(r_plot, x='variable', y='value', color='variable', template="plotly_dark")
        fig_f.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_f, use_container_width=True)
    with col_f2:
        st.markdown(f'<div class="detail-card" style="border-left-color:#BA7517"><h3>{selected_r}</h3><p>Analysis of land area percentage shift from 2000 to 2023.</p></div>', unsafe_allow_html=True)

# --- MINERAL TAB ---
with tabs[2]:
    st.subheader("Global Mineral Production")
    fig_m = px.bar(min_df.sort_values('Production'), x='Production', y='Mineral', orientation='h', log_x=True, template="plotly_dark", color='Production')
    fig_m.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_m, use_container_width=True)

st.markdown("<p style='text-align: center; margin-top: 50px; color: #444 !important;'>Data: BP · World Bank · FAO · USGS</p>", unsafe_allow_html=True)