def can_bob_reach_alice(n, s, first_track, second_track):
    if first_track[0] == 1 and first_track[s - 1] == 1:
        return "YES"
    for k in range(s, n):
        if first_track[k] == 1 and second_track[k] == 1 and second_track[s - 1] == 1:
            return "YES"
    return "NO"
