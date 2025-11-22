# obtain a list of files in the input directory
import os

files_in_input_dir=os.listdir('data/input/')
files_in_input_dir



# count the frequency of the words in the files in the input directory
counter={}
for filename in files_in_input_dir:
    with open('data/input/'+filename) as f:
        for l in f:
            for w in l.split( ):
                w = w.lower().strip(",.!?")
                counter[w] = counter.get(w, 0) + 1


# create the directory output/ if it doesn't exist
if not os.path.exists('data/output'):
    os.makedirs('data/output')

# save the results using tsv format
with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")
