import os
import re


def index_ranking_old(input_file=None, output_file=None):
	

	input_file = os.path.abspath(input_file.strip('"'))
	os.makedirs(os.path.dirname(output_file), exist_ok=True)
	
	with open(output_file, "w", newline="", encoding="utf-8") as fw:
		
		with open(input_file, "r", newline="", encoding='utf-8') as fr:
			header = fr.readline()
			fw.write(header)
			
			simple_counter = 0
			counter_map = {}
			for line in fr.readlines():
				if not line.strip():
					fw.write("\n")
					continue
				
				split_line = line.split(",")
				index_type, *_ = split_line
				
				if len(index_type) == 0:
					fw.write(line)
					continue
				
				if index_type.isdigit():
					simple_counter += 1
					fw.write(",".join([str(simple_counter)] + _))				
				else:
					prefix = list(index_type)[:-1]
					prefix = "".join(prefix)

					if not counter_map.get(prefix):
						counter_map[prefix] = 0
					counter_map[prefix] += 1
					
					updated_val = f'{prefix}{counter_map[prefix]}'
					fw.write(",".join([str(updated_val)] + _))

	print(f"\nCompleted: {output_file}")


def playlists_to_csv(input_folder, output_file):
    input_folder = os.path.abspath(input_folder.strip('"'))

    
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        for filename in os.listdir(input_folder):

            file_path = os.path.join(input_folder, filename)
            
            if not os.path.isfile(file_path):
                continue
            
            filename = re.sub(r'\.[^.]+$', '', filename)
            if (filename not in WHITELIST) or (filename in BLACKLIST):
                continue

            with open(file_path, "r", encoding="utf-8") as f:

                f_lines = [s for s in f.readlines() if not s.startswith('#')]
                count = len(f_lines)
                for line in f_lines:
                    line = line.strip()
                    
                    song_file = line.split("\\")[-1]
                    
                    parts_song, parts_artist = song_file.rstrip('.mp3').split(" - ")
                    parts_playlist = filename
                    parts_watch = WHITELIST[filename]
                    parts_rel_rank = f'{count}°/{len(f_lines)}'
                    
                    csv_line = ['n', parts_song, parts_artist, '----', parts_watch, parts_playlist, parts_rel_rank]
                    writer.writerow(csv_line)
                    
                    print(f"Written Line: {csv_line}")
                    count -= 1
            writer.writerow([])
            print(f'\n{filename} Playlist Written\n\n')

    print(f"\nCompleted: {output_file}")


def folders_to_playlists(input_root, output_root):

    output_root = os.path.abspath(output_root)

    print("\nInput:", input_root)
    print("Output:", output_root, "\n")

    os.makedirs(output_root, exist_ok=True)

    for root, dirs, files in os.walk(input_root):
        
        if root == input_root:
            continue

        sub = os.path.basename(root)
        output_path = os.path.join(output_root, f"{sub}.m3u8")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write(f"#{sub}\n\n")

            for file in files:
                abs_path = os.path.abspath(os.path.join(root, file))
                f.write(abs_path + "\n")

        print(f"Created: {output_path}")


def fix_playlists(root_path, pattern, replacement):
    regex = re.compile(pattern)

    for name in os.listdir(root_path):
        path = os.path.join(root_path, name)

        if not os.path.isfile(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = regex.sub(replacement, content)

        if new_content != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Modificato: {path}")
        else:
            print(f"Nessuna occorrenza in: {path}")
