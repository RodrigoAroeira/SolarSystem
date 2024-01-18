import sys

args = {
    '-- version': '1.0.0',
    '--main': 'main.py',
}


if not len(sys.argv) > 1:
    from __init__ import _example as main
    main()
else:
    args.get(sys.argv[1], None)