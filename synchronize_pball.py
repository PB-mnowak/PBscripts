from os import system, path, getcwd, listdir
import argparse


def main(target_dir):
    target_dir = target_dir
    source_dir = getcwd()
    synchronize(source_dir, target_dir)


def synchronize(source_dir, target_dir):
    common = _get_common_elements(source_dir, target_dir)
    if common:
        padding = max(map(len, common)) + 2
        for element in common:
            try:
                elem_source_path = path.join(source_dir, element)
                elem_target_path = path.join(target_dir, element)
                
                if path.isfile(elem_source_path):
                    if path.getmtime(elem_source_path) > path.getmtime(elem_target_path):
                        system(f'copy "{elem_source_path}" "{target_dir}" > nul')
                        print(f'> {element}{" " * (padding-len(element))} → File updated on PB all: {target_dir}')
                    elif path.getmtime(elem_source_path) < path.getmtime(elem_target_path):
                        system(f'copy "{elem_target_path}" "{source_dir}" > nul')
                        print(f'> {element}{" " * (padding-len(element))} ← File updated on local: {source_dir}')
                else:
                    sub_source_dir = path.join(source_dir, element)
                    sub_target_dir = path.join(target_dir, element)
                    synchronize(sub_source_dir, sub_target_dir)

            except Exception as e:
                print(e)


def _get_elements(mypath):
    return set(listdir(mypath))


def _get_common_elements(source_dir, target_dir):
    local = _get_elements(source_dir)
    target = _get_elements(target_dir)
    return local.intersection(target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('target_dir', action='store', type=str)
    args = parser.parse_args()

    main(args.target_dir)
