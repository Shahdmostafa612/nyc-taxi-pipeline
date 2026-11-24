import os, sys
import pyarrow.parquet as pq
from sqlalchemy import create_engine

path = sys.argv[1]  # e.g. /data/yellow_tripdata_2024-01.parquet
u, p, d = os.environ["POSTGRES_USER"], os.environ["POSTGRES_PASSWORD"], os.environ["POSTGRES_DB"]
engine = create_engine(f"postgresql+psycopg2://{u}:{p}@postgres:5432/{d}")

pf = pq.ParquetFile(path)
for i, batch in enumerate(pf.iter_batches(batch_size=100_000)):
    df = batch.to_pandas()
    df.columns = [c.lower() for c in df.columns]
    df.to_sql("yellow_trips_raw", engine,
              if_exists="replace" if i == 0 else "append", index=False)
    print(f"loaded chunk {i}")