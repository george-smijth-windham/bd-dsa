def decayed_followers(initial_followers, fraction_lost_daily, days):
    retention_rate = 1 - fraction_lost_daily
    return initial_followers * (retention_rate**days)
