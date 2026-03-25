from functools import reduce


def get_estimated_spread(audiences_followers):
    if len(audiences_followers) == 0:
        return 0
    num_followers = len(audiences_followers)
    average_audience_followers = (
        reduce(lambda a, b: a + b, audiences_followers, 0) / num_followers
    )
    estimated_spread = average_audience_followers * (num_followers**1.2)
    return estimated_spread
