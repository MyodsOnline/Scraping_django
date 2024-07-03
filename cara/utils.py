def data_scan():
    return ['2024-06-28', '2024-06-29', '2024-06-30']


def time_scan(selected_date):
    if selected_date == '2024-06-28':
        return ['09:00', '10:00', '11:00']
    elif selected_date == '2024-06-29':
        return ['12:00', '13:00', '14:00']
    else:
        return ['15:00', '16:00', '17:00']
