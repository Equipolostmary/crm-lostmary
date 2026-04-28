def create_unique_id(row):
    try:
        return f"{row['EXP']}_{row['POBLACION']}_{row['CIUDAD']}"
    except:
        return None

def unify_data(all_sheets):
    unified = []

    for sheet_name, df in all_sheets.items():
        if not df.empty:
            df["sheet_name"] = sheet_name
            df["unique_id"] = df.apply(create_unique_id, axis=1)
            unified.append(df)

    return unified
