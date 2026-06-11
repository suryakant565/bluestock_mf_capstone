import pandas as pd

performance = pd.read_csv(
    "dashboards/fact_performance.csv"
)

def recommend_funds(risk_profile):

    if risk_profile == "Low":

        funds = performance[
            performance["risk_grade"] == "Low"
        ]

    elif risk_profile == "Moderate":

        funds = performance[
            performance["risk_grade"] == "Moderate"
        ]

    else:

        funds = performance[
            performance["risk_grade"] == "High"
        ]

    recommendations = (
        funds
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return recommendations[
        [
            "scheme_name",
            "fund_house",
            "sharpe_ratio"
        ]
    ]


risk = input(
    "Enter Risk Profile (Low/Moderate/High): "
)

print(
    recommend_funds(risk)
)

