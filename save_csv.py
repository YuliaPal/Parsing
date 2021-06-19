import csv

def save_to_csv(so_jobs):
  file = open('parsing_jobs', mode='w')
  writer = csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'link'])
  for job in so_jobs:
    writer.writerow(list(job.values()))
  return
