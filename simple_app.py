import streamlit as st
import pandas as pd

st.set_page_config(page_title="Exciton Explorer", layout="wide")

st.title("Simple Exciton Explorer")
st.write("A minimal Python app you can later deploy on Streamlit Community Cloud.")

sample_data = pd.DataFrame(
    {
        "Exciton": ["X1", "X2", "X3", "X4"],
        "Energy (eV)": [5.82, 5.95, 6.10, 6.25],
        "Oscillator strength": [0.82, 0.41, 0.19, 0.08],
        "Character": ["Bright", "Bright", "Dark", "Interlayer"],
        "System": ["BL-hBN", "BL-hBN", "ML-hBN", "MoS2/WS2"],
    }
)

st.sidebar.header("Filters")
selected_system = st.sidebar.multiselect(
    "System",
    options=sorted(sample_data["System"].unique()),
    default=sorted(sample_data["System"].unique()),
)

selected_character = st.sidebar.multiselect(
    "Character",
    options=sorted(sample_data["Character"].unique()),
    default=sorted(sample_data["Character"].unique()),
)

energy_range = st.sidebar.slider(
    "Energy range (eV)",
    min_value=float(sample_data["Energy (eV)"].min()),
    max_value=float(sample_data["Energy (eV)"].max()),
    value=(float(sample_data["Energy (eV)"].min()), float(sample_data["Energy (eV)"].max())),
)

filtered = sample_data[
    sample_data["System"].isin(selected_system)
    & sample_data["Character"].isin(selected_character)
    & sample_data["Energy (eV)"].between(energy_range[0], energy_range[1])
]

col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("Filtered exciton table")
    st.dataframe(filtered, use_container_width=True)

with col2:
    st.subheader("Quick summary")
    st.metric("Visible excitons", len(filtered))
    if not filtered.empty:
        st.metric("Mean energy (eV)", f"{filtered['Energy (eV)'].mean():.3f}")
        st.metric("Max oscillator strength", f"{filtered['Oscillator strength'].max():.3f}")
    else:
        st.info("No exciton matches the selected filters.")

st.subheader("Energy vs oscillator strength")
st.scatter_chart(filtered, x="Energy (eV)", y="Oscillator strength")

st.markdown("---")
st.write(
    "You can replace the sample data by your own Yambo/QE/BSE output and later add band plots, degeneracy cards, k-space maps, or publication-linked datasets."
)
