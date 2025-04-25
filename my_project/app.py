import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

from preswald import (
    chat,
    get_df,
    plotly,
    sidebar,
    table,
    text,
)

# Initialize sidebar
sidebar()

# Report Title
text(
    "# AI-Generated Content Analysis Dashboard \n A comprehensive analysis of AI-generated content across industries, examining trends, adoption rates, and economic impact."
)

# Load the dataset
df = get_df("ai_content")

# Verify if the dataframe was loaded correctly
if df is None or df.empty:
    text("Error: Could not load the dataset!")
    exit()

# 1. Industry Distribution Analysis
text(
    "## Industry Distribution \n This visualization shows the distribution of AI-generated content across different industries, highlighting adoption patterns and market penetration."
)
fig1 = px.pie(
    df,
    names="Industry",
    color_discrete_sequence=px.colors.qualitative.Set3
)
fig1.update_layout(
    template="plotly_white",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial", size=12),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)
plotly(fig1)

# 2. AI Adoption Trends Over Time
text(
    "## AI Adoption Trends \n This line chart tracks the evolution of AI adoption rates across different industries over time."
)
fig2 = px.line(
    df,
    x="Year",
    y="AI Adoption Rate (%)",
    color="Industry",
    title="AI Adoption Rate Over Time",
    labels={
        "Year": "Year",
        "AI Adoption Rate (%)": "AI Adoption Rate (%)",
        "Industry": "Industry"
    }
)
fig2.update_layout(
    template="plotly_white",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial", size=12),
    hovermode="x unified"
)
plotly(fig2)

# 3. Content Volume vs Revenue Impact
text(
    "## Content Volume vs Revenue Impact \n This scatter plot examines the relationship between AI-generated content volume and revenue increase."
)
fig3 = px.scatter(
    df,
    x="AI-Generated Content Volume (TBs per year)",
    y="Revenue Increase Due to AI (%)",
    color="Industry",
    size="Market Share of AI Companies (%)",
    title="Content Volume vs Revenue Impact",
    labels={
        "AI-Generated Content Volume (TBs per year)": "Content Volume (TB/year)",
        "Revenue Increase Due to AI (%)": "Revenue Increase (%)",
        "Industry": "Industry",
        "Market Share of AI Companies (%)": "Market Share (%)"
    }
)
fig3.update_layout(
    template="plotly_white",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial", size=12)
)
plotly(fig3)

# 4. Economic and Social Impact Analysis
text(
    "## Economic and Social Impact \n This bar chart compares various impacts of AI adoption across industries."
)
fig4 = px.bar(
    df,
    x="Industry",
    y=["Job Loss Due to AI (%)", "Revenue Increase Due to AI (%)", "Human-AI Collaboration Rate (%)"],
    title="Economic and Social Impact by Industry",
    labels={
        "Industry": "Industry",
        "value": "Percentage (%)",
        "variable": "Impact Type"
    },
    barmode="group"
)
fig4.update_layout(
    template="plotly_white",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial", size=12),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)
plotly(fig4)

# 5. Consumer Trust and Market Share
text(
    "## Consumer Trust and Market Share \n This heatmap visualizes the relationship between consumer trust and market share of AI companies across industries."
)
fig5 = px.density_heatmap(
    df,
    x="Consumer Trust in AI (%)",
    y="Industry",
    z="Market Share of AI Companies (%)",
    title="Consumer Trust vs Market Share",
    labels={
        "Consumer Trust in AI (%)": "Consumer Trust (%)",
        "Industry": "Industry",
        "Market Share of AI Companies (%)": "Market Share (%)"
    }
)
fig5.update_layout(
    template="plotly_white",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial", size=12)
)
plotly(fig5)

# Dataset Overview
text(
    "## Dataset Overview \n Below is a sample of the AI content analysis dataset, showing key metrics and attributes for each record."
)
table(df.head(10))

# Interactive Analysis Section
text(
    "## Interactive Analysis \n Use the chat interface below to explore the dataset further. You can ask questions about specific trends, request explanations of the visualizations, or get additional insights about AI content generation patterns."
)

chat("ai_content")