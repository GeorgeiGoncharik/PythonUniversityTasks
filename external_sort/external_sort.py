import argparse
import heapq
import os
import tempfile


class ExternalMergeSort:

    def __init__(self):
        self.sortedTempFileHandlerList = []
        self.cwd = os.getcwd()

    def split_files(self, large_file, small_file_size):
        large_file_handler = open(large_file)
        temp_buffer = []
        size = 0
        while True:
            number = large_file_handler.readline()
            if not number:
                if len(temp_buffer) > 0:
                    temp_buffer = sorted(temp_buffer, key=lambda no: int(no.strip()))
                    temp_file = tempfile.NamedTemporaryFile(mode='w+', dir=self.cwd + '/temp', delete=False)
                    temp_file.writelines([str(el) for el in temp_buffer])
                    temp_file.seek(0)
                    self.sortedTempFileHandlerList.append(temp_file)
                    break

                break

            temp_buffer.append(number)
            size += 1
            if size % small_file_size == 0:
                temp_buffer = sorted(temp_buffer, key=lambda no: int(no.strip()))
                temp_file = tempfile.NamedTemporaryFile(mode='w+', dir=self.cwd + '/temp', delete=False)
                temp_file.writelines([str(num) for num in temp_buffer])
                temp_file.seek(0)
                self.sortedTempFileHandlerList.append(temp_file)
                temp_buffer = []

    def merge_sorted_temp_files(self):
        merged_node = (map(int, tempFileHandler) for tempFileHandler in self.sortedTempFileHandlerList)
        sorted_complete_data = heapq.merge(*merged_node)
        return sorted_complete_data


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

    if os.path.exists(args.indir):
        sorting_machine = ExternalMergeSort()
        sorting_machine.split_files(args.indir, 10)
        sorted_data = sorting_machine.merge_sorted_temp_files()

        with open(args.outdir, mode="w") as f:
            for el in sorted_data:
                f.write(str(el) + '\n')
