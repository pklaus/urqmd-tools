#!/usr/bin/env python

import copy, os, shutil, subprocess, tempfile

def run_urqmd(config, output_basename, executable='urqmd', cache_tables=False):

    with tempfile.TemporaryDirectory() as td:

        # Locate the executable
        try:
            executable = subprocess.check_output('which ' + executable, shell=True)
            executable = executable.decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            if e.returncode == 1:
                print("Executable", executable, "not found in PATH...")
                return

        # If cache_tables is set to True, the tables.dat will be cached
        # in the directory of the urqmd executable
        if cache_tables == True:
            cache_tables = os.path.join(os.path.dirname(executable), 'tables.dat')
        if type(cache_tables) is str and not cache_tables.endswith('tables.dat'):
            raise NameError('cache_tables should point to a tables.dat file')

        # Determine the aboslute path of the output basename
        # as we are about to change the working directory
        output_basename = os.path.abspath(output_basename) #os.getcwd()

        os.chdir(td)

        # link the tables.dat file into the temporary directory
        if type(cache_tables) is str and os.path.exists(cache_tables):
            os.symlink(cache_tables, 'tables.dat')

        # Dump the urqmd configuration to a file:
        with open('urqmd.conf', 'w') as f:
            f.write(config)

        # run UrQMD
        env = copy.copy(os.environ)
        env.update({'ftn09': 'urqmd.conf', 'ftn14': 'urqmd_output.f14'})
        subprocess.run(executable, shell=True, check=True, env=env)

        # if the tables.dat is not yet cached but should be, move it into place
        if type(cache_tables) is str and not os.path.exists(cache_tables):
            shutil.move('tables.dat', cache_tables)

        # Put our output files in the desired place
        shutil.move('urqmd_output.f14', output_basename + '.f14')
        shutil.move('urqmd.conf', output_basename + '.urqmd.conf')

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('configuration', type=argparse.FileType('r'))
    parser.add_argument('output_basename')
    parser.add_argument('--cache-tables', action='store_true')
    args = parser.parse_args()

    run_urqmd(args.configuration.read(), args.output_basename, cache_tables=args.cache_tables)

if __name__ == "__main__":
    main()
