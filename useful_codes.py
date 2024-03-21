import pandas as pd

# Chunking CSV files
def chunk_csv_file(csv_fp: str, chunk_size: int):
  chunks = []
  for chunk in pd.read_csv(csv_fp, chunksize=chunk_size):
    chunks.append(chunk)
  return pd.concat(chunks)
    
