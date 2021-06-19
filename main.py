from so import get_jobs
from save_csv import save_to_csv

so_jobs = get_jobs()
save_to_csv(so_jobs)