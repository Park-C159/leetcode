import pandas as pd


def top_traveller_simple(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    ridesSumById = rides.groupby(["user_id"])["distance"].sum().reset_index()
    ridesSumById.columns = ["id", "travelled_distance"]
    merge = pd.merge(users, ridesSumById, on="id", how="left")

    res = merge[["name", "travelled_distance"]]
    res["travelled_distance"] = res["travelled_distance"].fillna(0)
    result_df = res.sort_values(["travelled_distance", "name"], ascending=[False, True])

    return result_df
