import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="IPL Data Analysis", layout="wide")

st.title("🏏 IPL Data Analysis App")
st.markdown("Upload IPL dataset files to explore insights from over 12+ years of matches.")

# Upload CSV files
matches_file = st.file_uploader("Upload matches.csv", type="csv")
deliveries_file = st.file_uploader("Upload deliveries.csv", type="csv")

if matches_file and deliveries_file:
    matches = pd.read_csv(matches_file)
    deliveries = pd.read_csv(deliveries_file)

    st.subheader("🎯 Basic Match Stats")
    st.write("Total Matches:", matches.shape[0])
    st.write("Seasons:", matches['season'].nunique())
    st.write("Cities Played:", matches['city'].nunique())

    st.subheader("🏆 Most Winning Teams")
    st.bar_chart(matches['winner'].value_counts())

    st.subheader("📈 Toss vs Match Win")
    toss_match_win = matches[matches['toss_winner'] == matches['winner']]
    st.write("Matches where toss winner also won the match:", toss_match_win.shape[0])

    # Top Run Scorers
    runs = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
    runs.plot(kind='bar', color='green', title='Top Run Scorers')
    plt.ylabel("Runs")
    plt.xticks(rotation=45)
    plt.show()


    # Top Wicket Takers
    st.subheader("🎯 Top Wicket Takers")
    dismissals = deliveries[deliveries['dismissal_kind'].notna()]
    top_bowlers = dismissals['bowler'].value_counts().head(10)
    st.bar_chart(top_bowlers)

else:
    st.info("Please upload both `matches.csv` and `deliveries.csv` to continue.")
