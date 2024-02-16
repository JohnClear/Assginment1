import pandas as pd
import argparse

def clean(input_file1, input_file2, output_file):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    merged_df = pd.merge(df1, df2, on='id', how='inner')
    merged_df = merged_df.dropna()

    merged_df.to_csv(output_file, index=False)
    print(f"Merged data shape: {merged_df.shape}")
    return merged_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='First data file (CSV)')
    parser.add_argument('input2', help='Second data file (CSV)')
    parser.add_argument('output', help='Cleaned and merged data file (CSV)')
    args = parser.parse_args()

    clean(args.input1, args.input2, args.output)
