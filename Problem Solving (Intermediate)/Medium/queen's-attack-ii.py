def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    # Define array to store steps which could go with direction order by closewise (8 directions)
    steps = [
        r_q - 1,
        min(r_q - 1, n - c_q),
        n - c_q,
        min(n - c_q, n - r_q),
        n - r_q,
        min(n - r_q, c_q - 1),
        c_q - 1,
        min(c_q - 1, r_q - 1),
    ]

    for i in range(len(obstacles)):
        if obstacles[i][0] - r_q == 0:
            if obstacles[i][1] > c_q:
                steps[2] = min(steps[2], obstacles[i][1] - c_q - 1)
            else:
                steps[6] = min(steps[6], c_q - obstacles[i][1] - 1)
        elif obstacles[i][1] - c_q == 0:
            if obstacles[i][0] > r_q:
                steps[4] = min(steps[4], obstacles[i][0] - r_q - 1)
            else:
                steps[0] = min(steps[0], r_q - obstacles[i][0] - 1)
        elif obstacles[i][0] - r_q == obstacles[i][1] - c_q:
            if obstacles[i][0] > r_q:
                steps[3] = min(steps[3], obstacles[i][0] - r_q - 1)
            else:
                steps[7] = min(steps[7], r_q - obstacles[i][0] - 1)
        elif obstacles[i][0] - r_q == c_q - obstacles[i][1]:
            if obstacles[i][0] > r_q:
                steps[5] = min(steps[5], obstacles[i][0] - r_q - 1)
            else:
                steps[1] = min(steps[1], r_q - obstacles[i][0] - 1)
    return sum(steps)
