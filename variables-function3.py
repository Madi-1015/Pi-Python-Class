def calculate_mars_weight(weight):
    return e_weight * 0.378

e_weight = float(input("Earth Weight: "))
m_weight = calculate_mars_weight(e_weight)
print(f"Mars Weight: {m_weight}")