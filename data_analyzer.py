import pandas as pd

def calculate_similarity(column_df1, column_df2):
    length_unique_df1 = len(set(column_df1))
    length_unique_df2 = len(set(column_df2))

    length_overlap = len(set(column_df1) & set(column_df2))

    overlap_percentage = (length_overlap / min(length_unique_df1, length_unique_df2))

    return overlap_percentage

def similarity(df1, df2):
    similarity_results = pd.DataFrame(columns=['Colonna1', 'Colonna2', 'Similarita'])

    for col1 in df1.columns:
        for col2 in df2.columns:
            similarity = calculate_similarity(df1[col1], df2[col2])
            new_row = {'Colonna1': [col1], 'Colonna2': [col2], 'Similarita': [similarity]}
            new_row = pd.DataFrame(new_row)
            similarity_results = pd.concat([similarity_results, new_row], ignore_index=True)

    groupped = similarity_results.groupby('Colonna1')
    idx =  groupped['Similarita'].idxmax()
    max_scores = similarity_results.loc[idx]

    max_scores = max_scores[max_scores['Similarita']>0.8]
    max_scores = max_scores[['Colonna1', 'Colonna2']]
    max_scores = max_scores.to_dict()
    max_scores = {key: list(value.values()) for key, value in max_scores.items()}

    return max_scores


