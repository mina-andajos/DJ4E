def natural_size(size: int | float):
    size_float: float = float(size)

    K = 1024
    M = K * K
    G = M * K

    if size_float < K:
        return f"{size}B"

    if K <= size_float < M:
        return f"{int(size_float / (K / 10.0)) / 10.0}KB"

    if M <= size_float < G:
        return f"{int(size_float / (M / 10.0)) / 10.0}MB"

    else:
        return f"{int(size_float / (G / 10.0)) / 10.0}GB"
