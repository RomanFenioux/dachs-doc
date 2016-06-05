def replace_gavo_url(sub):
    import os
    import glob
    import fileinput
    import re
    pat = 'http://docs.g-vo.org/DaCHS'
    src_dir = os.path.abspath('docs/source/')
    rst_fls = glob.glob(os.path.join(src_dir,'*.rstx'))
    for _f in rst_fls:
        _file = fileinput.FileInput(_f, inplace=True)
        for _line in _file:
            _line = re.sub(pat,sub,_line.rstrip())
            print _line
        _file.close()

if __name__ == '__main__':
    import sys
    opt = sys.argv[1]
    if opt=='install':
        import os
        on_rtd = os.environ.get('READTHEDOCS') == 'True'
        if on_rtd:
            new_url = 'http://dachs-doc.rtfd.io/en/latest'
            replace_gavo_url(new_url)
        else:
            print ""
            print "So far, only ReadTheDocs support has been added."
            print "Exiting without modifications."
            print ""

