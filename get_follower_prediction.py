def get_follower_prediction(follower_count, influencer_type, num_months):
    # follower_count * (follower_type^num_months)
    initial_follower_count = follower_count
    constant = (
        4 if "fitness" == influencer_type else 3 if "cosmetic" == influencer_type else 2
    )
    predicted_follower_count = initial_follower_count * (constant**num_months)
    print(f"{influencer_type} constant: {constant}")
    return predicted_follower_count
