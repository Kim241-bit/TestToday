import statistics

def compute_variability(data):
    if not data:  # Handle empty list case
        return {"range": None, "variance": None, "std_dev": None}

    data_range = max(data) - min(data)  # Calculate range
    variance = statistics.variance(data) if len(data) > 1 else 0  # Sample variance
    std_dev = statistics.stdev(data) if len(data) > 1 else 0  # Sample standard deviation

    return {"range": data_range, "variance": variance, "std_dev": std_dev}


data = [10, 20, 30, 40, 50]
variability = compute_variability(data)
print(variability)



