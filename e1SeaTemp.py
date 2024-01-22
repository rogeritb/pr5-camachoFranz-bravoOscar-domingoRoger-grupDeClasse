# region Definició de dades
data = {
    'Gener': {'2000': 12.7, '2001': 13.8, '2002': 13.2, '2022': 13.6},
    'Febrer': {'2000': 12.4, '2001': 13.0, '2002': 12.4, '2022': 13.4},
    'Març': {'2000': 12.6, '2001': 12.6, '2002': 12.9, '2022': 13.2},
    'Abril': {'2000': 12.4, '2001': 13.6, '2002': 13.4, '2022': 13.4},
    'Maig': {'2000': 13.0, '2001': 13.5, '2002': 13.7, '2022': 13.9},
    'Juny': {'2000': 13.6, '2001': 13.5, '2002': 13.7, '2022': 13.9},
    'Juliol': {'2000': 13.3, '2001': 14.0, '2002': 14.4, '2022': 13.7},
    'Agost': {'2000': 13.5, '2001': 14.0, '2002': 14.0, '2022': 13.7},
    'Setembre': {'2000': 13.5, '2001': 14.2, '2002': 14.3, '2022': 13.8},
    'Octubre': {'2000': 15.9, '2001': 15.3, '2002': 14.8, '2022': 14.0},
    'Novembre': {'2000': 15.3, '2001': 16.8, '2002': 15.9, '2022': 14.3},
    'Desembre': {'2000': 14.9, '2001': 14.0, '2002': 14.2, '2022': 15.1},
}

annual_max = float('-inf')
annual_min = float('inf')
annual_avg = 0
overall_max = float('-inf')
overall_min = float('inf')
overall_avg = 0

for year in range(2000, 2023):
    year_data = {month: data[month][year] for month in data}
    annual_max = max(annual_max, max(year_data.values()))
    annual_min = min(annual_min, min(year_data.values()))
    annual_avg = sum(year_data.values()) / len(year_data)
    overall_max = max(overall_max, annual_max)
    overall_min = min(overall_min, annual_min)
    overall_avg += annual_avg


overall_avg /= 22


print(f"Any 2022")
print(f"Màxima: {annual_max:.1f} °C")
print(f"Mínima: {annual_min:.1f} °C")
print(f"Mitjana: {annual_avg:.1f} °C")
print(f"Període 2000 a 2022")
print(f"Màxima: {overall_max:.1f} °C")
print(f"Mínima: {overall_min:.1f} °C")
print(f"Mitjana: {overall_avg:.1f} °C")