import argparse
import heapq
import os
import tempfile

class ExternalMergeSort:

    def __init__(self):
        self.sorted_temp_file_name_list = []

    def sort(self, infile, small_file_size=10):
        with tempfile.TemporaryDirectory(dir='/tmp') as temp_directory:
            if os.path.exists(infile):
                with open(infile) as large_file_handler:
                    temp_buffer = []
                    size = 0
                    while True:
                        number = large_file_handler.readline()
                        if not number:
                            if len(temp_buffer) > 0:
                                temp_buffer = sorted(temp_buffer, key=lambda no: int(no.strip()))
                                with tempfile.NamedTemporaryFile(mode='w+', dir=temp_directory,
                                                                 delete=False) as temp_file:
                                    temp_file.writelines([str(num) for num in temp_buffer])
                                    self.sorted_temp_file_name_list.append(temp_file.name)
                            break

                        temp_buffer.append(number)
                        size += 1
                        if size % small_file_size == 0:
                            temp_buffer = sorted(temp_buffer, key=lambda no: int(no.strip()))
                            with tempfile.NamedTemporaryFile(mode='w+', dir=temp_directory, delete=False) as temp_file:
                                temp_file.writelines([str(num) for num in temp_buffer])
                                self.sorted_temp_file_name_list.append(temp_file.name)
                            temp_buffer = []

                merged_node = (map(int, handler) for handler in
                               (open(temp_file) for temp_file in self.sorted_temp_file_name_list))
                return heapq.merge(*merged_node)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "indir",
        type=str,
        help='file with numbers to be sorted')
    parser.add_argument(
        "outdir",
        type=str,
        help='file with sorted numbers to be saved')
    args = parser.parse_args()

    sorting_machine = ExternalMergeSort()
    sorted_data = sorting_machine.sort(args.indir)

    if os.path.exists(args.outdir):
        with open(args.outdir, mode="w") as f:
            for el in sorted_data:
                f.write(str(el) + '\n')

