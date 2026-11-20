import pathlib

def filter_file(filename_in, filename_out, cond):
    base_path = pathlib.Path("data")
    input_path = base_path / filename_in
    output_path = base_path / filename_out

    with (open(input_path, "r") as fr, open(output_path, "w") as fw):
        for line in fr.readlines():
            try:
                if cond(line):
                    fw.write(line)
            except ValueError:
                print("Invalid value, skipping...")
            except Exception as e:
                print(f"Error: {e}")
        fw.close()


def odd(s): return int(s) % 2 == 1
filter_file("small_ints.txt", "small_ints_out.txt", odd)