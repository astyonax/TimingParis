# Scripts

1. `TimeParis.py`: runs on the root folder of the project to get the daily dose of data (2500 GMaps calls)
   It's thought to run alone as cron job on a raspberry pi

2. `make_summary_plots.py`: writes the file plots_summary.md with all the png and jpg files in plots
   and calls `convert -trim` on every image

3. `assemble_daily_records.py`: to avoid unforseen error, `TimeParis.py` writes the daily data
on a  separate file. These files are assembles by this script in a big juicy file.
